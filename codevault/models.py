"""Data models for CodeVault."""
from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional


@dataclass
class Snippet:
    """Represents a code snippet."""
    id: str
    title: str
    code: str
    language: str
    tags: List[str]
    description: Optional[str] = None
    created_at: datetime = None
    updated_at: datetime = None
    
    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now()
        if self.updated_at is None:
            self.updated_at = datetime.now()
    
    def to_dict(self) -> dict:
        """Convert snippet to dictionary."""
        return {
            "id": self.id,
            "title": self.title,
            "code": self.code,
            "language": self.language,
            "tags": self.tags,
            "description": self.description,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> "Snippet":
        """Create snippet from dictionary."""
        return cls(
            id=data["id"],
            title=data["title"],
            code=data["code"],
            language=data["language"],
            tags=data["tags"],
            description=data.get("description"),
            created_at=datetime.fromisoformat(data["created_at"]),
            updated_at=datetime.fromisoformat(data["updated_at"]),
        )