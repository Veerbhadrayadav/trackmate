import streamlit as st

def task_form(default_values=None):
    if default_values is None:
        default_values = {
            "task_name": "",
            "description": "",
            "due_date": "",
            "priority": "Medium"
        }
    
    st.subheader("Task Details")
    task_name = st.text_input("Task Name", default_values["task_name"])
    description = st.text_area("Description", default_values["description"])
    due_date = st.date_input("Due Date", default_values["due_date"])
    priority = st.selectbox("Priority", ["Low", "Medium", "High"], index=["Low", "Medium", "High"].index(default_values["priority"]))
    
    return {
        "task_name": task_name,
        "description": description,
        "due_date": due_date,
        "priority": priority
    }
