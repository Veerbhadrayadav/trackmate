import streamlit as st

def subtask_form(task_options, default_data=None):
    if default_data is None:
        default_data = {
            "task_name": "",
            "subtask_name": "",
            "description": ""
        }
    
    st.subheader("Subtask Details")
    task_name = st.selectbox("Task Name", task_options, index=task_options.index(default_data["task_name"]) if default_data["task_name"] in task_options else 0)
    subtask_name = st.text_input("Subtask Name", default_data["subtask_name"])
    description = st.text_area("Description", default_data["description"])
    
    return {
        "task_name": task_name,
        "subtask_name": subtask_name,
        "description": description
    }
