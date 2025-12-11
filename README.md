# Leave Management System (Django)

The Leave Management System is a role-based web application built using Django.  
It allows **employees** to apply for leave and track their leave history, while **managers** can review, approve, or reject leave requests for their team.  
The project includes dashboards, leave balances, request status tracking, and a team calendar view.

---

## 📌 Project Description

This system provides a simple and efficient workflow for managing employee leave requests within an organization.  
It supports:

- Employee leave applications  
- Tracking of leave balances (Casual, Sick, Earned)  
- Manager approval workflow  
- Team calendar display (Approved, Rejected, Pending, Cancelled)  
- Role-based dashboard views for Employees and Managers  
- Admin access for full control  

Designed to be lightweight and easy to deploy, using Django and SQLite.

---

## 🧰 Technology Stack Used

| Component | Technology |
|----------|------------|
| Backend | Django |
| Frontend | HTML5, CSS3, Bootstrap 5 |
| Database | **SQLite** (default Django database) |
| Authentication | Django Auth |
| Deployment | *(Add your deployment platform, e.g., Render / Railway / PythonAnywhere)* |

---

## 🗄️ Database Setup Instructions (SQLite)

SQLite requires **no additional installation**.  
Django automatically creates the SQLite database file (`db.sqlite3`) when applying migrations.

### ✔ 1. Database configuration (default)
In `settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

}
✔ 2. Apply migrations
bash
Copy code
python manage.py migrate
✔ 3. (Optional) Reset database
bash
Copy code
rm db.sqlite3
python manage.py migrate
▶️ Step-by-Step Instructions to Run the Project Locally
1️⃣ Clone the project
bash
Copy code
git clone https://github.com/your-repo/leave-management.git
cd leave-management
2️⃣ Create a virtual environment
nginx
Copy code
python -m venv venv
3️⃣ Activate the virtual environment
Linux/Mac:

bash
Copy code
source venv/bin/activate
Windows:

Copy code
venv\Scripts\activate
4️⃣ Install required dependencies
css
Copy code
pip install -r requirements.txt
5️⃣ Run database migrations
nginx
Copy code
python manage.py migrate
6️⃣ Start the Django development server
nginx
Copy code
python manage.py runserver
✔ Access the Application
Open in browser:

cpp
Copy code
http://127.0.0.1:8000/
🌐 Deployed Application URL
🔗 https://your-deployment-url.com
(Replace with your actual deployment link.)

🔑 Test Login Credentials
👑 Admin / Manager Login
makefile
Copy code
username: basu
password: basu123
👨‍💼 Employee Login
makefile
Copy code
username: vishwa
password: basu1234
⚠ NOTE: These credentials are for testing/demo only.

⚠ Known Limitations / Issues
No email notifications for approvals/rejections

Calendar is basic (non-interactive)

No pagination for long leave history lists

Single-manager approval workflow (no multi-level approval)

SQLite is suitable for development—not recommended for large production use

No API layer (pure Django templates)

Admin and Manager use same credentials in demo environment

