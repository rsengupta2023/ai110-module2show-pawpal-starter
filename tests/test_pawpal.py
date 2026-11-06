from pawpal_system import Pet, Task


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
