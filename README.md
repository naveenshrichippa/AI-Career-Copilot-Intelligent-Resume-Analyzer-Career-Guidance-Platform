# AI Career Copilot

This project uses Django, a local MySQL database, and the Gemini API for resume analysis.

## Windows setup

1. Install Python and MySQL Server. Make sure the MySQL service is running.
2. From this project folder, create and activate a virtual environment if needed:

   ```powershell
   py -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

3. Install dependencies:

   ```powershell
   python -m pip install -r requirements.txt
   ```

4. Create the local database (enter your MySQL root password when prompted):

   ```powershell
   mysql -u root -p -e "CREATE DATABASE ai_career_copilot CHARACTER SET utf8mb4;"
   ```

5. Copy the example environment file and edit it:

   ```powershell
   Copy-Item .env.example .env
   ```

   Set `DB_PASSWORD` to your local MySQL root password and `GEMINI_API_KEY` to your Gemini API key. Keep `.env` private.
6. Create the Django tables and start the development server:

   ```powershell
   python manage.py migrate
   python manage.py runserver
   ```

7. Open <http://127.0.0.1:8000/> and create an account.

The app can start without a Gemini key, but resume analysis requires one. The database name, user, password, host, and port can be changed in `.env`.
