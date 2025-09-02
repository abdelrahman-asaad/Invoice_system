Invoice System
Project Overview

Invoice System is a Django-based web application for managing clients, products, invoices, payments, users, and audit logs. The project provides REST API endpoints to handle all operations and integrates JWT authentication for secure access.

The application uses SQLite as the database, Django REST Framework for API development, and django-decouple for environment configuration.

Features

User registration, login, and role management.

Client management (CRUD operations).

Product management (CRUD operations).

Invoice management with PDF generation.

Payment tracking.

Dashboard with sales summary and profit tracking.

Audit logging of all actions.

Installation

Clone the repository:

git clone https://github.com/yourusername/Invoice_system.git
cd Invoice_system/invoice_sys


Create a virtual environment:

python3.10 -m venv invoice_env
source invoice_env/bin/activate  # Linux / macOS
invoice_env\Scripts\activate     # Windows


Install dependencies:

pip install --upgrade pip
pip install -r requirements.txt


Set up .env file:
Create a .env file in the root directory with the following content:

SECRET_KEY="your_secret_key_here"
DEBUG=True


Apply migrations:

python manage.py makemigrations
python manage.py migrate


Create a superuser (optional):

python manage.py createsuperuser


Collect static files:

python manage.py collectstatic --noinput


Run the development server 



API Endpoints
Accounts

POST /api/accounts/register/ → Register a new user.

POST /api/accounts/token/ → Obtain JWT access & refresh token.

POST /api/accounts/token/refresh/ → Refresh JWT token.

GET /api/accounts/users/ → List all users.

PUT /api/accounts/users/<id>/role/ → Update user role.

Audit Logs

GET /api/auditlogs/ → List all audit logs.

Clients

GET /api/clients/ → List all clients.

POST /api/clients/create/ → Create a new client.

PUT /api/clients/<id>/update/ → Update client details.

DELETE /api/clients/<id>/delete/ → Delete client.

Dashboard

GET /api/dashboard/ → Dashboard main page.

GET /api/dashboard/sales-summary/ → Sales summary.

GET /api/dashboard/profit-tracker/ → Profit tracker.

Invoices

GET /api/invoices/ → List all invoices.

POST /api/invoices/ → Create a new invoice.

GET /api/invoices/<id>/ → Retrieve invoice details.

PUT /api/invoices/<id>/ → Update invoice.

DELETE /api/invoices/<id>/ → Delete invoice.

GET /api/invoices/<id>/pdf/ → Download invoice as PDF.

Payments

GET /api/payments/ → List all payments.

POST /api/payments/ → Record a new payment.

Products

GET /api/products/ → List all products.

POST /api/products/ → Create a new product.

GET /api/products/<id>/ → Retrieve product details.

PUT /api/products/<id>/ → Update product.

DELETE /api/products/<id>/ → Delete product.

Technologies Used

Python 3.10

Django 5.2.4

Django REST Framework

django-filter

django-decouple

SQLite (default DB)

JWT Authentication (Simple JWT)

Bootstrap / HTML templates for frontend

Notes

Make sure the .env file is correctly set on the server.

Run collectstatic after any static file changes.

Use the same Python version for virtual environment as on server if deploying.

For production, set DEBUG=False in .env.
