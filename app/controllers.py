from __future__ import annotations

from fastapi import APIRouter

from app.models import ApplicationCreate, LoginRequest, OpportunityCreate, RegisterRequest
from app.services import ApplicationService, AuthService, OpportunityService

router = APIRouter()


@router.post("/auth/register")
def register(req: RegisterRequest):
    user = AuthService().register(req)
    return {"id": user.id, "full_name": user.full_name, "email": user.email}


@router.post("/auth/login")
def login(req: LoginRequest):
    user = AuthService().login(req)
    return {"message": "Login successful", "user_id": user.id}


@router.post("/opportunities")
def create_opportunity(req: OpportunityCreate):
    opp = OpportunityService().create(req)
    return opp.model_dump()


@router.get("/opportunities")
def list_opportunities():
    opps = OpportunityService().list_all()
    return [o.model_dump() for o in opps]


@router.post("/applications")
def apply(req: ApplicationCreate):
    app_obj = ApplicationService().apply(req)
    return app_obj.model_dump()


@router.get("/applications")
def list_applications():
    apps = ApplicationService().list_all()
    return [a.model_dump() for a in apps]
