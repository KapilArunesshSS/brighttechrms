DMRM: Recruitment Management & FFR System

DMRM is a specialized human resources and operations platform designed to digitize recruitment workflows and automate Filling Factor Ratio (FFR) tracking for industrial sites. This project transforms manual manpower ledgers into a real-time digital dashboard, optimized for high performance and reliability.

🏗️ Project Structure

Based on the DMRM repository layout:

DMRM/
├── main/                   # Primary Application Logic
│   ├── migrations/         # Database schema history
│   ├── templates/          # HTML User Interface
│   │   ├── authentication/ # Login/Signup views
│   │   ├── add_employee.html
│   │   ├── dashboard.html
│   │   ├── edit_employee.html
│   │   └── ffr.html        # Filling Factor Ratio tracking
│   ├── admin.py            # Admin portal configuration
│   ├── models.py           # Database models (Employee, FFR data)
│   ├── urls.py             # App-level routing
│   └── views.py            # Business logic & FFR calculations
├── media/                  # User-uploaded files (resumes/docs)
├── server/                 # Server-specific configurations (WSGI/ASGI)
├── static/                 # CSS, JS, and Image assets
├── staticfiles/            # Collected static files for production
├── manage.py               # Django CLI
├── requirements.txt        # Project dependencies
└── .env                    # Environment variables


🚀 Key Features

FFR Tracking: Real-time calculation and visualization of the Filling Factor Ratio to monitor manpower efficiency across sites.

Employee Management: Full CRUD (Create, Read, Update, Delete) capabilities for handling the workforce lifecycle.

Secure Authentication: Dedicated module for role-based access to sensitive HR data.

Dashboard Analytics: Centralized hub for operational summaries and manpower distribution.

🛠️ Tech Stack

Framework: Django (Python)

Styling: Tailwind CSS / HTML5

Infrastructure & Cloud (AWS):

AWS EC2: Scalable compute capacity hosting the Django application instance.

AWS RDS: Managed relational database service (PostgreSQL/MySQL) for secure and reliable data persistence.

AWS S3: Object storage used for hosting media files (resumes, documents) and static assets.

Deployment Architecture:

cPanel (Production): The primary professional environment for backend management and Python WSGI application hosting.

Vercel (Reference/Frontend): Utilized as a reference deployment for frontend components and edge-based delivery.

⚙️ Local Installation

Clone the repository:

git clone <your-repo-url>
cd DMRM


Set up virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install dependencies:

pip install -r requirements.txt


Environment Variables:
Create a .env file and add your production credentials, including AWS access keys and database host information.

Run Migrations & Start Server:

python manage.py migrate
python manage.py runserver


🌐 Deployment Configuration

cPanel & AWS (Professional Backend)

Python App: Configured via the cPanel "Setup Python App" tool, interfaced with an AWS EC2 instance for stable production uptime.

WSGI: The entry point is mapped to server/wsgi.py.

Database (RDS): The application connects to an AWS RDS instance for high availability and automated backups.

Storage (S3): All media uploads and static files are offloaded to AWS S3 buckets, ensuring persistence and fast content delivery.

Vercel (Reference Deployment)

Deployment: Integrated with GitHub for continuous staging and reference testing.

Optimization: Used to benchmark frontend performance and ensure high availability for the UI layer.
