import os
from typing import Optional # Added Optional import
from supabase import create_client, Client
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables from .env file for local development
# Ensures .env in the same directory as this file is loaded.
dotenv_path = Path(__file__).resolve().parent / '.env'
load_dotenv(dotenv_path=dotenv_path)

SUPABASE_URL: Optional[str] = os.getenv("SUPABASE_URL")
SUPABASE_ANON_KEY: Optional[str] = os.getenv("SUPABASE_ANON_KEY")
# SUPABASE_SERVICE_ROLE_KEY: Optional[str] = os.getenv("SUPABASE_SERVICE_ROLE_KEY") # For admin tasks if needed

if not SUPABASE_URL or not SUPABASE_ANON_KEY:
    print("Warning: SUPABASE_URL or SUPABASE_ANON_KEY environment variables not found.")
    # In a real app, you might want to raise an error or have a more robust fallback.
    # For now, this will cause an error when trying to create the client if vars are missing.
    # This helps in early detection during development if .env is not set up.

# Initialize Supabase client
# This will raise an error if URL or Key is None, which is good for catching config issues.
try:
    supabase: Client = create_client(SUPABASE_URL, SUPABASE_ANON_KEY) # type: ignore
except Exception as e:
    print(f"Error initializing Supabase client: {e}")
    # Fallback to a None client or re-raise, depending on desired behavior on init failure
    supabase = None # type: ignore 

def get_supabase_client() -> Client:
    if supabase is None:
        # This would happen if the initial create_client failed.
        raise RuntimeError("Supabase client not initialized. Check SUPABASE_URL and SUPABASE_ANON_KEY environment variables.")
    return supabase

# Example of how to use the service role key if needed for specific admin operations
# def get_supabase_admin_client() -> Client:
#     if not SUPABASE_SERVICE_ROLE_KEY:
#         raise ValueError("SUPABASE_SERVICE_ROLE_KEY not set for admin operations.")
#     return create_client(SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY)

if __name__ == "__main__":
    # Test if client initializes (requires .env file in this directory or env vars set)
    print(f"SUPABASE_URL from env: {SUPABASE_URL}")
    print(f"SUPABASE_ANON_KEY from env (first 10 chars): {SUPABASE_ANON_KEY[:10] if SUPABASE_ANON_KEY else None}")
    try:
        client = get_supabase_client()
        print("Supabase client obtained successfully.")
        # Example: try a simple call if you have auth set up (this will likely fail without a user/pass)
        # auth_response = client.auth.sign_in_with_password({"email": "test@example.com", "password": "password"})
        # print(auth_response)
    except Exception as e:
        print(f"Error during Supabase client test: {e}")
