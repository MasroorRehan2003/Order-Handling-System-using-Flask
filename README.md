Order Handling System – Flask Backend
This project is a simple Order Management System built using Python's Flask framework. It allows users to add, edit, delete, and mark orders as delivered. Each operation is logged with details such as timestamp and performer. The system uses in-memory data structures and is intended for demonstration and learning purposes.


Features
Add new orders

Edit existing orders

Delete orders

Mark orders as delivered

View action logs for all performed operations

Simple HTML-based interface (forms and tables)

In-memory storage (no database required)

#  Tech Stack
Backend: Python (Flask)

Frontend: HTML (basic templating with Jinja2)

Data Handling: In-memory Python lists (orders, logs)

#  Approach

The project follows a simple and modular approach suitable for small-scale or educational applications:

Routing & Logic: All backend routes are defined in app.py, which manages GET and POST requests for adding, editing, deleting, and delivering orders.

Data Structure: Instead of using a database, orders and logs are stored in Python lists. This makes the application fast and easy to test, though not persistent.

Data Models: models.py defines two lightweight classes — Order and ActionLog — to encapsulate data and promote clean coding.

Templating: Jinja2 templating (built into Flask) is used to dynamically render order and log data in HTML files.

Logging: Every operation performed on an order (create, edit, delete, deliver) is tracked with a timestamp, user identity, and action type. This information is displayed in the Action Logs view.

Minimal UI: The frontend is kept very simple using basic HTML forms and tables, avoiding CSS or JavaScript for maximum clarity and focus on logic.

This system is ideal for:

Flask beginners

Backend design practice

Demonstrating CRUD operations