# E-Commerce Web Application 🚀

This repository contains the source code for a fully functional e-commerce web application built using Django.

## Why Django? 🤔

Django is a powerful and versatile web framework that simplifies the development process while ensuring security, scalability, and maintainability. Here are some reasons why Django was chosen for this project:

- **Built-in Features**: Django provides essential tools like user authentication, admin interface, and ORM out of the box, which accelerates development.
- **Security**: Django helps protect against common web vulnerabilities, such as SQL injection, cross-site scripting (XSS), and cross-site request forgery (CSRF).
- **Scalability**: With its modular architecture, Django can scale easily to handle high traffic and complex business logic.
- **Community Support**: Django has an extensive community and rich documentation, making it easier to learn and troubleshoot issues.


## Features 🌟

- **User Authentication**: Registration, login, and profile management.
- **Product Management**: Add, update, delete, and display products.
- **User Profiles**: Comprehensive user profiles, including account management.
- **Seller Listings**: Sellers can add, update, and view their product listings.

## Tech Stack 🛠️

- **Frontend**: HTML, Tailwind CSS  
- **Backend**: Django  
- **Database**: SQLite  

## Installation and Setup ⚙️

1. Clone the repository:
   ```bash
   git clone https://github.com/a-anuj/django.git
   cd django
    ```
2. Create a virtual environment and activate it:
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows: env\Scripts\activate
    ```
3. Install django
    ```bash
    pip install django
    ```

4. Apply migrations
    ```bash
    python manage.py migrate
    ```

5. Start the development server:
    ```bash
    python manage.py runserver
    ```

Open your browser and visit http://127.0.0.1:8000