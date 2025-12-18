import hashlib

from app.exceptions import BadRequestError, NotFoundError
from app.models import (
    Application,
    ApplicationCreate,
    LoginRequest,
    Opportunity,
    OpportunityCreate,
    RegisterRequest,
    User,
)
from app.singleton import DbSingleton


def _hash_password(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


class AuthService:
    def __init__(self):
        self.db = DbSingleton.get_db()

    def register(self, req: RegisterRequest) -> User:
        for user in self.db.users.values():
            if user.email == req.email:
                raise BadRequestError("Email already exists")

        user = User(
            id=self.db.user_seq,
            full_name=req.full_name,
            email=req.email,
            password_hash=_hash_password(req.password),
        )
        self.db.users[user.id] = user
        self.db.user_seq += 1
        return user

    def login(self, req: LoginRequest) -> User:
        for user in self.db.users.values():
            if user.email == req.email:
                if user.password_hash != _hash_password(req.password):
                    raise BadRequestError("Invalid credentials")
                return user
        raise BadRequestError("Invalid credentials")


class OpportunityService:
    def __init__(self):
        self.db = DbSingleton.get_db()

    def create(self, req: OpportunityCreate) -> Opportunity:
        opp = Opportunity(
            id=self.db.opportunity_seq,
            title=req.title,
            country=req.country,
            type=req.type,
            deadline=req.deadline,
        )
        self.db.opportunities[opp.id] = opp
        self.db.opportunity_seq += 1
        return opp

    def list_all(self):
        return list(self.db.opportunities.values())


class ApplicationService:
    def __init__(self):
        self.db = DbSingleton.get_db()

    def apply(self, req: ApplicationCreate) -> Application:
        if req.user_id not in self.db.users:
            raise NotFoundError("User not found")
        if req.opportunity_id not in self.db.opportunities:
            raise NotFoundError("Opportunity not found")

        app = Application(
            id=self.db.application_seq,
            user_id=req.user_id,
            opportunity_id=req.opportunity_id,
            status="SUBMITTED",
        )
        self.db.applications[app.id] = app
        self.db.application_seq += 1
        return app

    def list_all(self):
        return list(self.db.applications.values())
