\# Django Job Portal



A full-stack Job Portal web application built using Django. The platform provides separate functionality for Candidates and Recruiters, including job posting, job applications, saved jobs, profile management, and recruiter dashboards.



\## Features



\* Candidate Registration and Login

\* Recruiter Registration and Login

\* Candidate Profile Management

\* Recruiter Profile Management

\* Profile Photo Upload

\* Resume Upload

\* Job Posting

\* Edit and Delete Jobs

\* Open / Closed Job Status

\* Apply for Jobs

\* Save Jobs

\* View Saved Jobs

\* View My Applications

\* Recruiter Job Management

\* View Job Applicants

\* Update Applicant Status

\* Candidate Profile View

\* Recruiter Dashboard

\* Candidate Dashboard

\* Password Reset Functionality

\* Company Logo Upload

\* Dashboard Statistics and Charts



\## Tech Stack



\* Python

\* Django

\* HTML5

\* CSS3

\* JavaScript

\* Bootstrap

\* SQLite

\* Chart.js

\* Git

\* GitHub



\## Project Structure



```text

JobPortalProject/

├── JobPortal/

├── Jobs/

│   ├── migrations/

│   ├── static/

│   ├── templates/

│   ├── models.py

│   ├── views.py

│   └── urls.py

├── manage.py

├── requirements.txt

├── .gitignore

└── README.md

```



\## Installation



Clone the repository:



```bash

git clone https://github.com/nikhilpydev16/django-job-portal.git

```



Move into the project directory:



```bash

cd django-job-portal

```



Create a virtual environment:



```bash

python -m venv venv

```



Activate the virtual environment on Windows:



```bash

venv\\Scripts\\activate

```



Install dependencies:



```bash

pip install -r requirements.txt

```



Run database migrations:



```bash

python manage.py migrate

```



Start the development server:



```bash

python manage.py runserver

```



Open the application in your browser:



```text

http://127.0.0.1:8000/

```



\## User Roles



\### Candidate



Candidates can create accounts, manage their profiles, upload resumes, browse jobs, save jobs, apply for jobs, and track their applications.



\### Recruiter



Recruiters can create accounts, manage company profiles, post jobs, edit or delete jobs, view applicants, and update application status.



\## Future Improvements



\* Interview Scheduling System

\* Email Notifications

\* REST API Integration

\* Advanced Search and Filtering

\* Job Recommendations

\* Production Deployment

\* PostgreSQL Integration

\* Automated Testing



\## Author



\*\*Nikhil Jadhav\*\*



GitHub: \[nikhilpydev16](https://github.com/nikhilpydev16)





\## Project Screenshots



\### Home Page

!\[Home Page](screenshots/home.png)



\### Job Listings

!\[Job Listings](screenshots/jobs.png)



\### Login Page

!\[Login Page](screenshots/login.png)

