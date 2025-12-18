from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict

from app.models import Application, Opportunity, User


@dataclass
class InMemoryDatabase:
    users: Dict[int, User] = field(default_factory=dict)
    opportunities: Dict[int, Opportunity] = field(default_factory=dict)
    applications: Dict[int, Application] = field(default_factory=dict)

    user_seq: int = 1
    opportunity_seq: int = 1
    application_seq: int = 1


class DbSingleton:
    _instance: InMemoryDatabase | None = None

    @classmethod
    def get_db(cls) -> InMemoryDatabase:
        if cls._instance is None:
            cls._instance = InMemoryDatabase()
        return cls._instance
