from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
import uuid

class PersonalInfo(BaseModel):
    date_of_birth: Optional[str] = None
    gender: Optional[str] = None
    marital_status: Optional[str] = None
    nationality: Optional[List[Dict[str, Any]]] = None
    current_residence: Optional[Dict[str, Any]] = None
    phone: Optional[str] = None
    address: Optional[Dict[str, Any]] = None

class Education(BaseModel):
    institution: Optional[str] = None
    degree: Optional[str] = None
    field_of_study: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    country: Optional[str] = None
    description: Optional[str] = None

class WorkExperience(BaseModel):
    company: Optional[str] = None
    position: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    country: Optional[str] = None
    description: Optional[str] = None
    skills: Optional[List[str]] = None

class LanguageProficiency(BaseModel):
    language: Optional[str] = None
    proficiency: Optional[str] = None
    certification: Optional[str] = None
    certification_date: Optional[str] = None

class FinancialInformation(BaseModel):
    annual_income: Optional[float] = None
    savings: Optional[float] = None
    assets: Optional[float] = None
    currency: Optional[str] = None

class ImmigrationHistory(BaseModel):
    previous_applications: Optional[List[Dict[str, Any]]] = None
    visa_history: Optional[List[Dict[str, Any]]] = None
    travel_history: Optional[List[Dict[str, Any]]] = None
    refusals: Optional[List[Dict[str, Any]]] = None

class Preferences(BaseModel):
    target_countries: Optional[List[str]] = None
    immigration_goals: Optional[List[str]] = None
    timeline: Optional[str] = None
    budget: Optional[float] = None
    family_size: Optional[int] = None

class ReadinessChecklistItem(BaseModel):
    item_id: str
    title: str
    description: Optional[str] = None
    is_complete: bool = False
    completed_at: Optional[str] = None
    notes: Optional[str] = None

class ProfileCreate(BaseModel):
    personal_info: Optional[PersonalInfo] = None
    education: Optional[List[Education]] = None
    work_experience: Optional[List[WorkExperience]] = None
    language_proficiency: Optional[List[LanguageProficiency]] = None
    financial_information: Optional[FinancialInformation] = None
    immigration_history: Optional[ImmigrationHistory] = None
    preferences: Optional[Preferences] = None
    readiness_checklist: Optional[List[ReadinessChecklistItem]] = None

class ProfileResponse(BaseModel):
    id: uuid.UUID
    email: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    personal_info: Optional[Dict[str, Any]] = None
    education: Optional[List[Dict[str, Any]]] = None
    work_experience: Optional[List[Dict[str, Any]]] = None
    language_proficiency: Optional[List[Dict[str, Any]]] = None
    financial_information: Optional[Dict[str, Any]] = None
    immigration_history: Optional[Dict[str, Any]] = None
    preferences: Optional[Dict[str, Any]] = None
    readiness_checklist: Optional[List[Dict[str, Any]]] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class ProfileUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    personal_info: Optional[Dict[str, Any]] = None
    education: Optional[List[Dict[str, Any]]] = None
    work_experience: Optional[List[Dict[str, Any]]] = None
    language_proficiency: Optional[List[Dict[str, Any]]] = None
    financial_information: Optional[Dict[str, Any]] = None
    immigration_history: Optional[Dict[str, Any]] = None
    preferences: Optional[Dict[str, Any]] = None
