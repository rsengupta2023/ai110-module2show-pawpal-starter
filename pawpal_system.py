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
        if pet not in self.pets:
            self.pets.append(pet)

    def remove_pet(self, pet: Pet) -> None:
        """Remove a pet from the owner's profile."""
        self.pets.remove(pet)

    def get_all_tasks(self) -> list[CareTask]:
        """Return every task belonging to every pet owned by this owner."""
        return [task for pet in self.pets for task in pet.get_tasks()]


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
        if task not in self.care_tasks:
            self.care_tasks.append(task)

    def remove_task(self, task: CareTask) -> None:
        """Remove a care task from the pet's task list."""
        self.care_tasks.remove(task)

    def update_health_needs(self, health_needs: str) -> None:
        """Update the pet's health-related care information."""
        self.health_needs = health_needs

    def get_tasks(self) -> list[CareTask]:
        """Return the pet's care tasks."""
        return list(self.care_tasks)


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
        self.completed = True

    def mark_incomplete(self) -> None:
        """Mark the task as incomplete."""
        self.completed = False

    def update_details(self, **details: Any) -> None:
        """Update task details."""
        allowed_fields = {
            "name",
            "category",
            "description",
            "duration",
            "priority",
            "frequency",
            "deadline",
            "preferred_time",
            "completed",
        }
        unknown_fields = set(details) - allowed_fields
        if unknown_fields:
            raise ValueError(f"Unknown task fields: {sorted(unknown_fields)}")
        for field_name, value in details.items():
            setattr(self, field_name, value)

    def is_due(self) -> bool:
        """Determine whether the task is due."""
        return not self.completed

    def fits_time_available(self, minutes: int) -> bool:
        """Determine whether the task fits within the available time."""
        return minutes >= self.duration


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
        return self.available_time


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
        if task not in self.selected_tasks:
            self.selected_tasks.append(task)
            self.calculate_total_duration()

    def remove_task(self, task: CareTask) -> None:
        """Remove a task from the daily plan."""
        self.selected_tasks.remove(task)
        self.calculate_total_duration()

    def calculate_total_duration(self) -> int:
        """Calculate the duration of the selected tasks."""
        self.total_duration = sum(task.duration for task in self.selected_tasks)
        return self.total_duration

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

    plan_date: date = field(default_factory=date.today)
    owner: Owner | None = None
    current_plan: DailyPlan | None = field(default=None, init=False)

    def collect_due_tasks(self, date_to_plan: date) -> list[CareTask]:
        """Collect tasks due on a particular date."""
        if self.owner is None:
            return []
        return [task for task in self.owner.get_all_tasks() if task.is_due()]

    def prioritize_tasks(self, tasks: list[CareTask]) -> list[CareTask]:
        """Order tasks according to priority and constraints."""
        priority_order = {"high": 0, "medium": 1, "low": 2}
        return sorted(
            tasks,
            key=lambda task: (
                priority_order.get(task.priority.lower(), len(priority_order)),
                task.duration,
                task.name.lower(),
            ),
        )

    def build_daily_plan(self) -> DailyPlan:
        """Build a daily plan."""
        due_tasks = self.collect_due_tasks(self.plan_date)
        if self.owner is not None and self.owner.preferences is not None:
            available_time = self.owner.preferences.get_available_minutes()
        else:
            available_time = sum(task.duration for task in due_tasks)
        plan = DailyPlan(plan_date=self.plan_date, available_time=available_time)
        remaining_time = available_time

        for task in self.prioritize_tasks(due_tasks):
            if task.fits_time_available(remaining_time):
                plan.add_task(task)
                remaining_time -= task.duration
            else:
                plan.deferred_tasks.append(task)

        plan.calculate_total_duration()
        self.current_plan = plan
        return plan

    def defer_task(self, task: CareTask) -> None:
        """Defer a task that cannot be included in the current plan."""
        if self.current_plan is None:
            raise RuntimeError("Build a daily plan before deferring a task.")
        if task in self.current_plan.selected_tasks:
            self.current_plan.remove_task(task)
        if task not in self.current_plan.deferred_tasks:
            self.current_plan.deferred_tasks.append(task)

    def explain_decision(self, task: CareTask) -> str:
        """Explain why a task was selected or deferred."""
        if self.current_plan is None:
            raise RuntimeError("Build a daily plan before explaining a decision.")
        if task in self.current_plan.selected_tasks:
            return f"{task.name} was selected because it fits the available time."
        if task in self.current_plan.deferred_tasks:
            return f"{task.name} was deferred because it did not fit the available time."
        return f"{task.name} is not part of the current daily plan."


Task = CareTask
Scheduler = Planner
