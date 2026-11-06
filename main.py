from datetime import date

from pawpal_system import Owner, OwnerPreferences, Pet, Scheduler, Task


def main() -> None:
    owner = Owner(
        name="Jordan",
        preferences=OwnerPreferences(available_time=60),
    )

    mochi = Pet(name="Mochi", species="dog", age=3, breed="Mixed")
    luna = Pet(name="Luna", species="cat", age=5, breed="Domestic Shorthair")

    mochi.add_task(
        Task(
            name="Evening feeding",
            category="feeding",
            description="Serve Mochi dinner",
            duration=10,
            priority="high",
            frequency="daily",
            deadline="",
            preferred_time="18:00",
        )
    )
    mochi.add_task(
        Task(
            name="Morning walk",
            category="exercise",
            description="Take Mochi for a walk",
            duration=20,
            priority="high",
            frequency="daily",
            deadline="",
            preferred_time="08:00",
        )
    )
    mochi.add_task(
        Task(
            name="Morning feeding",
            category="feeding",
            description="Serve Mochi breakfast",
            duration=10,
            priority="medium",
            frequency="daily",
            deadline="",
            preferred_time="09:00",
        )
    )
    luna.add_task(
        Task(
            name="Medication",
            category="medication",
            description="Give Luna her prescribed medication",
            duration=5,
            priority="high",
            frequency="daily",
            deadline="",
            preferred_time="09:00",
        )
    )

    owner.add_pet(mochi)
    owner.add_pet(luna)

    scheduler = Scheduler(owner=owner, plan_date=date.today())
    all_tasks = owner.get_all_tasks()
    sorted_tasks = scheduler.sort_by_time(all_tasks)

    print("Today's Schedule")
    print("================")
    for task in sorted_tasks:
        print(f"{task.preferred_time} - {task.name} ({task.duration} min)")

    warnings = scheduler.detect_conflicts(sorted_tasks)
    if warnings:
        print("\nSchedule Warnings")
        print("-----------------")
        for warning in warnings:
            print(f"Warning: {warning}")

    print("\nMochi's Tasks")
    print("-------------")
    for task in scheduler.filter_tasks(pet_name="Mochi"):
        print(f"{task.preferred_time} - {task.name}")

    sorted_tasks[0].mark_complete()
    print("\nIncomplete Tasks")
    print("----------------")
    for task in scheduler.filter_tasks(completed=False):
        print(f"{task.preferred_time} - {task.name}")


if __name__ == "__main__":
    main()
