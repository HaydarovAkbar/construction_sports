# construction_sports
this project is the backend part of the web project made for the construction department under the ministry of youth policy and sports development!


# Project goal
Users registered through the my.sport.uz desk can use and residents of each district have the right to vote on the construction of construction objects.
and a web project that can retrieve data such as the value of a list of objects built so far, the number of votes, and the number of votes for each object.

# Project structure
The project consists of 3 parts: the backend, the frontend, and the telegram bot.

# Backend
The backend is written in Python using the Django framework. The backend is responsible for the fol
    lowing tasks:
    - User registration and authentication
    - User voting
    - Retrieving data from the database
    - Sending data to the frontend
    - Sending data to the telegram bot
    - Axes with security

# Frontend
The frontend is written in JavaScript using the React framework. The frontend is responsible for the following tasks:
    - User registration and authentication
    - User voting
    - Retrieving data from the backend
    - Displaying data to the user


# Telegram bot
The telegram bot is written in Python using the python-telegram-bot library. The telegram bot is responsible for the following tasks:
    - Retrieving data from the backend
    - Sending data to the backend
    - Sending data to the user


# Installation
To install the project, you need to install the following programs:
    - Python 3.8
    - Node.js 14.15.4
    - PostgreSQL 13.1
    - Redis 6.0.9
    - RabbitMQ 3.8.9
    - Nginx 1.18.0

# Backend installation
To install the backend, you need to do the following:
    - Create a virtual environment
    - Install the required packages
    - Create a database
    - Create a .env file
    - Run the backend


# Virtual environment creation

To create a virtual environment, you need to run the following command in the terminal:
```
python3 -m venv venv
```

# Installing the required packages

To install the required packages, you need to run the following command in the terminal:
```
pip install -r requirements.txt
```

# Creating a database

To create a database, you need to run the following commands in the terminal:
```
sudo -u postgres psql
CREATE DATABASE construction_sports;
CREATE USER construction_sports WITH PASSWORD 'construction_sports';
GRANT ALL PRIVILEGES ON DATABASE construction_sports TO construction_sports;
```

# Creating a .env file
    
To create a .env file, you need to run the following command in the terminal:
```
touch .env
```

# Running the backend

To run the backend, you need to run the following command in the terminal:
```

python manage.py runserver
```

# Frontend installation

To install the frontend, you need to do the following:
    - Install the required packages
    - Run the frontend

# Installing the required packages

To install the required packages, you need to run the following command in the terminal:
```

npm install
```

# Running the frontend

To run the frontend, you need to run the following command in the terminal:
```

npm start
```

# Telegram bot installation

Change the bot token in the .env file

.../src/.env.txt