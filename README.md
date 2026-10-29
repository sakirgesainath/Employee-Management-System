# 👨‍💼 Employee Management System

A web-based **Employee Management System** developed using Python, Django, MySQL, HTML, and CSS. This project allows users to manage employee information efficiently through a simple web interface.

## 📌 Project Overview

The Employee Management System is a Django web application designed to store, view, update, and delete employee records. It provides a centralized way to manage employee details, including salary, designation, company name, address, role, age, and date of birth.

## ✨ Features

- **Add Employee:** Register new employees with their personal and professional details.
- **View Employees:** Display all employee records in a table.
- **Update Employee:** Edit existing employee information.
- **Delete Employee:** Remove employee records after confirmation.
- **Form Validation:** Validate submitted information using Django ModelForms.
- **MySQL Database:** Store employee records persistently.
- **Dynamic Templates:** Display employee information using Django templates.
- **Simple User Interface:** Navigate between employee management pages.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Django | Web application framework |
| MySQL | Database management |
| HTML5 | Web page structure |
| CSS3 | Page styling |
| Django ModelForms | Form handling and validation |
| Git and GitHub | Version control and project hosting |

## 📂 Project Structure

```text
employee/
│
├── empapp/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
├── employee/
│   ├── templates/
│   │   ├── home.html
│   │   ├── emp_form.html
│   │   ├── views_emp.html
│   │   ├── upadate.html
│   │   ├── delete.html
│   │   └── sucess.html
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── manage.py
└── README.md
```

## 👥 Employee Information

The application stores the following employee details:

| Field | Description |
|---|---|
| ID | Automatically generated employee record ID |
| Name | Employee's name |
| Salary | Employee's salary |
| Designation | Employee's job title |
| Company Name | Name of the company |
| Address | Employee's address |
| Role | Employee's role |
| Age | Employee's age |
| Date of Birth | Employee's date of birth |

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone <your-github-repository-url>
```

### 2. Navigate to the Project Directory

```bash
cd employee
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the virtual environment in Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install Dependencies

```bash
python -m pip install Django mysqlclient
```

Make sure MySQL Server is installed and running.

### 5. Configure the Database

Open `employee/settings.py` and configure the database credentials according to your MySQL setup.

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'userdb',
        'USER': 'root',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

Create the database in MySQL if it does not already exist:

```sql
CREATE DATABASE userdb;
```

Replace `your_mysql_password` with your MySQL password.

### 6. Apply Migrations

Run the following commands in the terminal:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Start the Development Server

```bash
python manage.py runserver
```

### 8. Open the Application

Open your browser and visit:

```text
http://127.0.0.1:8000/home/
```

## 🔗 Application URLs

| URL | Function |
|---|---|
| `/home/` | Home page |
| `/add/` | Add a new employee |
| `/getall/` | View all employees |
| `/update/<id>/` | Update an employee |
| `/delete/<id>/` | Delete an employee |

## 🗄️ Database Model

The project contains a `Users` model in `empapp/models.py`.

The model stores employee information using Django model fields, including:

- `name` — Character field
- `Salary` — Floating-point field
- `designation` — Character field
- `company_name` — Character field
- `address` — Character field
- `role` — Character field
- `age` — Integer field
- `dob` — Date field

Django uses this model to create and manage the corresponding database table.

## 🔄 CRUD Operations

- **Create:** Add a new employee using a Django ModelForm.
- **Read:** Retrieve employee records from the database and display them.
- **Update:** Load an existing employee record and save the edited details.
- **Delete:** Remove the selected employee record after confirmation.

## 🚀 Future Enhancements

- Employee search and filtering
- Pagination for employee records
- Employee profile images
- Login and role-based access control
- Salary reports and analytics
- Export employee records to Excel or PDF
- Improved responsive design
- Automated unit and integration tests

## 👨‍💻 Author

**Your Name**

GitHub: [Your GitHub Profile](https://github.com/)

LinkedIn: [Your LinkedIn Profile](https://www.linkedin.com/)

## 📄 License

This project is intended for educational and demonstration purposes. Add an appropriate open-source license if you plan to distribute the project publicly.
