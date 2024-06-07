import random
import string
import streamlit as st
from services.data_service import load_tasks,load_subtasks
import pandas as pd
from datetime import datetime
def generate_id():
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for i in range(8))

def toggle_show_project():
    st.session_state.show_project=False

def show_project_details(project):
    col1, col2 = st.columns([3.5,1.5])
    with col1:
        st.write(f"##### {project['description']}")
        # st.progress()
    with col2:
        st.write(f"**Start**: {project['start_date']}")
        st.write(f"**Target**: {project['target_date']}")
        total_days = (datetime.strptime(project['target_date'],"%Y-%m-%d")-datetime.strptime(project['start_date'],"%Y-%m-%d")).days
        days_passed = (datetime.today()-datetime.strptime(project['start_date'],"%Y-%m-%d")).days
        st.progress(days_passed/total_days, "Days Elapsed")

    tasks = load_tasks()
    st.write("Tasks")
    project_tasks = [t for t in tasks if t['project_id']==project['project_id']]
    st.dataframe(pd.DataFrame(project_tasks),hide_index=True)
    st.write("**Activity**")
    # activity_df = pd.DataFrame(project['activity'])
    # if len(activity_df) == 0:
    #     st.write("No activity recorded yet!")
    # else:
    #     st.bar_chart(activity_df,
    #                   x='date',
    #                   y='progress',)
        
def show_task_details(task):
    col1, col2 = st.columns([3.5,1.5])
    with col1:
        st.write(f"##### {task['description']}")
        # st.progress()
    with col2:
        st.write(f"**Start**: {task['start_date']}")
        st.write(f"**Target**: {task['due_date']}")
        total_days = (datetime.strptime(task['due_date'],"%Y-%m-%d")-datetime.strptime(task['start_date'],"%Y-%m-%d")).days
        days_passed = (datetime.today()-datetime.strptime(task['start_date'],"%Y-%m-%d")).days
        st.progress(days_passed/total_days, "Days Elapsed")

    subtasks = load_subtasks()
    st.write("Tasks")
    subtasks = [t for t in subtasks if t['project_id']==task['project_id']]
    st.dataframe(pd.DataFrame(subtasks),hide_index=True)
    st.write("**Activity**")
    # activity_df = pd.DataFrame(task['activity'])
    # if len(activity_df) == 0:
    #     st.write("No activity recorded yet!")
    # else:
    #     st.bar_chart(activity_df,
    #                   x='date',
    #                   y='progress',)
