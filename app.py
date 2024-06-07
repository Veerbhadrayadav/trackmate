import streamlit as st
from allPages.project_page import project_page
from allPages.task_page import task_page
from allPages.subtask_page import subtask_page
from allPages.habit_page import habit_page
from allPages.progress import progress
from allPages.todo import todo_list
from services.analytics_service import get_task_progress, get_subtask_progress, get_habit_summary, get_project_summary
from utils.helpers import show_project_details,show_task_details


st.sidebar.title("Navigation")
option = st.sidebar.selectbox("Choose an option", ["ToDo", "Project Management", "Task Management", "Subtask Management", "Habit Management", "Progress Report"],key="navigation_option")

if option == "Project Management":
    project_page(show_project_details)
elif option == "Task Management":
    task_page(show_task_details)
elif option == "Subtask Management":
    subtask_page()
elif option == "Habit Management":
    habit_page()
elif option == "Progress Report":
    progress()
elif option == "ToDo":
    todo_list()
# st.session_state