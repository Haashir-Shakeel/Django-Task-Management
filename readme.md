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

## Installation

### clone the repository to your local machine:

```
git clone https://github.com/Haashir-Shakeel/Django-Task-Management.git
```

### Navigate to the project directory:
```
cd Django-Task-Management
```
### Install the required Python packages
```
pip install -r requirements.txt
```

### db setup
```
python manage.py migrate
```
or, if you have multiple versions of Python installed:
```
python3 manage.py migrate
```

### create super user
```
python manage.py createsuperuser
```
or, if you have multiple versions of Python installed:
```
python3 manage.py createsuperuser
```
### Running the application
```
python manage.py runserver
```
or, if you have multiple versions of Python installed:
```
python3 manage.py runserver
```


