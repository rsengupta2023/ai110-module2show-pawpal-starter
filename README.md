# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Features

- **Pet and task management** — Create an owner profile, add multiple pets, and attach care tasks to each pet.
- **Chronological sorting** — `Scheduler.sort_by_time()` orders tasks by preferred time and supports both 24-hour and AM/PM formats.
- **Pet and status filtering** — `Scheduler.filter_tasks()` filters tasks by pet name, completion status, or both.
- **Daily planning** — `Scheduler.build_daily_plan()` prioritizes due tasks and selects tasks that fit the owner's available time.
- **Conflict warnings** — `Scheduler.detect_conflicts()` identifies exact matching task times and returns readable warnings instead of stopping the program.
- **Daily and weekly recurrence** — Completing a recurring task creates its next occurrence using `timedelta`.
- **Streamlit interface** — Add pets and tasks interactively, view current tasks, and generate a schedule with success and warning messages.

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## 🖥️ Sample Output

Paste a sample of your app's CLI or Streamlit output here so a reader can see what a generated plan looks like:

Today's Schedule
================
9:00 AM - Medication (5 min)
6:00 PM - Evening feeding (10 min)
8:00 AM - Morning walk (20 min)

## 🧪 Testing PawPal+

```bash
python -m pytest
```

The test suite covers:

- Task completion status changes.
- Adding tasks to a pet.
- Sorting tasks chronologically by preferred time.
- Creating the next-day occurrence for a completed daily task.
- Detecting duplicate task times and returning a warning.

Successful test run:

```text
============================= test session starts ==============================
platform darwin -- Python 3.9.6, pytest-8.4.2, pluggy-1.6.0
rootdir: /Users/rudra/Library/CloudStorage/OneDrive-FloridaAtlanticUniversity(2)/FAU FALL 2026 (Sem 8)/CEN 5035 (Software Engineering)/CP Week 5 project submission/ai110-module2show-pawpal-starter
collected 5 items

tests/test_pawpal.py .....                                               [100%]

============================== 5 passed in 0.01s ===============================
```

**Confidence Level:** (4/5 stars)

The tests cover the most important implemented behaviors, including task management,
sorting, recurrence, and conflict detection. Additional tests for invalid input,
overlapping task durations, weekly recurrence, and scheduler time limits would increase
confidence further.

## 📐 Smarter Scheduling

PawPal+ includes the following scheduling features in
[`pawpal_system.py`](./pawpal_system.py):

| Feature | Method(s) | Behavior |
|---------|-----------|---------|
| Task sorting | `Planner.sort_by_time()` / `Scheduler.sort_by_time()` | Uses `sorted()` with a lambda key to convert `HH:MM` and AM/PM time strings into sortable values, then orders tasks chronologically. |
| Task filtering | `Planner.filter_tasks()` / `Scheduler.filter_tasks()` | Filters tasks by pet name, completion status, or both. For example, it can return only Mochi's incomplete tasks. |
| Conflict detection | `Planner.detect_conflicts()` / `Scheduler.detect_conflicts()` | Groups tasks by preferred start time and returns warning messages when two or more tasks share the same time. It does not stop the program. |
| Recurring tasks | `CareTask.mark_complete()`, `CareTask.next_occurrence()`, and `Planner.complete_task()` / `Scheduler.complete_task()` | Creates a new occurrence for daily tasks due the next day and weekly tasks due one week later, using `timedelta`. |

The current conflict check identifies exact matching start times. It does not yet detect
overlaps caused by task durations, such as a 9:00 AM task lasting 30 minutes and another
task starting at 9:15 AM.

## Demo Walkthrough

1. Start the Streamlit app and enter the owner's name in the **Owner and Pets** section.
2. Use **Add pet** to create a pet profile with its name, species, and age. The pet is stored in
   Streamlit session state so it remains available across page reruns.
3. Select a pet, enter a task title, duration, priority, and preferred time, then click **Add task**.
   The task is created through the backend `Pet.add_task()` method and appears in the current-task table.
4. Click **Generate schedule** to retrieve incomplete tasks through the `Scheduler`, prioritize them,
   and display them in chronological order using `Scheduler.sort_by_time()`.
5. Review the schedule table, which includes the pet, task, preferred time, duration, and priority.
   If two tasks have the same preferred time, the UI displays a warning identifying both tasks and
   suggesting that one preferred time be changed. The scheduler also supports filtering tasks by pet
   or completion status and creates the next occurrence when a daily or weekly task is completed.

The terminal demonstration in [`main.py`](./main.py) produces output like this:

```text
Today's Schedule
================
08:00 - Morning walk (20 min)
09:00 - Morning feeding (10 min)
09:00 - Medication (5 min)
18:00 - Evening feeding (10 min)

Schedule Warnings
-----------------
Warning: Conflict at 09:00: Mochi: Morning feeding, Luna: Medication are scheduled at the same time.

Mochi's Tasks
-------------
18:00 - Evening feeding
08:00 - Morning walk
09:00 - Morning feeding

Incomplete Tasks
----------------
18:00 - Evening feeding
09:00 - Morning feeding
09:00 - Medication
```
