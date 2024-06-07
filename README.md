## Breakdown of the Use Case

### 1. Projects
**Definition:** A project is a high-level goal or initiative, such as "IAS".
**Features:**
- Create and manage projects.
- Each project can have its own tasks and settings.
- Projects can share common habits.

### 2. Tasks
**Definition:** Tasks are specific actions or objectives within a project, such as "Learning Geography".
**Features:**
- Create and manage tasks within a project.
- Tasks can have multiple subtasks.

### 3. Subtasks
**Definition:** Subtasks are smaller, more detailed actions under a task, such as "Chapter 1", "Chapter 2", "Chapter 3".
**Features:**
- Create and manage subtasks within a task.
- Subtasks can be tracked individually.

### 4. Habits
**Definition:** Habits are recurring actions that support the completion of tasks and subtasks, such as "Watch Lecture", "Read Book", "Current Affairs".
**Features:**
- Define and track habits on a daily or regular basis.
- Habits can be linked to multiple tasks and subtasks across different projects.

## Data Structure

To organize the data, here is a conceptual schema:

### Projects Table:
- **project_id:** Unique identifier for each project
- **project_name:** Name of the project
- **description:** Detailed description of the project

### Tasks Table:
- **task_id:** Unique identifier for each task
- **project_id:** Foreign key linking to the project
- **task_name:** Name of the task
- **description:** Detailed description of the task
- **due_date:** Due date to complete the task
- **priority:** Priority of the task

### Subtasks Table:
- **subtask_id:** Unique identifier for each subtask
- **task_id:** Foreign key linking to the task
- **subtask_name:** Name of the subtask
- **description:** Detailed description of the subtask

### Habits Table:
- **habit_id:** Unique identifier for each habit
- **habit_name:** Name of the habit
- **description:** Detailed description of the habit

### Habit Tracking Table:
- **habit_tracking_id:** Unique identifier for each tracking entry
- **habit_id:** Foreign key linking to the habit
- **date:** Date of the habit tracking
- **status:** Status of the habit on that day (e.g., completed, not completed)

### Linking Table (to associate habits with tasks/subtasks):
- **link_id:** Unique identifier for each linking entry
- **habit_id:** Foreign key linking to the habit
- **task_id:** Foreign key linking to the task (can be null)
- **subtask_id:** Foreign key linking to the subtask (can be null)

## Workflow

### Project Creation:
- User creates a new project (e.g., "IAS").

### Task Management:
- Within the project, the user adds tasks (e.g., "Learning Geography").

### Subtask Management:
- Under each task, the user adds subtasks (e.g., "Chapter 1", "Chapter 2", "Chapter 3").

### Habit Definition:
- The user defines habits that support task/subtask completion (e.g., "Watch Lecture", "Read Book").
- These habits are linked to specific tasks or subtasks.

### Daily Tracking:
- Users log their progress on habits daily.
- The system tracks which habits are completed and provides visual feedback on progress.

## User Interface Design

### Main Dashboard:
- Overview of all projects.
- Quick access to tasks and progress metrics.

### Project Page:
- Details of the selected project.
- List of tasks with options to add, edit, or delete tasks.

### Task Page:
- Details of the selected task.
- List of subtasks with options to add, edit, or delete subtasks.

### Subtask Page:
- Details of the selected subtask.
- Link to associated habits.

### Habits Page:
- List of defined habits.
- Interface for logging daily habit progress.

### Tracking and Analysis Page:
- Visual representation of habit completion (e.g., streaks, graphs).
- Reports summarizing project/task/subtask progress.


```
trackmate/
│
├── app.py                 # Main entry point for the Streamlit app
├── requirements.txt       # Dependencies for the project
├── README.md              # Project documentation
│
├── data/                  # Directory for storing data files
│   ├── tasks.json         # JSON file for storing tasks (initial development)
│   ├── projects.json      # JSON file for storing projects (initial development)
│   ├── subtasks.json      # JSON file for storing subtasks (initial development)
│   └── habits.json        # JSON file for storing habits (initial development)
│
├── allPages/                 # Directory for Streamlit pages
│   ├── __init__.py        # Initialize the pages module
│   ├── project_page.py    # Page for managing projects
│   ├── task_page.py       # Page for managing tasks
│   ├── subtask_page.py    # Page for managing subtasks
│   └── habit_page.py      # Page for managing habits
│
├── components/            # Directory for reusable components
│   ├── __init__.py        # Initialize the components module
│   ├── task_form.py       # Form component for creating/editing tasks
│   ├── subtask_form.py    # Form component for creating/editing subtasks
│   ├── habit_form.py      # Form component for creating/editing habits
│   └── habit_tracker.py   # Component for tracking habits
│
├── services/              # Directory for service modules
│   ├── __init__.py        # Initialize the services module
│   ├── data_service.py    # Service for loading/saving data
│   └── analytics_service.py # Service for data analysis and reporting
│
└── utils/                 # Directory for utility functions
    ├── __init__.py        # Initialize the utils module
    └── helpers.py         # Helper functions used across the project