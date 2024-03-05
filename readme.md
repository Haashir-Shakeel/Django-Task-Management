# Task Management application


## Tools

- Python
- Django
- SQLite

## How to Run the Application

Follow these steps to get your development env running.

### Pre-requisites

Before starting, ensure you have the following installed:
1. Python
2. pip

### Installation

First, clone the repository to your local machine:

```bash
git clone <https://github.com/Haashir-Shakeel/Django-Task-Management.git>

cd <project-directory>

pip install -r requirements.txt

python manage.py migrate
# or, if you have multiple versions of Python installed:
python3 manage.py migrate

python manage.py createsuperuser
# or, if you have multiple versions of Python installed:
python3 manage.py createsuperuser

python manage.py runserver
# or, if you have multiple versions of Python installed:
python3 manage.py runserver


