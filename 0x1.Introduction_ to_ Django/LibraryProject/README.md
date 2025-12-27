# LibraryProject

This is a simple Django project created as an introduction to Django. It manages a collection of books.

## Features

*   **Book Model**: The project defines a `Book` model with the following fields:
    *   `title`: The title of the book.
    *   `author`: The author of the book.
    *   `publication_year`: The year the book was published.

*   **Admin Interface**: The `Book` model is registered with the Django admin interface, allowing for easy management of book records. The admin interface includes list filters and search functionality for books.

## Getting Started

To run this project, you need to have Python and Django installed.

1.  **Clone the repository or download the project files.**

2.  **Navigate to the project directory:**
    ```bash
    cd 0x1.Introduction_ to_ Django/LibraryProject
    ```

3.  **Install the dependencies.** This project uses `pipenv`.
    ```bash
    pipenv install
    pipenv shell
    ```

4.  **Apply the database migrations:**
    ```bash
    python manage.py migrate
    ```

5.  **Create a superuser to access the admin panel:**
    ```bash
    python manage.py createsuperuser
    ```

6.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```

7.  **Access the admin panel:**
    Open your web browser and go to `http://127.0.0.1:8000/admin/`. Log in with the superuser credentials you created. You can then add, edit, and delete books.