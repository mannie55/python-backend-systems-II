# Advanced API Project

This project is a Django REST Framework API for managing a collection of books and authors. It includes features like token-based authentication, filtering, searching, and ordering.

## Features

*   **Book and Author API Endpoints**: Provides full CRUD (Create, Read, Update, Delete) functionality for books and authors.
*   **Token Authentication**: Secures the API using `djangorestframework.authtoken`.
*   **Filtering**: Allows filtering books by `publication_year` and `author__name`.
*   **Searching**: Enables searching for books by `title` and `author__name`.
*   **Ordering**: Supports ordering books by `title` and `publication_year`.
*   **Serialization**: Uses `ModelSerializer` to handle the conversion of `Book` and `Author` models to and from JSON.
*   **Nested Serialization**: The `Author` serializer includes a list of books written by the author.

## Getting Started

To run this project, you need to have Python, Django, and Django REST Framework installed.

1.  **Clone the repository or download the project files.**

2.  **Navigate to the project directory:**
    ```bash
    cd advanced-api-project
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Apply the database migrations:**
    ```bash
    python manage.py migrate
    ```

5.  **Create a superuser:**
    ```bash
    python manage.py createsuperuser
    ```

6.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```

## API Endpoints

The following API endpoints are available:

*   `POST /api/token/`: Obtain an authentication token by providing a username and password.
*   `GET /api/books/`: Get a list of all books.
*   `POST /api/books/create`: Create a new book (requires authentication).
*   `GET /api/books/<int:pk>/`: Retrieve a specific book by its ID.
*   `PUT /api/books/update/<int:pk>/`: Update a book (requires authentication).
*   `DELETE /api/books/delete/<int:pk>/`: Delete a book (requires authentication).
*   `GET /api/authors/`: Get a list of all authors and their books.
*   `POST /api/authors/`: Create a new author (requires authentication).

### Example Usage

1.  **Get an authentication token:**
    ```bash
    curl -X POST http://127.0.0.1:8000/api/token/ -d "username=your_username&password=your_password"
    ```

2.  **Create a new book:**
    ```bash
    curl -X POST http://127.0.0.1:8000/api/books/create -H "Authorization: Token YOUR_TOKEN_HERE" -d "title=New Book&author=1&publication_year=2023"
    ```

3.  **List all books:**
    ```bash
    curl http://127.0.0.1:8000/api/books/
    ```