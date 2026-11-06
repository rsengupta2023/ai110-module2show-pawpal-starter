from datetime import date, timedelta

from pawpal_system import Owner, Pet, Scheduler, Task


def make_task() -> Task:
    return Task(
        name="Morning walk",
        category="exercise",
        description="Take the pet for a walk",
        duration=20,
        priority="high",
        frequency="daily",
        deadline="",
        preferred_time="8:00 AM",
    )


def test_task_completion() -> None:
    task = make_task()

    task.mark_complete()

    assert task.completed is True


def test_task_addition() -> None:
    pet = Pet(name="Mochi", species="dog", age=3)

    pet.add_task(make_task())

    assert len(pet.get_tasks()) == 1


def test_sorting_tasks_by_time() -> None:
    owner = Owner("Jordan")
    pet = Pet(name="Mochi", species="dog", age=3)
    tasks = [
        make_task(),
        Task(
            name="Evening feeding",
            category="feeding",
            description="Serve dinner",
            duration=10,
            priority="high",
            frequency="daily",
            deadline="",
            preferred_time="18:00",
        ),
        Task(
            name="Medication",
            category="medication",
            description="Give medication",
            duration=5,
            priority="high",
            frequency="daily",
            deadline="",
            preferred_time="09:00",
        ),
    ]
    for task in tasks:
        pet.add_task(task)
    owner.add_pet(pet)

    sorted_tasks = Scheduler(owner=owner).sort_by_time(tasks)

    assert [task.name for task in sorted_tasks] == [
        "Morning walk",
        "Medication",
        "Evening feeding",
    ]


def test_daily_task_completion_creates_next_day_task() -> None:
    task = make_task()

    next_task = task.mark_complete()

    assert task.completed is True
    assert next_task is not None
    assert next_task.completed is False
    assert next_task.due_date == date.today() + timedelta(days=1)


def test_scheduler_flags_duplicate_task_times() -> None:
    owner = Owner("Jordan")
    pet = Pet(name="Mochi", species="dog", age=3)
    first_task = make_task()
    duplicate_time_task = Task(
        name="Medication",
        category="medication",
        description="Give medication",
        duration=5,
        priority="high",
        frequency="daily",
        deadline="",
        preferred_time="08:00",
    )
    pet.add_task(first_task)
    pet.add_task(duplicate_time_task)
    owner.add_pet(pet)

    warnings = Scheduler(owner=owner).detect_conflicts()

    assert len(warnings) == 1
    assert "08:00" in warnings[0]
    assert "Morning walk" in warnings[0]
    assert "Medication" in warnings[0]
