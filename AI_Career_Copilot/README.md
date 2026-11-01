# AI Career Copilot

This project uses Django, a local MySQL database, and the Gemini API for resume analysis.

## Windows setup

1. Install Python 3.10 or later and MySQL Server. Make sure the MySQL service is running.
2. From this project folder, create and activate a virtual environment if needed:

   ```powershell
   py -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

3. Install dependencies:

   ```powershell
   python -m pip install -r requirements.txt
   ```

4. Create the local database. Run this SQL in MySQL Workbench:

   ```sql
   CREATE DATABASE ai_career_copilot CHARACTER SET utf8mb4;
   ```

   Alternatively, from PowerShell with the MySQL command-line client installed:

   ```powershell
   mysql -u root -p -e "CREATE DATABASE ai_career_copilot CHARACTER SET utf8mb4;"
   ```

5. Copy the example environment file and edit `.env` with your local MySQL settings and Gemini API key:

   ```powershell
   Copy-Item .env.example .env
   ```

   Set `DB_PASSWORD` to your local MySQL password and `GEMINI_API_KEY` to your Gemini API key. Never commit `.env`; `.gitignore` excludes it.
6. Create the Django tables and start the development server:

   ```powershell
   python manage.py migrate
   python manage.py runserver
   ```

7. Open <http://127.0.0.1:8000/> and create an account.

The app can start without a Gemini key, but resume analysis requires one. The database name, user, password, host, and port can be changed in `.env`.

## Project layout

- `manage.py`, `career_copilot/`: Django project configuration and entry point.
- `analyzer/`: Django app, models, views, forms, routes, and database migrations.
- `templates/`, `static/`: HTML templates and CSS.
- `ai.py`: Gemini resume-analysis integration.
- `requirements.txt`: Python dependencies.
- `.env.example`: Safe template for local configuration; copy it to `.env`.
