Leave Management System (Django)

The Leave Management System is a role-based web application built using Django.
It allows employees to apply for leave and track their leave history, while managers
can review, approve, or reject leave requests for their team. The system includes
dashboards, leave balances, request status tracking, and a team calendar view.

----------------------------------------------------------------------
PROJECT DESCRIPTION
----------------------------------------------------------------------

This system provides a simple and efficient workflow for managing employee
leave requests within an organization. It supports:

- Employee leave applications
- Tracking of leave balances (Casual, Sick, Earned)
- Manager approval workflow
- Team calendar display (Approved, Rejected, Pending, Cancelled)
- Role-based dashboard views for Employees and Managers
- Admin access for full control

Designed to be lightweight and easy to deploy, using Django and SQLite.

----------------------------------------------------------------------
TECHNOLOGY STACK USED
----------------------------------------------------------------------

Backend: Django  
Frontend: HTML5, CSS3, Bootstrap 5  
Database: SQLite (default Django database)  
Authentication: Django Auth  
Deployment: Render 

----------------------------------------------------------------------
DATABASE SETUP INSTRUCTIONS (SQLite)
----------------------------------------------------------------------

SQLite requires no installation. Django automatically creates the database file
(db.sqlite3) when migrations are applied.

1. Default database configuration (settings.py):

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

2. Apply migrations:

python manage.py migrate

3. (Optional) Reset the database:

rm db.sqlite3
python manage.py migrate

----------------------------------------------------------------------
STEP-BY-STEP INSTRUCTIONS TO RUN THE PROJECT LOCALLY
----------------------------------------------------------------------

1. Clone the project:

git clone https://github.com/Basavaraj607/Leave_Management1.git

cd leave-management

2. Create a virtual environment:

python -m venv venv

3. Activate the virtual environment:

Linux/Mac:
source venv/bin/activate

Windows:
venv\Scripts\activate

4. Install dependencies:

pip install -r requirements.txt

5. Run migrations:

python manage.py migrate

6. Start the Django development server:

python manage.py runserver

Access the application at:
http://127.0.0.1:8000/

----------------------------------------------------------------------
DEPLOYED APPLICATION URL
----------------------------------------------------------------------

https://leave-management1.onrender.com

----------------------------------------------------------------------
DEMO VIDEO URL
----------------------------------------------------------------------
https://www.loom.com/share/3ac6660e1f994f84a8811817b8b69687



----------------------------------------------------------------------
TEST LOGIN CREDENTIALS
----------------------------------------------------------------------

ADMIN / MANAGER LOGIN:
username: basu
password: basu123

EMPLOYEE LOGIN:
username: vishwa
password: basu1234

Note: These credentials are for demo/testing only.

----------------------------------------------------------------------
KNOWN LIMITATIONS / ISSUES
----------------------------------------------------------------------

- No email notifications implemented for approval/rejection events
- Team calendar is simple (non-interactive)
- No pagination for large leave history tables
- Single-level manager approval workflow only
- SQLite suitable for development only, not recommended for large-scale production
- No REST API layer (Django templates only)
- Admin and Manager share the same credentials in demo mode

----------------------------------------------------------------------
ADDITIONAL DOCUMENTATION
----------------------------------------------------------------------

See DECISIONS.txt for:
- Technology choices
- Database design decisions
- Assumptions made
- Feature priorities
- Challenges and solutions
- Trade-offs
