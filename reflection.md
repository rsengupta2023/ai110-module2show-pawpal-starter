# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

I used six main classes. `Owner` stores the pets and owner preferences.
`Pet` stores pet information and its care tasks. `CareTask` represents one
activity, including its time, duration, priority, and frequency.
`OwnerPreferences` stores scheduling limits. `Planner` handles sorting,
filtering, conflicts, and plan creation. `DailyPlan` stores selected and
deferred tasks for a date. An owner has pets, pets have tasks, and the planner
uses the owner to create a schedule.

**b. Design changes**

Yes. The first UML was more basic. During implementation, I added `due_date`
and recurring-task methods to `CareTask`. I also added sorting, filtering,
conflict detection, and task completion methods to `Planner`. These changes were
needed because the app became more than a simple task list. I updated the final
UML to show these methods and the recurring-task relationship.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

The scheduler considers whether a task is incomplete, its priority, preferred
time, duration, and the owner’s available minutes. High-priority tasks are
considered first, but the final display is sorted by time. I treated health
and medication-related tasks as important because missing them could affect the
pet. Available time also matters because the plan should be realistic for a
busy owner.

**b. Tradeoffs**

The scheduler currently detects conflicts when two tasks have the same preferred start time. It does not yet detect tasks whose time ranges overlap because one task lasts longer than the other. For example, a 9:00 AM task lasting 30 minutes and a 9:15 AM task would not be reported as a conflict. This is a tradeoff because exact-time matching is simpler to implement and easy to explain, while still catching the most obvious scheduling conflicts. It is reasonable for this early version because the application focuses on demonstrating task organization and prioritization; a future version could compare each task's start and end times for more precise conflict detection.

---

## 3. AI Collaboration

**a. How you used AI**

I used the AI coding assistant for UML brainstorming, creating Python class
skeletons, connecting the backend to Streamlit, and writing tests. The most
helpful prompts were specific requests for one feature at a time, such as
sorting tasks by time, creating recurring tasks, and detecting conflicts.

**b. Judgment and verification**

I modified the suggested conflict-detection design because using task IDs made
the code harder to read for this small project. I changed it to use direct task
membership checks and a normal dictionary. I verified the change by running the
demo and the pytest suite.

Using separate chat sessions for each phase helped me stay organized. I could
focus on design first, then implementation, testing, UI integration, and final
documentation without mixing unrelated decisions.

---

## 4. Testing and Verification

**a. What you tested**

I tested task completion, adding tasks to pets, sorting tasks by time, creating
the next day for a completed daily task, and detecting duplicate task times.
These tests cover the main behaviors that make the scheduler different from a
basic list. They also helped catch mistakes in recurrence and time handling.

**b. Confidence**

I am fairly confident in the core behavior because all five tests pass. I would
next test weekly recurrence, invalid time strings, empty owners, exact time
limits, and overlapping durations. I would also test multiple tasks with the
same time across several pets.

---

## 5. Reflection

**a. What went well**

I am most satisfied with connecting the Streamlit UI to the backend classes.
Adding a pet or task in the UI now changes the actual objects in session state,
and the scheduler can use that data to create a plan.

**b. What you would improve**

I would improve the time model by using real date and time values instead of
mostly storing time as strings. I would also implement overlapping-duration
conflict detection and finish the preference methods.

**c. Key takeaway**

I learned that being the lead architect means deciding the structure and
checking the AI’s work instead of accepting every suggestion. AI helped me move
quickly, but I still had to choose simple class responsibilities, test the
behavior, and keep the UML, backend, and UI consistent.
