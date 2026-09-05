# WorkSpace Platform

WorkSpace is a full-stack web platform for discovering, booking, and managing workspaces.

The project was developed as part of an internship and includes a Vue.js frontend, a Django REST Framework backend, MySQL database integration, and Docker support.

---

## Project Structure

```text
stage-project/
├── WORKSPACE_BACKEND/
├── WORKSPACE_FRONTEND/
├── WORKSPACE_DOCKER-COMPOSE/
├── .gitignore
└── README.md
Backend

The backend is built with Django and Django REST Framework.

Main features include:

JWT authentication
User registration and login
User profile management
Role-based access control
Admin dashboard APIs
Office management
Workspace search and filtering
Booking management
Reserved date management
Cash payment requests
Favorites
Reviews
Notifications
Contact messages
Analytics
Website settings management

Backend location:

WORKSPACE_BACKEND/
Frontend

The frontend is built with Vue 3.

Main technologies:

Vue 3
Vue Router
Pinia
Axios
Tailwind CSS
Lucide Icons
Chart.js
SweetAlert2
vue-sonner
vue-tel-input

Frontend location:

WORKSPACE_FRONTEND/

Main frontend features:

Responsive homepage
Browse offices
Workspace categories
Office detail pages
Booking guide
User authentication
User dashboard
Reservations management
Favorites
Notifications
Profile management
Admin dashboard
Users management
Offices management
Bookings management
Payments management
Reviews management
Contact messages management
Analytics dashboard
Website settings management
Docker

The project supports Docker and Docker Compose.

Docker configuration is located in:

WORKSPACE_DOCKER-COMPOSE/

The Docker environment includes:

Django backend
Vue frontend
MySQL database

The project uses environment variables for sensitive configuration.

Real .env files are not included in the repository.

Example environment files are provided as:

.env.example
Environment Configuration

Before running the project, create the required .env files from the provided examples.

Backend

Go to:

WORKSPACE_BACKEND/

Copy:

.env.example

to:

.env

Then update the values with your local configuration.

Docker Compose

Go to:

WORKSPACE_DOCKER-COMPOSE/

Copy:

.env.example

to:

.env

Then configure your MySQL credentials.

Run with Docker

From the Docker Compose folder:

cd WORKSPACE_DOCKER-COMPOSE

Run:

docker compose up --build

The services will be available at:

Frontend:
http://localhost:5173

Backend API:
http://localhost:8000

MySQL:
localhost:3307

To stop the containers:

docker compose down

To stop the containers and remove volumes:

docker compose down -v
Run Backend Locally

Go to the backend folder:

cd WORKSPACE_BACKEND

Create a virtual environment:

Windows
python -m venv myenv
myenv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Run migrations:

python manage.py migrate

Start the development server:

python manage.py runserver

Backend:

http://127.0.0.1:8000
Run Frontend Locally

Go to the frontend folder:

cd WORKSPACE_FRONTEND

Install dependencies:

npm install

Start the development server:

npm run dev

Frontend:

http://localhost:5173
Main API Modules

The backend is organized into several Django applications:

analytics
bookings
contact
dashboard
favorites
notifications
offices
payments
reviews
site_settings
users
Authentication

The application uses JWT authentication.

Main authentication endpoints include:

POST /api/login/
POST /api/token/refresh/

Authenticated requests use:

Authorization: Bearer <access_token>
Website Settings

Administrators can manage global website information such as:

Website name
Website URL
Contact email
Contact phone
WhatsApp number
Address
Instagram
Facebook
LinkedIn
X / Twitter

These values are used dynamically across different frontend pages such as:

Navbar
Footer
Contact page
Office detail page
Booking guide
Booking Flow

Users can:

Browse available workspaces
Select a workspace
Select booking dates
Enter contact information
Submit a cash booking request
Wait for administrator confirmation
Track the booking from the user dashboard

Reserved dates are displayed in the booking calendar to prevent conflicting bookings.

Admin Dashboard

The admin panel provides management tools for:

Dashboard statistics
Users
Offices
Bookings
Payments
Contact messages
Reviews
Notifications
Analytics
Website settings
Security

Sensitive files are excluded from Git using .gitignore.

The repository does not include:

.env
database passwords
secret keys
virtual environments
node_modules
build files

Example configuration files are included using:

.env.example
Technologies
Backend
Python
Django
Django REST Framework
JWT
MySQL
Django ORM
Frontend
Vue 3
Pinia
Vue Router
Axios
Tailwind CSS
Chart.js
Lucide Vue
SweetAlert2
vue-sonner
vue-tel-input
DevOps
Docker
Docker Compose
Git
GitHub
Git Repository Structure

This repository is a monorepo containing the complete project:

WORKSPACE_BACKEND
WORKSPACE_FRONTEND
WORKSPACE_DOCKER-COMPOSE

Backend and frontend were previously maintained separately and were later combined into a single repository for easier project management and deployment.

Author

Developed as part of a Full Stack Web Development internship project.
