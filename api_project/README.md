# API Project

This is a simple Django REST Framework project that provides a basic API for managing a collection of books.

## Features

*   **Book API**: A complete CRUD (Create, Read, Update, Delete) API for books.
*   **Token Authentication**: Uses token-based authentication to secure the API.
*   **ViewSets and Routers**: Utilizes `ModelViewSet` and `DefaultRouter` for concise and efficient API development.

## Getting Started

To run this project, you'll need Python, Django, and Django REST Framework installed.

1.  **Clone the repository or download the project files.**

2.  **Navigate to the project directory:**
    ```bash
    cd api_project
    ```

3.  **Install the dependencies:**
    ```bash
    pip install django djangorestframework
    ```

4.  **Apply the database migrations:**
    ```bash
    python manage.py migrate
    ```

5.  **Create a superuser to get an auth token:**
    ```bash
    python manage.py createsuperuser
    ```

6.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```

## API Endpoints

The project uses a `DefaultRouter`, which automatically generates the following URLs for the `BookViewSet`:

*   `GET /api/books/`: List all books.
*   `POST /api/books/`: Create a new book.
*   `GET /api/books/{id}/`: Retrieve a specific book.
*   `PUT /api/books/{id}/`: Update a specific book.
*   `PATCH /api/books/{id}/`: Partially update a specific book.
*   `DELETE /api/books/{id}/`: Delete a specific book.

### Authentication

To access the API, you first need to obtain an authentication token:

```bash
curl -X POST http://127.0.0.1:8000/api-token-auth/ -d "username=your_username&password=your_password"
```

Then, you can use the token in the `Authorization` header for your API requests:

```bash
curl -X GET http://127.0.0.1:8000/api/books/ -H "Authorization: Token YOUR_TOKEN_HERE"
```
