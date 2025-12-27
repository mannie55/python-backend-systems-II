# Social Media API

This project is a comprehensive back-end for a social media application built with Django and Django REST Framework. It includes features like user accounts, a following system, posts, comments, likes, a personalized feed, and a notification system.

## Features

*   **User Accounts**: A custom user model with profiles (bio and profile picture), user registration, and token-based authentication.
*   **Following System**: Users can follow and unfollow each other to create a social graph.
*   **Posts**: A full CRUD (Create, Read, Update, Delete) API for posts.
*   **Comments**: Users can comment on posts.
*   **Likes**: Users can like and unlike posts.
*   **Personalized Feed**: The post feed is tailored to each user, showing posts from the people they follow.
*   **Notification System**: A robust notification system that alerts users to new followers, likes, and comments. It uses Django's `GenericForeignKey` to associate notifications with different types of objects (e.g., posts, users).
*   **Custom Permissions**: Implements custom permissions to ensure that only the author of a post or comment has the right to edit or delete it.

## Getting Started

To run this project, you will need Python, Django, and Django REST Framework.

1.  **Clone the repository or download the project files.**

2.  **Navigate to the project directory:**
    ```bash
    cd social_media_api
    ```

3.  **Install the dependencies:**
    ```bash
    pip install django djangorestframework
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

The API is organized into three main applications: `accounts`, `posts`, and `notifications`.

### Accounts (`/api/`)

*   `POST /api/register/`: Create a new user account.
*   `POST /api/login/`: Obtain an authentication token.
*   `GET /api/profile/`: View your own user profile.
*   `POST /api/follow/<int:user_id>/`: Follow a user.
*   `POST /api/unfollow/<int:user_id>/`: Unfollow a user.

### Posts (`/api/posts/`)

*   `GET /api/posts/feed/`: Get your personalized post feed.
*   `GET, POST /api/posts/posts/`: List all posts or create a new post.
*   `GET, PUT, PATCH, DELETE /api/posts/posts/<int:pk>/`: Retrieve, update, or delete a specific post.
*   `POST /api/posts/<int:pk>/comment/`: Add a comment to a post.
*   `POST /api/posts/<int:pk>/like/`: Like a post.
*   `POST /api/posts/<int:pk>/unlike/`: Unlike a post.

### Notifications (`/notifications/`)

*   `GET /notifications/`: Get a list of your unread notifications.
*   `POST /notifications/mark-as-read/<int:notification_id>/`: Mark a specific notification as read.
