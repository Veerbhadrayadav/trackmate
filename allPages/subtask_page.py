import streamlit as st
from services.data_service import load_subtasks, save_subtasks, load_tasks,load_projects,load_habits
from utils.helpers import generate_id
from datetime import datetime, timedelta


def navigate_to_task_page():
    st.session_state.navigation_option = "Task Management"

def navigate_to_project_page():
    st.session_state.navigation_option = "Project Management"

def is_subtask_id_available(subtasks, task_id):
    all_subtasks_ids = [s['subtask_id'] for s in subtasks if s['task_id']==task_id]
    subtask_id = generate_id()
    if all_subtasks_ids is None:
        return True, subtask_id 
    if subtask_id not in all_subtasks_ids:
        return True, subtask_id
    return False, None

def subtask_page():
    st.title("Subtask Management")
    projects = load_projects()
    habits = load_habits()
    if projects:
        tasks = load_tasks()
        selected_project_name = st.selectbox("Which Project?", [p['project_name'] for p in projects])
        selected_project = [p for p in projects if p['project_name']==selected_project_name][0]
        selected_task_name = st.selectbox("Select Task", [t['task_name'] for t in tasks if t['project_id']==selected_project['project_id']])
        subtasks = load_subtasks()
        if selected_task_name:
            selected_task = [t for t in tasks if t['task_name']==selected_task_name][0]
            # Form for creating a new subtask
            with st.form(key='subtask_form'):
                subtask_name = st.text_input("Subtask Name")
                description = st.text_area("Description")
                due_date = st.date_input("Due Date",min_value=datetime.today()+timedelta(1),max_value=datetime.strptime(selected_task['due_date'],"%Y-%m-%d"))
                submit = st.form_submit_button("Add Subtask")
                is_available = False
                while is_available == False:
                    is_available, subtask_id = is_subtask_id_available(subtasks,selected_task['task_id'])
                if submit:
                    new_subtask = {
                        "task_id": selected_task['task_id'],
                        "subtask_id": subtask_id,
                        "subtask_name": subtask_name,
                        "description": description,
                        "done": False,
                        "due_date": due_date.strftime("%Y-%m-%d")
                    }
                    subtasks.append(new_subtask)
                    save_subtasks(subtasks)
                    st.success("Subtask added successfully")
            # Display subtasks for the selected task
            st.subheader(f"Subtasks:")
            for project in projects:
                st.write(f"#### {project['project_name']}")
                project_task = [t for t in tasks if t['project_id']==project['project_id']]
                for task in project_task:
                    subtask_list = [s for s in subtasks if s['task_id']==task['task_id']]
                    with st.expander(label=f"{task['task_name']}",expanded=False):
                        if subtask_list:
                            col1, col2 = st.columns([4,1])
                            for subtask in subtask_list:
                                if subtask['done']:
                                    label = (":green[Completed]")
                                else:
                                    label = (":red[Pending]")
                                with col1:
                                    st.write(f"**{subtask['subtask_name']}**")
                                with col2:
                                    st.write(label)
                        else:
                            st.write("No subtask added yet")
                                    
        else:
            st.write("Bro!! First add some task in this project 🫤🫤")
            st.button("Go to add task", on_click=navigate_to_task_page)
    else:
        st.write("Bro!! Don't you think first you should add a project 😑😑")
        st.button("Go to add project", on_click=navigate_to_project_page)
