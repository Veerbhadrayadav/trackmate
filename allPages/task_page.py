# Example integration in task_page.py
import streamlit as st
from components.subtask_form import subtask_form
from services.data_service import load_tasks, save_tasks, load_subtasks, load_projects
from utils.helpers import generate_id
from datetime import datetime, timedelta


def navigate_to_project_page():
    st.session_state.navigation_option = "Project Management"

def is_task_id_available(tasks, project_id):
    all_tasks_ids = [t['task_id'] for t in tasks if t['project_id']==project_id]
    task_id = generate_id()
    if all_tasks_ids is None:
        return True, task_id 
    if task_id not in all_tasks_ids:
        return True, task_id
    return False, None

def task_page(show_task_details):
    st.title("Task Management")
    
    projects = load_projects()
    if projects:
        selected_project_name = st.selectbox("Select Project",[p['project_name'] for p in projects])
        tasks = load_tasks()
        selected_project = [p for p in projects if p['project_name']==selected_project_name][0]
        selected_project_id = selected_project['project_id']
        # Form for creating a new task
        with st.form(key='task_form'):
            task_name = st.text_input("Task Name")
            description = st.text_area("Description")
            due_date = st.date_input("Due Date",min_value=datetime.today()+timedelta(1),max_value=datetime.strptime(selected_project['target_date'],"%Y-%m-%d"))
            priority = st.selectbox("Priority", ["Low", "Medium", "High"])
            submit = st.form_submit_button("Add Task")
            
            if submit:
                is_available = False
                while is_available == False:
                    is_available, task_id = is_task_id_available(tasks,selected_project_id)
                new_task = {
                    "task_id": task_id,
                    "project_id": selected_project_id,
                    "task_name": task_name,
                    "description": description,
                    "due_date": due_date.strftime('%Y-%m-%d'),
                    "start_date": datetime.today().strftime('%Y-%m-%d'),
                    "priority": priority,
                    "done": False
                }
                tasks.append(new_task)
                save_tasks(tasks)
                st.success("Task added successfully")
        
        # Display tasks
        st.subheader("Existing Tasks")
        for project in projects:
            st.write(f"#### {project['project_name']}")
            project_tasks = [t for t in tasks if t['project_id']==project['project_id']]
            color_mapping = {
                "High": "#0e1117",
                "Medium": "#f5f5f5",
                "Low": "light green"
            }
            for pt in project_tasks:
                with st.expander(label=f"### {pt['task_name']}",expanded=False):
                    st.markdown(f"""
                        <style>
                        .streamlit-expanderHeader {{
                            background-color: {color_mapping[pt['priority']]};
                            color: white;
                        }}
                        </style>
                        """, unsafe_allow_html=True)
                    show_task_details(pt)
    else:
        st.write("First add a project to add task")
        st.button("Go to add project", on_click=navigate_to_project_page)