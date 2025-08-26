# Api-driven-mini-web-app
A full stack project allows users to enter a city name as a keyword, fetches real-time weather data from the OpenWeather API, 
stores the results in PostgreSQL database and display the details on dashboard .

# Features :
1. Search weather by city name
2. Fetch live weather data from OpenWeather API
3. stores weather details in PostgreSQL
4. view all stored city weather data in a dashboard either in tabular form or api format or JSON format

# Tech Stack :
Backend : Python, Django
Database : PostgreSQL
Frontend : HTML, CSS, JavaScript
API : OpenWeather API

# Demo :
Github Repo : https://github.com/veenamadhuric12/Api-driven-mini-web-app

# Setup Instructions :
1. Create and activate virtual environment :
     python -m venv project1
     project1\scripts\activate
2. Installing dependencies :
     pip install django djangorestframework psycopg2-binary requests
3. Creating Django project and app :
     django-admin startproject project_api
     python manage.py startapp app
4. Setup PostgreSQL database :
     create PostgreSQL database
     update settings.py with DB credentials
5. Apply migrations and run the server :
     python manage.py makemigrations
     python manage.py migrate
     python manage.py runserver
6. Open the app at http://127.0.0.1:8000


<img width="1001" height="844" alt="Screenshot 2025-08-26 164423" src="https://github.com/user-attachments/assets/3cb2eff9-4cb1-445f-a27a-314a27a1cfc7" />

<img width="1044" height="720" alt="Screenshot 2025-08-26 164454" src="https://github.com/user-attachments/assets/70f67823-7fd2-4ee1-9906-fb58d17acb47" />

<img width="1700" height="923" alt="Screenshot 2025-08-26 164542" src="https://github.com/user-attachments/assets/fb64add2-ad51-4e25-bd0a-cefeb70443d3" />

<img width="643" height="866" alt="Screenshot 2025-08-26 164651" src="https://github.com/user-attachments/assets/15a1b053-d5f7-4953-a45e-4322446fa401" />

<img width="1873" height="993" alt="Screenshot 2025-08-26 164758" src="https://github.com/user-attachments/assets/8d6a54a5-1b89-4d44-9945-312bc979b166" />
