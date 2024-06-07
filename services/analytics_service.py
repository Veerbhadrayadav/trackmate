import datetime
from services.data_service import load_tasks, load_subtasks, load_habits, load_data

# Utility function to calculate completion rate
def calculate_completion_rate(total, completed):
    return (completed / total) * 100 if total > 0 else 0

# Get overall progress for tasks
def get_task_progress():
    tasks = load_tasks()
    completed_tasks = [task for task in tasks if task.get('completed', False)]
    return {
        "total_tasks": len(tasks),
        "completed_tasks": len(completed_tasks),
        "completion_rate": calculate_completion_rate(len(tasks), len(completed_tasks))
    }

# Get overall progress for subtasks
def get_subtask_progress():
    subtasks = load_subtasks()
    completed_subtasks = [subtask for subtask in subtasks if subtask.get('completed', False)]
    return {
        "total_subtasks": len(subtasks),
        "completed_subtasks": len(completed_subtasks),
        "completion_rate": calculate_completion_rate(len(subtasks), len(completed_subtasks))
    }

# Get habit tracking summary
def get_habit_summary():
    habits = load_habits()
    habit_summary = {}
    
    for habit in habits:
        habit_id = habit['habit_id']
        habit_tracking = load_data(f"data/habit_tracking_{habit_id}.json")
        
        total_days = len(habit_tracking)
        completed_days = len([day for day in habit_tracking if day['status'] == 'completed'])
        
        habit_summary[habit['habit_name']] = {
            "total_days": total_days,
            "completed_days": completed_days,
            "completion_rate": calculate_completion_rate(total_days, completed_days)
        }
    
    return habit_summary

# Generate a summary report for a project
def get_project_summary(project_name):
    tasks = load_tasks()
    project_tasks = [task for task in tasks if task['project_name'] == project_name]
    completed_project_tasks = [task for task in project_tasks if task.get('completed', False)]
    
    project_subtasks = []
    for task in project_tasks:
        subtasks = load_subtasks()
        task_subtasks = [subtask for subtask in subtasks if subtask['task_name'] == task['task_name']]
        project_subtasks.extend(task_subtasks)
    
    completed_project_subtasks = [subtask for subtask in project_subtasks if subtask.get('completed', False)]
    
    return {
        "total_tasks": len(project_tasks),
        "completed_tasks": len(completed_project_tasks),
        "total_subtasks": len(project_subtasks),
        "completed_subtasks": len(completed_project_subtasks),
        "task_completion_rate": calculate_completion_rate(len(project_tasks), len(completed_project_tasks)),
        "subtask_completion_rate": calculate_completion_rate(len(project_subtasks), len(completed_project_subtasks))
    }

# Get progress over time for visual representation (e.g., for a graph)
def get_progress_over_time():
    tasks = load_tasks()
    subtasks = load_subtasks()
    
    # Dummy data representing progress over time
    # In a real application, you would calculate these values based on task/subtask completion dates
    progress_data = [
        {"date": datetime.date(2024, 1, 1), "completed_tasks": 5, "completed_subtasks": 10},
        {"date": datetime.date(2024, 2, 1), "completed_tasks": 15, "completed_subtasks": 25},
        {"date": datetime.date(2024, 3, 1), "completed_tasks": 25, "completed_subtasks": 40},
        # Add more data points as needed
    ]
    
    return progress_data
