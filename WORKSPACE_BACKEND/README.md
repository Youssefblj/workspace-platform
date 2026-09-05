# WorkSpace Backend

Backend API for the **WorkSpace** workspace booking platform.

Built with Django REST Framework and MySQL.

## Tech Stack

- Django
- Django REST Framework
- MySQL
- SimpleJWT
- django-filter
- django-cors-headers
- drf-spectacular
- Pillow

## Main Features

- User authentication with JWT
- User profile management
- Office management
- Workspace booking
- Payment management
- Card, PayPal and Cash payment flows
- Favorites
- Reviews
- Notifications
- Contact messages
- Admin dashboard
- Analytics
- Booking and payment status management

## Project Setup

### 1. Clone the repository

```bash
git clone https://github.com/Youssefblj/workspace-backend.git
cd workspace-backend

2. Create a virtual environment

Windows:

python -m venv myenv
myenv\Scripts\activate

Linux / macOS:

python3 -m venv myenv
source myenv/bin/activate
3. Install dependencies
pip install -r requirements.txt
4. Create the environment file

Create a .env file in the project root, next to manage.py.

You can use .env.example as a reference.

Example:

DJANGO_SECRET_KEY=your-secret-key
DJANGO_DEBUG=True


DB_NAME=office_rental_db
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=127.0.0.1
DB_PORT=3306


CORS_ALLOWED_ORIGIN=http://localhost:5173

Do not commit the real .env file.

Database

This project uses MySQL.

Create the database before running migrations:

CREATE DATABASE office_rental_db;

Then make sure the credentials in .env match your MySQL configuration.

Run Migrations
python manage.py migrate
Create an Admin Account
python manage.py createsuperuser
Run the Development Server
python manage.py runserver

Backend API:

http://127.0.0.1:8000/
API Base URL
http://127.0.0.1:8000/api/
Authentication

The project uses JWT authentication.

Login:

POST /api/login/

Refresh token:

POST /api/token/refresh/

Authenticated requests should use:

Authorization: Bearer <access_token>
Media Files

Uploaded office images are stored in the local media/ directory during development.

The media/ directory is ignored by Git.

Email

During development, Django uses the console email backend.

Emails are displayed in the terminal instead of being sent to real email addresses.

Notes
.env is ignored by Git.
.env.example contains the required environment variable names.
The project currently uses Django development settings.
Production deployment requires secure environment variables, production database configuration, static/media configuration, and DEBUG=False.
