import json

# Paths to data files
TASKS_FILE = 'data/tasks.json'
PROJECTS_FILE = 'data/projects.json'
SUBTASKS_FILE = 'data/subtasks.json'
HABITS_FILE = 'data/habits.json'
TODO = 'data/todo.json'
ACTIVITY = 'data/activity.json'

# Load data from a JSON file
def load_data(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

# Save data to a JSON file
def save_data(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

# Specific functions for loading and saving tasks, projects, subtasks, and habits
def load_tasks():
    return load_data(TASKS_FILE)

def save_tasks(tasks):
    save_data(tasks, TASKS_FILE)

def load_projects():
    return load_data(PROJECTS_FILE)

def save_projects(projects):
    save_data(projects, PROJECTS_FILE)

def load_subtasks():
    return load_data(SUBTASKS_FILE)

def save_subtasks(subtasks):
    save_data(subtasks, SUBTASKS_FILE)

def load_habits():
    return load_data(HABITS_FILE)

def save_habits(habits):
    save_data(habits, HABITS_FILE)

def load_todo():
    return load_data(TODO)

def save_todo(todo):
    save_data(todo,TODO)

def load_activity():
    return load_data(ACTIVITY)

def save_activity(activity):
    save_data(activity,ACTIVITY)
