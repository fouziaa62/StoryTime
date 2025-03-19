# StoryTime

StoryTime is a web application where users can read and share their stories with the world. Users can create an account, log in, add stories, view profiles, and delete their profiles.

## Features

- User authentication (signup, login, logout)
- Add, edit, and delete stories
- View a list of stories
- View individual story details
- Like stories
- User profiles with profile pictures and bios
- Dark theme support

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/StoryTime.git
    cd StoryTime
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Apply migrations:
    ```bash
    python manage.py migrate
    ```

4. Create a superuser:
    ```bash
    python manage.py createsuperuser
    ```

5. Run the development server:
    ```bash
    python manage.py runserver
    ```

6. Open your browser and go to `http://127.0.0.1:8000/` to see the application.

## Usage

- **Landing Page**: The main page of the application.
- **Signup**: Create a new user account.
- **Login**: Log in to an existing account.
- **Story List**: View a list of all stories.
- **Story Detail**: View the details of a specific story.
- **Add Story**: Add a new story.
- **Edit Story**: Edit an existing story.
- **Delete Story**: Delete a story.
- **Profile**: View and edit user profile.
- **Delete Profile**: Delete user profile and redirect to the landing page.

## File Structure

- `stories/templates/stories/`: Contains HTML templates for the application.
- `stories/views.py`: Contains view functions for handling requests.
- `stories/urls.py`: Contains URL patterns for routing.
- `static/styles/style.css`: Contains CSS styles for the application.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.