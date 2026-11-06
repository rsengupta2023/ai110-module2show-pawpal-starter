# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

The initial design uses several classes, each with a focused responsibility:

- **Owner** — Represents the person using PawPal+. It stores the owner’s name, pets, and scheduling preferences, and provides operations for adding or removing pets.
- **Pet** — Represents an animal receiving care. It stores basic information such as the pet’s name, species, age, breed, health needs, and pet-specific preferences. It also maintains the care tasks assigned to that pet.
- **CareTask** — Represents an individual activity, such as walking, feeding, medication, grooming, or enrichment. It stores task details including category, duration, priority, frequency, deadline, preferred time, and completion status.
- **OwnerPreferences** — Stores the owner’s scheduling constraints, including available time, preferred task times, priority preferences, excluded activities, and the maximum number of daily tasks.
- **Planner** — Contains the scheduling responsibilities. It collects due tasks, prioritizes them, builds a daily plan, defers tasks that cannot be included, and explains its decisions.
- **DailyPlan** — Represents the plan for a specific date. It stores selected and deferred tasks, total duration, available time, and an explanation of the scheduling decisions.

The relationships between these classes reflect the system’s responsibilities: an owner has one or more pets, each pet has care tasks, and the planner uses the owner’s information to create a daily plan.

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

The scheduler currently detects conflicts when two tasks have the same preferred start time. It does not yet detect tasks whose time ranges overlap because one task lasts longer than the other. For example, a 9:00 AM task lasting 30 minutes and a 9:15 AM task would not be reported as a conflict. This is a tradeoff because exact-time matching is simpler to implement and easy to explain, while still catching the most obvious scheduling conflicts. It is reasonable for this early version because the application focuses on demonstrating task organization and prioritization; a future version could compare each task's start and end times for more precise conflict detection.

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
