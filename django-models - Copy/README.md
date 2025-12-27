# Django Models and Relationships

This project demonstrates various database models and their relationships in Django. It serves as a practical example of how to structure your data models for a library management system.

## Data Models

The project includes the following models, primarily in the `relationship_app`:

*   **`UserProfile`**: Extends the default Django `User` model with a one-to-one relationship to add a `role` field. This is used to manage user roles (Admin, Librarian, Member). A `UserProfile` is automatically created for each new `User` using a signal.

*   **`Author`**: A simple model to store author names.

*   **`Book`**: Represents a book with a title and a `ForeignKey` relationship to the `Author` model (a many-to-one relationship). It also includes custom permissions in its `Meta` class.

*   **`Library`**: Represents a library with a name and a `ManyToManyField` relationship to the `Book` model (a library can have many books, and a book can be in many libraries).

*   **`Librarian`**: Represents a librarian with a name and a `OneToOneField` relationship to the `Library` model (a librarian is in charge of one library).

## Getting Started

To explore this project, you can examine the code in the `relationship_app/models.py` file. You can also run the project to interact with the models through the Django admin interface.

1.  **Clone the repository or download the project files.**

2.  **Navigate to the project directory:**
    ```bash
    cd "django-models - Copy"
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
    Open your web browser and go to `http://127.0.0.1:8000/admin/`. Log in with your superuser credentials to view and manage the different models.