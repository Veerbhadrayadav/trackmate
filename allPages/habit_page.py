import streamlit as st
from services.data_service import load_habits, save_habits, load_projects, load_tasks, load_subtasks
from utils.helpers import generate_id
from components.habit_tracker import habit_tracker

def is_habit_id_available(habits):
    all_habits_ids = [h['habit_id'] for h in habits]
    habit_id = generate_id()
    if all_habits_ids is None:
        return True, habit_id 
    if habit_id not in all_habits_ids:
        return True, habit_id
    return False, None

def habit_page():
    st.title("Habit Management")
    
    habits = load_habits()
    
    # Form for creating a new habit
    with st.form(key='habit_form'):
        habit_name = st.text_input("Habit Name")
        description = st.text_area("Description")
        submit = st.form_submit_button("Add Habit")
        
        if submit:
            is_available = False
            while is_available == False:
                is_available, habit_id = is_habit_id_available(habits)
            new_habit = {
                "habit_id": habit_id,
                "habit_name": habit_name,
                "description": description,
            }
            habits.append(new_habit)
            save_habits(habits)
            st.success("Habit added successfully")
    
    # Display existing habits
    st.subheader("Existing Habits")
    for habit in habits:
        habit_tracker(habit['habit_name'],habit['habit_id'])
