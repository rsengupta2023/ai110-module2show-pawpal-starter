import streamlit as st

from pawpal_system import Owner, OwnerPreferences, Pet, Scheduler, Task

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

if "owner" not in st.session_state:
    st.session_state.owner = Owner(
        name="Jordan",
        preferences=OwnerPreferences(available_time=60),
    )

st.markdown(
    """
Welcome to the PawPal+ starter app.

This file is intentionally thin. It gives you a working Streamlit app so you can start quickly,
but **it does not implement the project logic**. Your job is to design the system and build it.

Use this app as your interactive demo once your backend classes/functions exist.
"""
)

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.

You will design and implement the scheduling logic and connect it to this Streamlit UI.
"""
    )

with st.expander("What you need to build", expanded=True):
    st.markdown(
        """
At minimum, your system should:
- Represent pet care tasks (what needs to happen, how long it takes, priority)
- Represent the pet and the owner (basic info and preferences)
- Build a plan/schedule for a day that chooses and orders tasks based on constraints
- Explain the plan (why each task was chosen and when it happens)
"""
    )

st.divider()

st.subheader("Owner and Pets")
owner_name = st.text_input("Owner name", value="Jordan")
st.session_state.owner.name = owner_name

with st.form("add_pet_form"):
    new_pet_name = st.text_input("Pet name", value="Mochi")
    new_species = st.selectbox("Species", ["dog", "cat", "other"])
    new_age = st.number_input("Age", min_value=0, max_value=100, value=1)
    add_pet_submitted = st.form_submit_button("Add pet")

if add_pet_submitted:
    if any(pet.name == new_pet_name for pet in st.session_state.owner.pets):
        st.warning("A pet with that name already exists.")
    else:
        st.session_state.owner.add_pet(
            Pet(
                name=new_pet_name,
                species=new_species,
                age=int(new_age),
            )
        )
        st.success(f"Added {new_pet_name} to {st.session_state.owner.name}'s pets.")

if st.session_state.owner.pets:
    pet_name = st.selectbox(
        "Pet to manage",
        [pet.name for pet in st.session_state.owner.pets],
    )
    pet = next(
        pet for pet in st.session_state.owner.pets if pet.name == pet_name
    )
else:
    pet = None
    st.info("Add a pet before creating care tasks.")

st.markdown("### Tasks")
st.caption("Add tasks to the selected pet. They persist in the Owner object.")

if pet is not None:
    col1, col2, col3 = st.columns(3)
    with col1:
        task_title = st.text_input("Task title", value="Morning walk")
    with col2:
        duration = st.number_input(
            "Duration (minutes)",
            min_value=1,
            max_value=240,
            value=20,
        )
    with col3:
        priority = st.selectbox("Priority", ["low", "medium", "high"], index=2)

    if st.button("Add task"):
        pet.add_task(
            Task(
                name=task_title,
                category="care",
                description=task_title,
                duration=int(duration),
                priority=priority,
                frequency="daily",
                deadline="",
                preferred_time="",
            )
        )
        st.success(f"Added {task_title} for {pet.name}.")

all_tasks = st.session_state.owner.get_all_tasks()
if all_tasks:
    st.write("Current tasks:")
    st.table(
        [
            {
                "Pet": task_pet.name,
                "Task": task.name,
                "Duration (minutes)": task.duration,
                "Priority": task.priority,
                "Completed": task.completed,
            }
            for task_pet in st.session_state.owner.pets
            for task in task_pet.get_tasks()
        ]
    )
else:
    st.info("No tasks yet. Add one above.")

st.divider()

st.subheader("Build Schedule")
st.caption("Generate a schedule from the tasks stored in the Owner object.")

if st.button("Generate schedule"):
    scheduler = Scheduler(owner=st.session_state.owner)
    plan = scheduler.build_daily_plan()
    if plan.selected_tasks:
        st.write("Today's Schedule")
        st.table(
            [
                {
                    "Task": task.name,
                    "Duration (minutes)": task.duration,
                    "Priority": task.priority,
                }
                for task in plan.selected_tasks
            ]
        )
    else:
        st.info("No tasks fit the available schedule.")
