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
            name="Morning walk",
            category="exercise",
            description="Take Mochi for a walk",
            duration=20,
            priority="high",
            frequency="daily",
            deadline="",
            preferred_time="8:00 AM",
        )
    )
    mochi.add_task(
        Task(
            name="Evening feeding",
            category="feeding",
            description="Serve Mochi dinner",
            duration=10,
            priority="high",
            frequency="daily",
            deadline="",
            preferred_time="6:00 PM",
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
            preferred_time="9:00 AM",
        )
    )

    owner.add_pet(mochi)
    owner.add_pet(luna)

    scheduler = Scheduler(owner=owner, plan_date=date.today())
    plan = scheduler.build_daily_plan()

    print("Today's Schedule")
    print("================")
    for task in plan.selected_tasks:
        print(f"{task.preferred_time} - {task.name} ({task.duration} min)")

    if plan.deferred_tasks:
        print("\nDeferred Tasks")
        print("--------------")
        for task in plan.deferred_tasks:
            print(f"{task.name} ({task.duration} min)")


if __name__ == "__main__":
    main()
