const classDiagram = `
classDiagram
    class Owner {
        +String name
        +Pet[] pets
        +OwnerPreferences preferences
        +addPet(pet)
        +removePet(pet)
    }

    class Pet {
        +String name
        +String species
        +int age
        +String breed
        +String healthNeeds
        +String petPreferences
        +CareTask[] careTasks
        +addTask(task)
        +removeTask(task)
        +updateHealthNeeds(healthNeeds)
        +getTasks()
    }

    class CareTask {
        +String name
        +String category
        +String description
        +int duration
        +String priority
        +String frequency
        +String deadline
        +String preferredTime
        +bool completed
        +markComplete()
        +markIncomplete()
        +updateDetails()
        +isDue()
        +fitsTimeAvailable(minutes)
    }

    class OwnerPreferences {
        +int availableTime
        +String preferredTaskTimes
        +String priorityPreferences
        +String excludedActivities
        +int maximumDailyTasks
        +updatePreferences()
        +isPreferredTime(task)
        +allowsTask(task)
        +getAvailableMinutes()
    }

    class DailyPlan {
        +Date date
        +CareTask[] selectedTasks
        +CareTask[] deferredTasks
        +int totalDuration
        +int availableTime
        +String explanation
        +addTask(task)
        +removeTask(task)
        +calculateTotalDuration()
        +isWithinTimeLimit()
        +generateExplanation()
        +getSummary()
    }

    class Planner {
        +Date planningDate
        +collectDueTasks(date)
        +prioritizeTasks(tasks)
        +buildDailyPlan()
        +deferTask(task)
        +explainDecision(task)
    }

    Owner "1" *-- "many" Pet : has
    Owner "1" *-- "1" OwnerPreferences : has
    Pet "1" *-- "many" CareTask : has
    Planner --> Owner : uses
    Planner "1" --> "1" DailyPlan : creates
    DailyPlan "1" o-- "many" CareTask : contains
`;

export default classDiagram;
