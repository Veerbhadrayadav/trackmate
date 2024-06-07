import streamlit as st
from services.data_service import load_todo,load_habits,load_projects,load_tasks,load_subtasks,load_activity,save_todo,save_activity
from utils.helpers import generate_id
from datetime import datetime, timedelta

def navigate_to_habit_page():
    st.session_state.navigation_option="Habit Management"

def navigate_to_subtask_page():
    st.session_state.navigation_option="Subtask Management"

def navigate_to_task_page():
    st.session_state.navigation_option="Task Management"

def navigate_to_project_page():
    st.session_state.navigation_option="Project Management"

def navigate_to_todo_page():
    st.session_state.navigation_option="ToDo"

def is_todo_id_available(todo, subtask_id):
    all_todo_ids = [t['todo_id'] for t in todo if t['subtask_id']==subtask_id]
    todo_id = generate_id()
    if all_todo_ids is None:
        return True, todo_id 
    if todo_id not in all_todo_ids:
        return True, todo_id
    return False, None

def update_todo_lists():
    for todo in st.session_state.todo:
        todo_id = todo['todo_id']
        todo['done'] = st.session_state[todo_id]
    save_todo(st.session_state.todo)

def sort_tasks(key):
    mapping = {
        "Name": "name",
        "Due Date": "due_date"
    }
    st.session_state.todo.sort(key=lambda x: x[mapping[key]])
    save_todo(st.session_state.todo)

def update_activity():
    save_activity(st.session_state.activity)

def todo_list():
    st.title("Items in the bucket...")
    
    projects = load_projects()
    if projects:
        tasks = load_tasks()
        if tasks:
            subtasks = load_subtasks()
            if subtasks:
                habits = load_habits()
                if habits:
                    col1, col2 = st.columns([3,1])
                    st.session_state.todo = load_todo()
                    st.session_state.activity = load_activity()
                    with col1:
                        with st.popover("Let's do something!!🥳🥳",use_container_width=True):
                            project_name = st.selectbox(label="Project Name",key="project",options=[p['project_name'] for p in projects])
                            project = [p for p in projects if p['project_name']==project_name][0]
                            task_name = st.selectbox(label="Task Name",key="task",options=[t['task_name'] for t in tasks if t['project_id']==project['project_id']])
                            if task_name:
                                task = [t for t in tasks if t['task_name']==task_name][0]
                                subtask_name = st.selectbox(label="Subtask Name",key="subtask",options=[s['subtask_name'] for s in subtasks if s['task_id']==task['task_id']])
                                if subtask_name:
                                    subtask = [s for s in subtasks if s['subtask_name']==subtask_name][0]
                                    title = st.text_input(label='Title',key="title")
                                    desc = st.text_area(label="Describe in one line",key="desc")
                                    category = st.selectbox(label="Category",key="category",options=[h['habit_name'] for h in habits])
                                    due_date = st.date_input("Due Date",min_value=datetime.today()+timedelta(1),max_value=datetime.strptime(subtask['due_date'],"%Y-%m-%d"))
                                    is_available = False
                                    while is_available == False:
                                        is_available, todo_id = is_todo_id_available(st.session_state.todo,subtask['subtask_id'])
                                    add = st.button('Add')
                                    if add:
                                        new_todo = {
                                            "subtask_id": subtask['subtask_id'],
                                            "todo_id": todo_id,
                                            "name": title,
                                            "description": desc,
                                            "done": False,
                                            "category": category,
                                            "due_date": due_date.strftime("%Y-%m-%d")
                                        }
                                        st.session_state.todo.append(new_todo)
                                        st.session_state[todo_id] = False
                                        save_todo(st.session_state.todo)
                                        st.success("Item added successfully")
                                else:
                                    st.write("No subtasks added! 🤦‍♀️🤦‍♀️")
                                    st.button("Let's add a subtask first",on_click=navigate_to_subtask_page)
                            else:
                                st.write("No task added! 👀")
                                st.button("Let's add a task first",on_click=navigate_to_task_page)
                        st.session_state.todo = load_todo()
                        if not st.session_state.todo:
                            st.write("Woah! No item in the bucket. 😱😱")
                        else:
                            st.write("#### Items still pending?? 😶😶")
                            pending_items = [todo for todo in st.session_state.todo if not todo["done"]]
                            if pending_items:
                                for item in pending_items:
                                    item_id = item['todo_id']
                                    st.checkbox(item['name'],key=f"{item_id}",value=item['done'],on_change=update_todo_lists)
                            else:
                                st.write("Wow, Nothing Pending bro")
                            
                            st.write("#### Completed items!! 🤩🤩")
                            completed_items = [todo for todo in st.session_state.todo if todo["done"]]
                            if completed_items:
                                for item in completed_items:
                                    item_id=item['todo_id']
                                    st.checkbox(f"~~{item['name']}~~",key=item_id,value=item['done'],on_change=update_todo_lists)
                            else:
                                st.write("Why are items still pending?????")
                    with col2:
                        with st.expander("Sort Options", expanded=False):
                            sort_key = st.radio("Sort option", options=["Name","Due Date"], on_change=lambda: sort_tasks(sort_key), label_visibility='collapsed')
                else:
                    st.write("No habits added in habit list.")
                    st.button("Let's add a habit first",on_click=navigate_to_habit_page)
            else:
                st.write("No subtasks added! 🤦‍♀️🤦‍♀️")
                st.button("Let's add a subtask first",on_click=navigate_to_subtask_page)
        else:
            st.write("No task added! 👀")
            st.button("Let's add a task first",on_click=navigate_to_task_page)
    else:
        st.write("No Projects!!! 😕😕")
        st.button("Let's add a Project first",on_click=navigate_to_project_page)    

    

