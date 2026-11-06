"""Core data models and service skeleton for the PawPal+ system."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from typing import Any


@dataclass
class Owner:
    """Represents a pet owner and the owner's pets and preferences."""

    name: str
    pets: list[Pet] = field(default_factory=list)
    preferences: OwnerPreferences | None = None

    def add_pet(self, pet: Pet) -> None:
        """Add a pet to the owner's profile."""
        pass

    def remove_pet(self, pet: Pet) -> None:
        """Remove a pet from the owner's profile."""
        pass


@dataclass
class Pet:
    """Represents a pet and the care tasks associated with that pet."""

    name: str
    species: str
    age: int
    breed: str = ""
    health_needs: str = ""
    pet_preferences: str = ""
    care_tasks: list[CareTask] = field(default_factory=list)

    def add_task(self, task: CareTask) -> None:
        """Add a care task to the pet's task list."""
        pass

    def remove_task(self, task: CareTask) -> None:
        """Remove a care task from the pet's task list."""
        pass

    def update_health_needs(self, health_needs: str) -> None:
        """Update the pet's health-related care information."""
        pass

    def get_tasks(self) -> list[CareTask]:
        """Return the pet's care tasks."""
        pass


@dataclass
class CareTask:
    """Represents one care activity for a pet."""

    name: str
    category: str
    description: str
    duration: int
    priority: str
    frequency: str
    deadline: str
    preferred_time: str
    completed: bool = False

    def mark_complete(self) -> None:
        """Mark the task as completed."""
        pass

    def mark_incomplete(self) -> None:
        """Mark the task as incomplete."""
        pass

    def update_details(self, **details: Any) -> None:
        """Update task details."""
        pass

    def is_due(self) -> bool:
        """Determine whether the task is due."""
        pass

    def fits_time_available(self, minutes: int) -> bool:
        """Determine whether the task fits within the available time."""
        pass


@dataclass
class OwnerPreferences:
    """Represents the owner's scheduling preferences and constraints."""

    available_time: int
    preferred_task_times: str = ""
    priority_preferences: str = ""
    excluded_activities: str = ""
    maximum_daily_tasks: int = 0

    def update_preferences(self, **preferences: Any) -> None:
        """Update the owner's scheduling preferences."""
        pass

    def is_preferred_time(self, task: CareTask) -> bool:
        """Determine whether a task matches a preferred time."""
        pass

    def allows_task(self, task: CareTask) -> bool:
        """Determine whether the preferences allow a task."""
        pass

    def get_available_minutes(self) -> int:
        """Return the owner's available care time."""
        pass


@dataclass
class DailyPlan:
    """Represents the care plan generated for one day."""

    plan_date: date
    selected_tasks: list[CareTask] = field(default_factory=list)
    deferred_tasks: list[CareTask] = field(default_factory=list)
    total_duration: int = 0
    available_time: int = 0
    explanation: str = ""

    def add_task(self, task: CareTask) -> None:
        """Add a task to the daily plan."""
        pass

    def remove_task(self, task: CareTask) -> None:
        """Remove a task from the daily plan."""
        pass

    def calculate_total_duration(self) -> int:
        """Calculate the duration of the selected tasks."""
        pass

    def is_within_time_limit(self) -> bool:
        """Determine whether the plan fits within the available time."""
        pass

    def generate_explanation(self) -> str:
        """Generate an explanation for the plan's decisions."""
        pass

    def get_summary(self) -> str:
        """Return a readable summary of the daily plan."""
        pass


@dataclass
class Planner:
    """Creates a daily plan from an owner's pets, tasks, and preferences."""

    plan_date: date

    def collect_due_tasks(self, date_to_plan: date) -> list[CareTask]:
        """Collect tasks due on a particular date."""
        pass

    def prioritize_tasks(self, tasks: list[CareTask]) -> list[CareTask]:
        """Order tasks according to priority and constraints."""
        pass

    def build_daily_plan(self) -> DailyPlan:
        """Build a daily plan."""
        pass

    def defer_task(self, task: CareTask) -> None:
        """Defer a task that cannot be included in the current plan."""
        pass

    def explain_decision(self, task: CareTask) -> str:
        """Explain why a task was selected or deferred."""
        pass
