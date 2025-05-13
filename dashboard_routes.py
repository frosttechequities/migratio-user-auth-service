from fastapi import APIRouter, Depends, HTTPException, status
from typing import Annotated, Optional, Dict, Any
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from supabase_client import get_supabase_client, Client
from gotrue.errors import AuthApiError
from models import UserResponse
import uuid

router = APIRouter(prefix="/dashboard", tags=["dashboard"])
bearer_scheme = HTTPBearer()

# Dependency to get current user from Supabase using JWT
async def get_current_user(
    auth: Annotated[HTTPAuthorizationCredentials, Depends(bearer_scheme)],
    supabase: Client = Depends(get_supabase_client)
) -> UserResponse:
    if auth.scheme.lower() != "bearer":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication scheme. Only Bearer is supported.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    token = auth.credentials
    
    try:
        user_response = supabase.auth.get_user(token)
        
        if user_response.user is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Not authenticated: Invalid token or user not found",
                headers={"WWW-Authenticate": "Bearer"},
            )
        
        return UserResponse(
            id=user_response.user.id,
            email=user_response.user.email,
            created_at=str(user_response.user.created_at) if user_response.user.created_at else None
        )
    except AuthApiError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Not authenticated: {e.message}",
            headers={"WWW-Authenticate": "Bearer"},
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error validating token: {str(e)}"
        )

@router.get("/data", summary="Get dashboard data for the current user")
async def get_dashboard_data(
    current_user: UserResponse = Depends(get_current_user),
    supabase: Client = Depends(get_supabase_client)
):
    try:
        # Get the user's profile
        profile_response = supabase.table("profiles").select("*").eq("id", str(current_user.id)).execute()
        
        if not profile_response.data or len(profile_response.data) == 0:
            # If profile doesn't exist, create a default one
            new_profile = {
                "id": str(current_user.id),
                "email": current_user.email,
                "first_name": "",
                "last_name": "",
                "personal_info": {},
                "education": [],
                "work_experience": [],
                "language_proficiency": [],
                "financial_information": {},
                "immigration_history": {},
                "preferences": {},
                "readiness_checklist": []
            }
            
            # Insert the new profile
            profile_response = supabase.table("profiles").insert(new_profile).execute()
            
            if not profile_response.data or len(profile_response.data) == 0:
                raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail="Failed to create profile"
                )
        
        profile = profile_response.data[0]
        
        # Create a mock dashboard data response
        dashboard_data = {
            "profile": profile,
            "stats": {
                "profileCompletion": 10,  # Placeholder value
                "documentsUploaded": 0,
                "documentsVerified": 0,
                "roadmapsCreated": 0,
                "roadmapsCompleted": 0
            },
            "recentActivity": [],
            "upcomingTasks": [],
            "recommendations": {
                "programs": [],
                "countries": []
            }
        }
        
        return dashboard_data
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error fetching dashboard data: {str(e)}"
        )
