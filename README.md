# Digital Waste Management System (DWMS)

The **Digital Waste Management System (DWMS)** is an innovative solution aimed at streamlining waste collection and management. By leveraging technologies such as Google Plus Codes, GPS, and secure payment gateways, the system ensures efficient, scalable, and user-friendly operations for various stakeholders, including customers, employees, and administrators.

---

## Features

### **1. User Roles and Access**
- **Customer**: Register for services, manage subscriptions, and track service notifications.
- **Employee**: View assigned tasks, confirm service completion, and report issues.
- **Admin**: Oversee user accounts, manage routes, payments, and monitor overall operations.
- **Supervisor**: Assign shifts, monitor performance, and handle escalations.

### **2. Key Functionalities**
- **Location Management**:
  - Integration with Google Plus Codes for precise geolocation.
  - Support for multiple addresses (home, business).
- **Subscription Management**:
  - Multiple service plans (weekly, monthly).
  - Real-time notifications for renewals and payments.
- **Payment Processing**:
  - Secure gateways including M-Pesa, PayPal, and credit cards.
  - Automatic invoice generation and billing history tracking.
- **Employee & Shift Management**:
  - Role-based shift assignments with GPS and QR code validation.
- **Route Optimization**:
  - Dynamic route updates based on payment status and traffic data.
- **Reporting & Analytics**:
  - Real-time and historical reports for performance tracking and decision-making.

---

## Project Structure

```plaintext
DWMS
│
├── dwms/                          # Core Django project
│   ├── settings.py                # Global settings and configurations
│   ├── urls.py                    # URL routing
│   ├── asgi.py, wsgi.py           # ASGI/WSGI configurations
│
├── user_registration/             # User management module
│   ├── templates/                 # User-facing HTML templates
│   ├── models.py                  # Custom user model (RBAC integration)
│   ├── views.py                   # User logic
│
├── establishment_registration/    # Establishment module
│   ├── templates/                 # Establishment registration views
│   ├── forms.py                   # Forms for establishment data
│   ├── models.py                  # Establishment database structure
│   ├── views.py                   # Logic for CRUD operations
│
├── location_registration/         # Location tracking module
│   ├── models.py                  # Location and Plus Code management
│   ├── forms.py                   # Location-related forms
│   ├── views.py                   # Address-related views
│
├── occupant_registration/         # Occupant registration module
│   ├── templates/                 # Occupant-facing views
│   ├── forms.py                   # Occupant enrollment forms
│   ├── views.py                   # Logic for occupant management
│
└── templates/
    ├── base.html                  # Global HTML template
    └── various templates for UIs
```

---

## Installation and Setup

### **Requirements**
- Python (v3.9 or higher)
- Django (v4.0+)
- A database engine (SQLite, MySQL, or PostgreSQL)
- Google Maps API Key (for Plus Code integration)

### **Steps to Run Locally**
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/dwms.git
   cd dwms
   ```
2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv env
   source env/bin/activate      # On Windows: env\Scripts\activate
   pip install -r requirements.txt
   ```
3. Set up the database:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
4. Run the development server:
   ```bash
   python manage.py runserver
   ```
5. Access the application at `http://127.0.0.1:8000`.

---

## Technologies Used

- **Frontend**: HTML5, CSS3, JavaScript (integrated with Django templates)
- **Backend**: Django Framework (Python)
- **Database**: SQLite (default), with support for MySQL/PostgreSQL
- **APIs**: Google Maps API (Plus Codes integration)
- **Authentication**: JSON Web Tokens (JWT), Role-Based Access Control (RBAC)
- **Payment Gateways**: M-Pesa, PayPal, and credit cards

---

## Current Progress

- Role-switching functionality is fully operational.
- Dashboards for **owners** and **occupants** allow:
  - Adding/removing establishments.
  - Managing occupants.
  - Editing personal details.

### Modules Completed:
- **User Registration**: Registration and login with email verification.
- **Location Registration**: Linking multiple Plus Codes to users.
- **Occupant Management**: Enrollment and role-switching features.

---

## Next Steps

### **Integrating Automatic Capture and Validation of Google Plus Codes**
- **Objective**:
  - Automate the process of capturing Plus Codes for precise location tracking during registration.
  - Validate captured Plus Codes against user input to ensure accuracy and prevent duplication.
- **Approach**:
  - Utilize Google Maps API to fetch and validate Plus Codes dynamically.
  - Implement a frontend interface for users to pinpoint locations on a map.
  - Enhance backend validation to cross-check Plus Codes against existing records in the database.

This feature will ensure seamless location management, minimize manual errors, and improve the overall system usability.

---

## Contributing

Contributions are welcome! Please follow these steps:
1. Fork this repository.
2. Create a new branch for your feature:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes and push to your fork.
4. Submit a pull request describing your changes.

---

## License

This project is licensed under the [MIT License](LICENSE).

---
