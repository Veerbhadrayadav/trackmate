import streamlit as st
import logging
from services.data_service import load_projects, save_projects,load_tasks
from utils.helpers import generate_id
from datetime import datetime,timedelta

def is_project_id_available(projects):
    all_project_ids = [p['project_id'] for p in projects]
    project_id = generate_id()
    if all_project_ids is None:
        return True, project_id 
    if project_id not in all_project_ids:
        return True, project_id
    return False, None





def project_page(show_project_details):
    st.title("Project Management")
    projects = load_projects()

    # Form for creating a new project
    with st.form(key='project_form'):
        project_name = st.text_input("Project Name")
        description = st.text_area("Description")
        target_date = st.date_input("Target Date", min_value=datetime.today()+timedelta(1))
        submit = st.form_submit_button("Add Project")
        
        if submit:
            if project_name in [p['project_name'] for p in projects] and submit == True:
                raise ValueError("Project name already exists")
            is_available = False
            while is_available == False:
                is_available, project_id = is_project_id_available(projects)
            new_project = {
                "project_id": project_id,
                "project_name": project_name,
                "description": description,
                "start_date": datetime.today().strftime("%Y-%m-%d"),
                "target_date": target_date.strftime("%Y-%m-%d"),
            }
            projects.append(new_project)
            save_projects(projects)
            st.success("Project added successfully")
    
    # Display existing projects
    st.subheader("Existing Projects")
    
    for project in projects:
        with st.expander(label=f"### {project['project_name']}"):
            show_project_details(project)
