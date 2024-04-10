### Django Commands Reference

Here's a concise explanation of essential Django commands:

- **`py manage.py makemigrations`**
  *Purpose*: Examines the current state of the models and detects any changes (such as new fields or modified relationships). Generates migration files to capture these changes.
  
- **`py manage.py migrate`**
  *Purpose*: Applies the generated migration files to the database, synchronizing the database schema with the current state of the models.

- **`py manage.py createsuperuser`**
  *Purpose*: Prompts you to create a new superuser account, granting administrative access to the Django project's admin interface..

- **`py manage.py runserver`**
  *Purpose*: Starts the Django development server, allowing you to preview your project locally by serving it at `localhost:8000`.

- **`py manage.py startapp [appname]`**
  *Purpose*: Creates a new Django app within the project structure, encapsulating related functionality, models, views, and templates.

- **`py manage.py startproject [projname]`**
  *Purpose*: Initiates a new Django project, creating the necessary files and directories to begin building a web application.

- **`py manage.py sqlmigrate [appname] [migration number]`**
  *Purpose*: Displays the SQL code that corresponds to a specific migration (identified by the app name and migration number), aiding in understanding database changes and debugging.

  #### Shell Commands:

- **`python manage.py shell`**
  *Purpose*: Launches the Django shell, providing an interactive Python environment with access to your Django project's models and database objects.

- **`python manage.py dbshell`**
  *Purpose*: Opens a connection to the database shell, allowing you to execute SQL commands directly against the database.
