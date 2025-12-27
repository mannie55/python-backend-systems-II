# Django Blog

This is a full-featured blog application built with Django. It includes user authentication, profiles, posts, comments, tagging, and search functionality.

## Features

*   **User Authentication**: Users can register, log in, and log out.
*   **User Profiles**: Each user has a profile with a bio, location, and birthdate that they can update.
*   **Post Management**: Users can create, read, update, and delete their own posts.
*   **Commenting System**: Authenticated users can comment on posts. They can also edit or delete their own comments.
*   **Tagging**: Posts can be tagged with keywords, and users can browse posts by a specific tag.
*   **Search Functionality**: Users can search for posts by title, content, or tags.
*   **Authorization**: The application ensures that only the author of a post or comment can edit or delete it.
*   **Class-Based Views**: The project effectively uses Django's class-based views for handling posts and comments.
*   **Pagination**: The list of posts is paginated to improve performance and user experience.

## Getting Started

To run this project, you'll need Python, Django, and `django-taggit`.

1.  **Clone the repository or download the project files.**

2.  **Navigate to the project directory:**
    ```bash
    cd django_blog
    ```

3.  **Install the dependencies:**
    ```bash
    pip install django django-taggit
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

## Usage

*   **Homepage**: The homepage displays a list of all blog posts.
*   **Register/Login/Logout**: Use the respective links to manage your authentication state.
*   **Profile**: View and update your profile information from the profile page.
*   **Posts**: Create new posts, and view, edit, or delete your existing posts.
*   **Comments**: Add comments to posts, and edit or delete your own comments.
*   **Tags**: Click on a tag to see all posts with that tag.
*   **Search**: Use the search bar to find posts.
