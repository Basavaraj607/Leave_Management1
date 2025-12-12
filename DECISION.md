    # DECISIONS.md – Leave Management System

## 1. Technology Choices

### Django
I chose Django because I already have internship experience building projects with it. Django provides:
- Built-in authentication
- Admin panel for quick testing
- Powerful ORM
- Faster development for backend-heavy systems

### SQLlite
I selected SQLlite because:
- It is reliable for production
- Render provides managed SQLlite hosting
- And it is built in
- Supports relational models needed for approvals and workflow

### Frontend (HTML, CSS, Bootstrap)
Simple, lightweight, and quick to build.
My focus was backend workflow, not UI-heavy features.

### Deployment: Render
Render allows:
- Free hosting
- Automatic deployment from GitHub
- Managed database support

---

## 2. Implementation Decisions

### Database Schema
I designed the schema with three key entities:
- **User** (custom user model)
- **LeaveApplication**
- **Manager actions**

Fields include leave type, dates, reason, status, and comments.

### Assumptions
- Users belong to a simple hierarchy: Employee → Manager
- No automated leave balance calculation required
- No email notification system needed for this version

### Prioritized Features
- Smooth workflow for applying and approving leave
- Clean dashboard for employees and managers
- Simple user authentication

---

## 3. Challenges

### 1. Deployment Issues
I faced multiple Render errors:
- Static files not configured
- ALLOWED_HOSTS error
- Database URL not loading from .env
- PostgreSQL authentication failures

I solved them by updating:
- STATIC_ROOT, STATICFILES_DIRS, Whitenoise
- Correct ALLOWED_HOSTS
- Correct .env variable loading

### 2. Database Migrations
Solved by resetting migrations and aligning database URL correctly.

---

## 4. Improvements with More Time
- Add leave balance tracking
- Add email notifications
- Add calendar-based leave visualization
- Improve UI/UX

---

## 5. Trade-offs & Shortcuts
- UI kept simple due to time
- No complex leave policies
- No HR dashboards implemented
