# 🏢 WorkSpace Frontend


Frontend application for the **WorkSpace** workspace booking platform.


Built with **Vue 3** and **Vite**, with support for workspace browsing, bookings, payments, dashboards, notifications, and administration.


---


## 🚀 Tech Stack


- **Vue 3**
- **Vite**
- **Vue Router**
- **Pinia**
- **Axios**
- **Tailwind CSS**
- **Lucide Vue**
- **Chart.js**
- **Vee Validate**
- **Yup**
- **Vue Sonner**


---


## ✨ Main Features


### 👤 User Features


- User authentication
- Office browsing
- Workspace details
- Workspace booking
- Favorites
- User dashboard
- Reservations
- Billing and invoices
- Notifications
- User profile
- Account settings


### 💳 Payments


- Card payments
- PayPal payments
- Cash payment flow


### 🛠️ Admin Features


- Admin dashboard
- User management
- Office management
- Booking management
- Payment management
- Reviews
- Messages
- Notifications
- Analytics


---


# ⚙️ Project Setup


## 1. Clone the Repository


```bash
git clone https://github.com/Youssefblj/workspace-frontend.git
cd workspace-frontend
2. Install Dependencies
npm install
🔐 Environment Variables

Create a .env file in the project root if environment variables are required.

Example:

VITE_API_BASE_URL=http://127.0.0.1:8000/api/
VITE_BACKEND_URL=http://127.0.0.1:8000

[!IMPORTANT]
Do not store secrets in frontend environment variables.

Variables prefixed with VITE_ are exposed to the browser.

▶️ Run the Development Server
npm run dev

The frontend will normally be available at:

http://localhost:5173
🔗 Backend Requirement

The Django backend should be running at:

http://127.0.0.1:8000

The backend is required for features such as:

Authentication
Workspace bookings
Payments
Notifications
User account functionality
Admin features
📦 Build for Production
npm run build

The production build will be generated inside:

dist/
👀 Preview Production Build
npm run preview
🔑 Authentication

The frontend uses JWT authentication with the Django backend.

Access and refresh tokens are handled through the Axios API service.

📁 Project Structure
src/
├── components/
│   ├── admin/
│   ├── dashboard/
│   └── home/
├── layouts/
├── router/
├── services/
├── stores/
├── views/
└── App.vue
📝 Notes
node_modules/ is ignored by Git.
dist/ is ignored by Git.
.env is ignored by Git.
The backend API must be running for authentication, bookings, payments, notifications, and admin functionality.
🧑‍💻 Development

Recommended development flow:

npm install
npm run dev

Make sure the Django API is running before testing features that communicate with the backend.

✅ Production Check

Before deployment, run:

npm run build

Then verify the production build with:

npm run preview


The biggest visual improvement will come from switching to the **Preview** tab in the editor. I
