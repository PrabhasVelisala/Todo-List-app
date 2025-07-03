### Overview of Todo List App Operations

This Django-based Todo List application allows users to manage their tasks with features such as viewing, adding, editing, and deleting tasks. Here’s a breakdown of the core functionalities implemented in the `views.py`:

- **Home Page (`home` view):**  
  Users can add new tasks by submitting a form with a task title and description. When a POST request is made, the app creates a new `Task` object with the provided data and records the current timestamp. It then confirms success and reloads the homepage.

- **List Tasks (`tasks` view):**  
  Users can view all existing tasks. The app fetches all tasks from the database and displays them on the `tasks.html` page. If no tasks exist, it prompts the user to add new tasks via the home page.

- **Delete Task (`delete` view):**  
  Users can delete specific tasks. The app ensures that only the owner of the task (if user-specific filtering is used) can delete it, then removes the task from the database and refreshes the task list.

- **Edit Task (`edit` view):**  
  When editing, the app retrieves the task by ID and populates an edit form with current task details. Upon form submission (POST request), it updates the task's title, description, and timestamp, then redirects back to the task list.

- **Update Task (`update` view):**  
  Handles the POST request from the edit form, updating the task's details and timestamp, then redirects to the task list.

- **User Authentication (`@login_required` decorators):**  
  Critical operations like viewing, editing, and deleting tasks are protected, ensuring only logged-in users can perform these actions.

