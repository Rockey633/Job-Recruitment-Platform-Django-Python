# Job Portal - Django Web Application

Ek full-stack job portal jisme candidates apna profile banate hain 
aur companies job post karti hain.

## Features
- Candidate & Company registration with OTP verification
- Job listing, search, and filtering
- Job apply system with resume upload
- Company dashboard for managing job posts
- Candidate profile with salary expectations

## Tech Stack
- Backend: Django (Python)
- Frontend: HTML, CSS, Bootstrap
- Database: SQLite (development)

## Setup Instructions

1. Clone the repository
   git clone <your-repo-url>
   cd final_project

2. Virtual environment banao
   python -m venv .venv
   .venv\Scripts\activate   (Windows)

3. Dependencies install karo
   pip install -r requirements.txt

4. Database migrate karo
   python manage.py migrate

5. Server chalao
   python manage.py runserver
