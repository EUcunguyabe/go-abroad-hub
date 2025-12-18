from __future__ import annotations

from pydantic import BaseModel, EmailStr, Field


class RegisterRequest(BaseModel):
    full_name: str = Field(min_length=1, max_length=100)
    email: EmailStr
    password: str = Field(min_length=6, max_length=100)


class LoginRequest(BaseModel):
    email: EmailStr
    password: str = Field(min_length=1, max_length=100)


class User(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    password_hash: str


class OpportunityCreate(BaseModel):
    title: str = Field(min_length=1, max_length=150)
    country: str = Field(min_length=1, max_length=80)
    type: str = Field(min_length=1, max_length=30)  # STUDY / WORK / VOLUNTEER
    deadline: str = Field(min_length=1, max_length=30)


class Opportunity(BaseModel):
    id: int
    title: str
    country: str
    type: str
    deadline: str


class ApplicationCreate(BaseModel):
    user_id: int
    opportunity_id: int


class Application(BaseModel):
    id: int
    user_id: int
    opportunity_id: int
    status: str
