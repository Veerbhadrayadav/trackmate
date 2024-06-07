import streamlit as st
from services.data_service import load_projects,load_tasks,load_subtasks,load_habits
import pandas as pd


def get_projects_progress(projects):
    tasks = load_tasks()
    sub_tasks = load_subtasks()
    overall_progress = []
    for project in projects:
        project_tasks = [t for t in tasks if t['project_id']==project['project_id']]
        project_progress = 0
        for task in project_tasks:
            all_subtask = [s for s in sub_tasks if s['task_id']==task['task_id']]
            if all_subtask is not None:
                completed = [s for s in all_subtask if s['done']==True]
                progress = (len(completed)/len(all_subtask))
            progress = 1 if task['done'] == True else 0
            project_progress +=progress
        if len(project_tasks):
            project_progress /=len(project_tasks)
        overall_progress.append(project_progress)
    return overall_progress


def projects_df():
    projects = load_projects()
    df = pd.DataFrame(columns=['Project','Start','Target','Progress'])
    if projects is not None:
        df['Project'] = [p['project_name'] for p in projects]
        df['Start'] = [p['start_date'] for p in projects]
        df['Target'] = [p['target_date'] for p in projects]
        df['Progress'] = get_projects_progress(projects)
    return df


def progress():
    st.title("Progress Report")
    
    col1, col2 = st.columns([2,3])
    with col1:
        st.write("## Projects")
        st.dataframe(
            projects_df(),
            hide_index=True,
            use_container_width=True
        )
    with col2:
        st.write("## Habits")
        st.dataframe(
            pd.DataFrame(load_habits()),
            hide_index=True,
            use_container_width=True
        )
    
    st.write("## Tasks")
    st.dataframe(
        pd.DataFrame(load_tasks()),
        hide_index=True,
        use_container_width=True
    )
    st.write("## SubTasks")
    st.dataframe(
        pd.DataFrame(load_subtasks()),
        hide_index=True,
        use_container_width=True
    )