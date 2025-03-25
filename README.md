# StoryTime

StoryTime is a web application where users can read and share their stories with the world. Users can create an account, log in, add stories, view profiles, and delete their profiles.
![Screenshot 2025-03-23 142119](https://github.com/user-attachments/assets/f8441856-6f90-44fe-b57c-141970270fbb)

## Introduction

Welcome to StoryTime! This project allows users to share their stories with a community of readers. You can explore the source code on GitHub and check out the live project using the links below:

- [Source Code](https://github.com/fouziaa62/StoryTime)
- [Live Project](https://stories-724c424e708b.herokuapp.com/)

## Purpose

The purpose of StoryTime is to provide a platform for users to share their personal stories and experiences with a wider audience. It aims to create a community where people can connect through storytelling, inspire others, and find common ground. Whether it's a fictional tale, a personal anecdote, or a life lesson, StoryTime encourages users to express themselves and engage with the stories shared by others.

## Key Features

- **User Authentication**: Secure signup, login, and logout functionality to ensure user data privacy and security.
- **Story Management**: Users can add new stories, edit existing ones, and delete stories they no longer wish to share.
- **Profile Management**: Users can view and edit their profiles, including uploading profile pictures and writing bios to personalize their accounts.
- **Story Interaction**: Users can like stories to show appreciation and leave comments to engage with the content and the author.
- **Responsive Design**: The application is fully responsive, ensuring a seamless experience on desktops, tablets, and mobile devices.
- **Dark Theme Support**: Users have a dark theme for a more comfortable reading experience, especially in low-light environments.

## User Experience

StoryTime is designed to provide an intuitive and engaging user experience. Key aspects of the user experience include:

- **Easy Navigation**: The application features a clean and simple layout, making it easy for users to navigate between different sections such as the story list, profile, and story details.
- **Interactive Elements**: Users can interact with stories by liking them and leaving comments, fostering a sense of community and engagement.
- **Personalization**: Users can personalize their profiles with profile pictures and bios, making their accounts unique and reflective of their personalities.
- **Responsive Design**: The responsive design ensures that the application looks and works great on all devices, from desktops to smartphones.
- **Dark Theme**: The dark theme option provides a comfortable reading experience, especially in low-light conditions.

### Site Users

StoryTime caters to a diverse range of users, including:

- **Storytellers**: Individuals who want to share their personal stories, experiences, and creative writing with a wider audience.
- **Readers**: Users who enjoy reading stories and engaging with the content by liking and commenting.
- **Community Members**: Users who want to connect with others through storytelling and find common ground through shared experiences.

### Goals

The primary goals of StoryTime are:

- **Encourage Storytelling**: Provide a platform for users to share their stories and express themselves creatively.
- **Foster Community**: Create a sense of community where users can connect through shared experiences and engage with each other's stories.
- **Enhance User Experience**: Ensure a seamless and enjoyable user experience through responsive design, easy navigation, and interactive elements.

## Database Structure and Purpose

### Overview

The database structure of StoryTime is designed to efficiently store and manage user data, stories, comments, likes, and profiles. It ensures data integrity and supports the core functionalities of the application.

### Core Models

- **User**: Represents the users of the application. It includes fields for username, email, password, and other authentication-related information. This model is provided by Django's built-in authentication system.
- **Profile**: Extends the User model to include additional information such as profile picture and bio. This model allows users to personalize their accounts with a profile picture and a short biography.
- **Story**: Represents the stories shared by users. It includes fields for title, content, author, and timestamps for creation and updates. The author field is a foreign key linking to the User model, indicating which user created the story.
- **Comment**: Represents comments made by users on stories. It includes fields for the comment text, author, story, and timestamps. The author field is a foreign key linking to the User model, and the story field is a foreign key linking to the Story model, indicating which story the comment belongs to.
- **Like**: Represents likes given by users to stories. It includes fields for the user and the story they liked. Both fields are foreign keys linking to the User and Story models, respectively, indicating which user liked which story.

## Entity-Relationship Diagram (ERD)

The ERD below illustrates the relationships between the core models in the StoryTime application:

![Screenshot 2025-03-24 154019](https://github.com/user-attachments/assets/24fbc912-7e6f-4dc7-bb08-065a3064c975)


- **User**: The central entity representing the users of the application.
- **Profile**: Each user has one profile, which includes additional information such as profile picture and bio.
- **Story**: Each story is authored by a user and can have multiple comments and likes.
- **Comment**: Each comment is made by a user on a specific story.
- **Like**: Each like is given by a user to a specific story.

## Database Design Decisions

### Choice of PostgreSQL

PostgreSQL was chosen as the database management system for StoryTime due to its robustness, scalability, and support for advanced features. PostgreSQL offers strong data integrity, ACID compliance, and extensive support for complex queries, making it an ideal choice for handling the application's data requirements.

### Model Structure

The model structure in StoryTime is designed to reflect the core entities and their relationships within the application. Each model represents a distinct entity, such as users, profiles, stories, comments, and likes. The relationships between these models are defined using foreign keys, ensuring data consistency and enabling efficient data retrieval.

### Security Considerations

Security is a critical aspect of the database design for StoryTime. Key security considerations include:

- **Data Encryption**: Sensitive data, such as passwords, are encrypted using industry-standard hashing algorithms to protect user information.
- **Access Control**: Access to the database is restricted to authorized users only, with role-based access control implemented to ensure that users have appropriate permissions.
- **Data Validation**: Input data is validated at both the application and database levels to prevent SQL injection and other common security vulnerabilities.

## Future Database Enhancements

### Scalability

As the user base grows, the database structure may need to be optimized for scalability. This could include implementing database sharding, indexing frequently accessed fields, and optimizing query performance to handle a larger volume of data efficiently.

### Advanced Search Functionality

Enhancing the search functionality to support advanced search queries, such as full-text search, filtering by tags or categories, and sorting by relevance, can improve the user experience and make it easier for users to find specific stories.

### Analytics and Reporting

Implementing analytics and reporting features can provide valuable insights into user behavior, story engagement, and overall platform performance. This could include tracking metrics such as the number of stories published, comments made, likes received, and user activity over time.

### Enhanced Security Measures

Continuously improving security measures to protect user data and prevent unauthorized access is crucial. This could include implementing two-factor authentication, monitoring for suspicious activity, and regularly updating security protocols to address emerging threats.

### Integration with External Services

Integrating the database with external services, such as social media platforms, cloud storage, and third-party authentication providers, can enhance the functionality and user experience of StoryTime. This could include allowing users to share stories on social media, store media files in the cloud, and log in using their existing social media accounts.

## Database Management

### Migrations

Django's migration system is used to manage changes to the database schema over time. Migrations allow you to evolve your database schema as your application grows and changes, without losing data.

To create a new migration after making changes to your models, run:

```bash
python manage.py makemigrations
```

This command will generate a new migration file in the `migrations` directory of your app. To apply the migration and update the database schema, run:

```bash
python manage.py migrate
```

This command will apply all pending migrations and bring your database schema up to date.

### Rollback

If you need to undo a migration, you can use the `migrate` command with the name of the app and the migration number you want to roll back to. For example, to roll back the last migration in the `stories` app, run:

```bash
python manage.py migrate stories <previous_migration_number>
```

Replace `<previous_migration_number>` with the migration number you want to roll back to.

### Inspecting Migrations

To see a list of all migrations and their status, run:

```bash
python manage.py showmigrations
```

This command will display a list of all migrations and indicate which ones have been applied.

### Creating a Superuser

To create a superuser who can access the Django admin interface, run:

```bash
python manage.py createsuperuser
```

Follow the prompts to create a new superuser account. This account can be used to log in to the admin interface and manage the application.

### Database Backup and Restore

Regular backups of the database are essential to ensure data recovery in case of data loss or corruption. To back up the PostgreSQL database, you can use the `pg_dump` command:

```bash
pg_dump dbname > backup.sql
```

Replace `dbname` with the name of your database and `backup.sql` with the desired backup file name.

To restore the database from a backup, use the `psql` command:

```bash
psql dbname < backup.sql
```

Replace `dbname` with the name of your database and `backup.sql` with the backup file name.

## Database Access Patterns

### Common Queries

Here are some common queries used in the StoryTime application:

- **Retrieve all stories**:
    ```python
    stories = Story.objects.all()
    ```

- **Retrieve a specific story by ID**:
    ```python
    story = Story.objects.get(id=story_id)
    ```

- **Retrieve all comments for a specific story**:
    ```python
    comments = Comment.objects.filter(story=story)
    ```

- **Retrieve all stories authored by a specific user**:
    ```python
    user_stories = Story.objects.filter(author=user)
    ```

- **Retrieve all likes for a specific story**:
    ```python
    likes = Like.objects.filter(story=story)
    ```

## Performance Considerations

### Indexing

Indexing frequently accessed fields can significantly improve query performance. Ensure that fields used in filter conditions and join operations are indexed.

### Query Optimization

Optimize queries to minimize the number of database hits. Use select_related and prefetch_related to fetch related objects in a single query.

### Caching

Implement caching strategies to reduce the load on the database. Cache frequently accessed data and use cache invalidation techniques to keep the cache up to date.

### Load Testing

Perform load testing to identify performance bottlenecks and optimize the database and application accordingly. Use tools like Apache JMeter or Locust to simulate high traffic and measure performance.

### Monitoring

Set up monitoring to track database performance metrics such as query execution time, slow queries, and resource utilization. Use tools like pgAdmin, New Relic, or Datadog to monitor and analyze database performance.

## Agile Development

### Iterative Development

StoryTime follows an iterative development process, where the project is divided into small, manageable iterations or sprints. Each iteration focuses on delivering a specific set of features or improvements, allowing for continuous feedback and adjustments.

### User Stories

User stories are used to capture the requirements and expectations of the users. Each user story describes a specific feature or functionality from the user's perspective, including the desired outcome and acceptance criteria.

Some examples of user stories from the project board are:

- **As a user, I want to create an account so that I can share my stories with others.**
- **As a user, I want to log in to my account so that I can access my profile and stories.**
- **As a user, I want to add a new story so that I can share my experiences with the community.**
- **As a user, I want to edit my profile so that I can update my bio and profile picture.**
- **As a user, I want to like and comment on stories so that I can engage with the content and the author.**

## User Interface

### Wireframes

<!-- Add wireframe images here -->

### Color Scheme

The color scheme for StoryTime is designed to be visually appealing and easy on the eyes. The primary colors used are:

- **Primary Color**: #007bff (Bootstrap Blue)
- **Secondary Color**: #6c757d (Gray)
- **Success Color**: #28a745 (Green)
- **Danger Color**: #dc3545 (Red)
- **Warning Color**: #ffc107 (Yellow)
- **Info Color**: #17a2b8 (Cyan)
- **Light Color**: #f8f9fa (Light Gray)
- **Dark Color**: #343a40 (Dark Gray)

### Fonts

The fonts used in StoryTime are chosen for readability and aesthetics. The primary font used is:

- **Font**: Arial, sans-serif

Additional styles and font weights are used to create hierarchy and emphasis within the text.

## Templates

### Base Template (`base.html`)

The base template provides the overall structure for the application and common styles. It serves as the foundation for all other templates.

### Landing Page (`landing.html`)

The landing page template is the first page users see when they visit the application. It provides an overview of the platform and highlights some of the latest stories.

### Story List (`stories/story_list.html`)

The story list template displays a list of all stories shared by users. It includes links to view individual story details and options to add new stories.

### Story Detail (`stories/story_detail.html`)

The story detail template displays the full content of a specific story, along with comments and likes. Users can interact with the story by liking it and leaving comments.

### Add Story (`stories/add_story.html`)

The add story template provides a form for users to submit new stories. It includes fields for the story title and content.

### Edit Story (`stories/edit_story.html`)

The edit story template provides a form for users to edit their existing stories. It pre-fills the form with the current story details.

### Delete Story (`stories/delete_story.html`)

The delete story template provides a confirmation prompt for users to delete their stories. It ensures that users do not accidentally delete their content.

### Profile (`stories/profile.html`)

The profile template displays the user's profile information, including their bio and profile picture. Users can view and edit their profile details.

### Edit Profile (`stories/edit_profile.html`)

The edit profile template provides a form for users to update their profile information, including their bio and profile picture.

### Delete Profile (`stories/delete_profile.html`)

The delete profile template provides a confirmation prompt for users to delete their profiles. It ensures that users do not accidentally delete their accounts.

### Signup (`registration/signup.html`)

The signup template provides a form for users to create a new account. It includes fields for the username, email, and password.

### Login (`registration/login.html`)

The login template provides a form for users to log in to their accounts. It includes fields for the username and password.

### Password Change (`registration/password_change.html`)

The password change template provides a form for users to change their passwords. It includes fields for the current password and the new password.

## Views

### Landing Page View (`landing_page`)

This view function returns the landing page with the latest 6 stories.

### Story List View (`story_list`)

This view function returns a list of all stories, ordered by creation date.

### Signup View (`signup`)

This view function handles user signup by displaying a signup form and saving the user to the database.

### Story Detail View (`story_detail`)

This view function returns the details of a specific story, including comments and likes. It also handles the submission of new comments.

### Add Story View (`add_story`)

This view function provides a form for users to submit new stories. It requires the user to be logged in.

### Edit Story View (`edit_story`)

This view function provides a form for users to edit their existing stories. It requires the user to be logged in and the author of the story.

### Delete Story View (`delete_story`)

This view function provides a confirmation prompt for users to delete their stories. It requires the user to be logged in and the author of the story.

### Profile View (`profile_view`)

This view function returns the user's profile information, including their bio and profile picture. It requires the user to be logged in.

### Edit Profile View (`edit_profile`)

This view function provides a form for users to update their profile information, including their bio and profile picture. It requires the user to be logged in.

### Delete Profile View (`delete_profile`)

This view function provides a confirmation prompt for users to delete their profiles. It requires the user to be logged in.

### Custom Login View (`custom_login`)

This view function handles user login by displaying a login form and authenticating the user.

### Toggle Like View (`toggle_like`)

This view function allows users to like or unlike a story. It requires the user to be logged in.

### Login Success Signal (`login_success`)

This signal handler displays a welcome message when a user logs in successfully.

### Logout Success Signal (`logout_success`)

This signal handler displays a logout message when a user logs out successfully.

## Testing and Validation

### HTML Validation

The HTML code was validated using the W3C Markup Validation Service to ensure it adheres to web standards and is free of errors.

### CSS Validation

The CSS code was validated using the W3C CSS Validation Service (Jigsaw) to ensure it adheres to web standards and is free of errors.

### JavaScript Validation

The JavaScript code was validated using JSLint to ensure it adheres to best practices and is free of errors.

### Python Code Validation

The Python code was validated using a continuous integration (CI) pipeline with a Python linter to ensure it adheres to best practices and is free of errors.

## Manual Testing

This section outlines a list of manual test cases to ensure that the core functionalities of the **StoryShare** application work as expected.

### 1. User Authentication Tests
- [x] **Create User Account** – Users should be able to sign up successfully.
- [x] **Login** – Users should be able to log in with valid credentials.
- [x] **Logout** – Logged-in users should be able to log out successfully.
- [x] **Superuser Access Admin Panel** – Only superusers should access `/admin/`.
- [x] **Non-Superuser Cannot Access Admin Panel** – Regular users should be restricted from `/admin/`.

### 2. Story Management Tests
- [x] **Users Can Write a Story** – Authenticated users should be able to create a new story.
- [x] **Users Can Edit Only Their Own Stories** – Users should only edit the stories they created.
- [x] **Users Cannot Add a Story Without a Title** – The system should not allow empty titles.
- [x] **Users Can Delete Their Story** – Users should be able to delete their own stories.
- [x] **Users Can Write a Limited Number of Words** – There should be a word limit for stories.

### 3. Profile Management Tests
- [x] **Users Can Make a Profile** – Users should be able to create a profile.
- [x] **Users Can Edit Their Profile** – Only the profile owner can edit their profile.
- [x] **Users Can Delete Their Profile** – Users should be able to delete their own profile.
- [x] **Bio Has a Word Limit** – The bio section should not exceed the set word limit.

### 4. Interaction Tests (Comments & Likes)
- [x] **Users Can Comment on a Story** – Logged-in users should be able to comment.
- [x] **Users Can Only Like a Story Once** – A user should not be able to like a story multiple times.
- [x] **Comments Have a Word Limit** – Users should not exceed the set word limit for comments.

---


This checklist ensures a fully functional and user-friendly application. 










