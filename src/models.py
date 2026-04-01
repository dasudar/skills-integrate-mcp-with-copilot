"""Database models for activities and participants."""

from sqlalchemy import Column, String, Integer, ForeignKey, List
from sqlalchemy.orm import relationship
from database import Base


class Activity(Base):
    """Activity model."""
    __tablename__ = "activities"

    name = Column(String, primary_key=True, index=True)
    description = Column(String)
    schedule = Column(String)
    max_participants = Column(Integer)

    # Relationship to participants
    participants = relationship(
        "Participant",
        back_populates="activity",
        cascade="all, delete-orphan"
    )

    def to_dict(self):
        """Convert activity to dictionary format."""
        return {
            "name": self.name,
            "description": self.description,
            "schedule": self.schedule,
            "max_participants": self.max_participants,
            "participants": [p.email for p in self.participants]
        }


class Participant(Base):
    """Participant model."""
    __tablename__ = "participants"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, index=True)
    activity_name = Column(String, ForeignKey("activities.name"))

    # Relationship back to activity
    activity = relationship("Activity", back_populates="participants")
