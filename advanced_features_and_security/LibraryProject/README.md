# LibraryProject - Advanced Features and Security

This Django project is an advanced version of the simple LibraryProject, incorporating more complex features and security measures. It demonstrates role-based access control, custom user models, and more intricate relationships between models.

## Features

*   **Custom User Model**: Extends the default Django `User` model with additional fields like `date_of_birth` and `profile_photo`.
*   **Role-Based Access Control (RBAC)**: Implements different roles for users (Admin, Librarian, Member) with specific permissions for each role.
*   **Book Management**: Full CRUD (Create, Read, Update, Delete) functionality for books, protected by permissions.
*   **User Authentication**: Includes user registration, login, and logout functionality.
*   **Model Relationships**: Demonstrates various model relationships:
    *   `OneToOneField`: Between `Librarian` and `Library`, and `UserProfile` and `User`.
    *   `ForeignKey`: Between `Book` and `Author`.
    *   `ManyToManyField`: Between `Library` and `Book`.
*   **Custom Permissions**: Defines custom permissions for the `Book` model.

## Project Structure

The project is divided into two main apps:

*   `bookshelf`: Contains the `CustomUser` model and initial `Book` model with custom permissions.
*   `relationship_app`: Contains the core logic for role-based access, views, and more detailed models (`Author`, `Library`, `Librarian`, `UserProfile`).

## Getting Started

To run this project, you need to have Python and Django installed.

1.  **Clone the repository or download the project files.**

2.  **Navigate to the project directory:**
    ```bash
    cd advanced_features_and_security/LibraryProject
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
    After creating a superuser, a `UserProfile` with the role 'member' will be automatically created. To test the admin functionality, you'll need to go to the admin panel and change the role of your superuser to 'admin'.

6.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```

7.  **Access the application:**
    *   **Registration**: `http://127.0.0.1:8000/register/`
    *   **Login**: `http://127.0.0.1:8000/login/`
    *   **Admin View**: `http://127.0.0.1:8000/admin/` (requires admin role)
    *   **Librarian View**: `http://127.0.0.1:8000/librarian/` (requires librarian role)
    *   **Member View**: `http://127.0.0.1:8000/member/` (requires member role)
    *   **Book List**: `http://127.0.0.1:8000/books/`
