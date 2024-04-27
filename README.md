# drf-api
"MMAPI"" is the backend service used by the [MarketMingle](https://github.com/AntonEi/marketmingle) platform.
The deployed DjangoRESTFramework API can be found [here](https://marketmingle-d94891f1357b.herokuapp.com/)

# Purpose of the API:
To serve as the Back bone for the Front-end, by posting and getting data from endpoints and to perform Create, Read, Update and Delete operations to objects entered by Users via Front-end.

### User Stories

Posts app: 
- As a user, I want to be able to create, edit, and delete posts so that I can share content with others.
- As a user, I want to be able to view posts from other users so that I can discover new content and engage with the community.
- As a user, I want to be able to filter posts based on various criteria such as date, popularity, or topic.

Tags App:
- As a user, I want to be able to add tags to my posts so that I can categorize and organize my content.
- As a user, I want to be able to click on a tag to view all posts associated with that tag so that I can explore related content.
- As a creator, I want to be able to manage tags by creating, editing, and deleting them so that I can maintain a consistent tagging system.

Profiles App:
- As a user, I want to be able to view my profile so that I can see an overview of my activity and information.
- As a user, I want to be able to edit my profile information such as username, bio, and profile picture.
- As a user, I want to be able to see other users' profiles so that I can learn more about them and their activity on the platform.

Likes App: 
- As a user, I want to be able to like content so that I can express appreciation for items that I enjoy or find useful.
- As a user, I want to see the total number of likes on a piece of content so that I can gauge its popularity or appeal.
- As a user, I want to be able to unlike content if I change my mind or made a mistake in liking it.

Dislikes App:
- As a user, I want to be able to "dislike" certain content so that I can express my preferences and provide feedback on items I don't like .
- As a user, I want to see the total number of dislikes on a piece of content so that I can gauge its popularity or controversiality.

Comments App: 
- As a user, I want to be able to add comments to posts so that I can engage in discussions and provide feedback.
- As a user, I want to be able to delete my own comments so that I can manage my contributions to discussions.
- As a user, I want to be able to edit my comments so that I can correct mistakes or update information.

Followers App:
- As a user, I want to be able to follow other users or entities so that I can stay updated on their activities and receive notifications about their actions.
- As a user, I want to see a list of followers for my profile so that I can interact with them or follow them back if desired.
- As a user, I want to receive notifications when someone follows me so that I can acknowledge their interest in my content.

Polls App:
- As a user, I want to be able to participate in polls so that I can share my opinion on various topics.
- As a user, I want to see the results of polls after I have voted so that I can compare my opinion with others.
- As a creator, I want to be able to create, edit, and delete polls so that I can engage my audience and gather feedback.

## Features

- User Registration and Authentication: Allows users to create accounts, log in and log out to access personalized features.
- Profile Management: Profiles are automatically created upon registration. Profiles can be updated including personal information and bio.
- Posts Creation and Interaction: Users can create posts, like and comment on others posts.
- Followers and likes System: Users can follow each other and be bullish/bearish on each others' content.
- Poll Feature: Visitors can easily answer poll questions to share their opinions and contribute to discussions on the site.
- Tag Feature: Users can tag posts and events to enhance categorization and searchability.

### Future Features

- User Messaging System: Implement a messaging system to allow users to communicate with each other privately.

- Notification System: Introduce a notification system to alert users about new interactions, events, or updates relevant to their interests.

## Database Design

The applicatopn leverages a relational database structured around Django models. The relationships between the models are illustrated in the ERD:

![ERD](documentation/hoodsap_ERD.png)

- **Profile**: Contains user profiles with additional information like name, content, and image.
- **Location**: Stores geographical data with fields for latitude, longitude, country, city, and locality. It's referenced by the Profile, Post, and SocialEvent models to facilitate location-based filtering.
- **Post**: Represents user-generated content with fields for owner, created_at, updated_at, title, content, tags, image, and image_filter. It includes a foreign key to User for ownership, a link to the Location model, and a many-to-many relationship with the Tag model for categorization.
- **Comment, Dislike**: Manage commenting and disliking on posts, each linking back to the User and the Post.
- **Follower**: Manages the relationship between users, allowing one user to follow another.
- **Like**: Manages user interactions such as liking posts, linking back to the User and the Post.
- **Question, Choice**: Represents a poll feature with questions and choices. The Question model contains the question_text and created_at fields. The Choice model contains the choice_text, votes, and users fields, with a many-to-many relationship with User for tracking user choices.
- **Tag**: Used for categorizing posts and events, featuring a simple model with just a name for each tag.


## Testing

All endpoints underwent manual testing during the development phase by accessing the URLs directly. The API was rigorously evaluated through various request types (GET, POST, PUT, DELETE) both during development and in the production environment, as initiated from the Front End Application.

### Python Linter (PEP 8)


In settings.py five instances of the 'E501 line too long' error have been identified. In these specific cases, it is considered acceptable not to break the line.

For all other files the result was "All clear, no errors found"

## Technologies used

The project is developed in Python.

### Frameworks

- Django and Django REST Framework to create the web API.

### Libraries and Packages

- Gunicorn: Used to handle web requests.
- Dj-Database-URL: Configures the database management.
- Django-CORS-Headers: Handles the server headers required for Cross-Origin Resource Sharing (CORS).
- Django Filters: Allows users to filter querysets dynamically.
- Pillow: Used for image processing.
- Psycopg2: Acts as an adapter used for database connectivity.
- PyJWT: Utilized to encode and decode JSON Web Tokens (JWT).
- Django Allauth and Dj-Rest-Auth: Used to handle user authentication, registration, and account management.
- GeoPy: Used to calculate the distance between locations.


### Database

- ElephantSQL as the PostgreSQL database used in production

### Hosting

- Heroku to host and deploy the appliocation.

### Other Technologies

- Git for version control.
- GitHub to host the code.
- Cloudinary to manage media assets.
- Gitpod as the IDE used to develop the website.
- Lucidchart to create the ERD.

## Deployment

This site has been deployed to Heroku, using ElephantSQL database and Cloudinary, following these steps:

1. Installing Django and supporting libraries

    - Install Django, Djangorestframework (and add it to installed apps in settings.py) and gunicorn
    - Install supporting database libraries: dj_database_url and psycopg2
    - Install Cloudinary libraries: dj-cloudinary-storage
    - Install Pillow
    - Create requirements file
    - Create Django project
    - Create first app
    - Add app to installed apps in settings.py file
    - Migrate changes
    - Run the server to test if the app is installed

2. Create the Heroku App
    - Log into Heroku and go to the Dashboard
    - Click “New" and then “Create new app”
    - Choose an app name and select the region closest to you. Then, click “Create app” to confirm.

3. Create an external database with ElephantSQL

    - Log into ElephantSQL
    - Click "Create New Instance"
    - Set up a plan by giving a Name and selecting a Plan
    - Click "Select Region" and choose a Data center
    - Click "Review", check all details and click "Create Instance"
    - Return to the Dashboard and click on the database instance name
    - Copy the database URL

4. Create an env.py file to avoid exposing sensitive information

    - In the project workspace, create a file called env.py. Check that the file name is included in the .gitignore file
    - Add ``import os`` to env.py file and set environment variable DATABASE_URL to the URL copied from ElephantSQL ``os.environ["DATABASE_URL"]="<copiedURL>"``
    - Add a SECRET_KEY environment variable ``os.environ["SECRET_KEY"]="mysecretkey"``

5. Upate settings.py

    - Add the following code below the path import in ``settings.py`` to connect the Django project to env.py:
        ````
        import os
        if os.path.exists("env.py"):
            import env
        ````
    - Remove the secret key provided by Django in settings.py and refer to variable in env.py instead (``SECRET_KEY = os.environ.get('SECRET_KEY')``)

    - In order to keep using the sqlite database in the development environment as well as as having Debug on, but off in production and use the ElephantSQL database, create a new variable called DEV at the top of settings.py. This means that if there's an environment variable called DEV in the environment this variable will be set to its value. And otherwise, it'll be false. 
        ````
        development = os.environ.get('DEV', False)
        ````

    - To connect to the new database for production and keep sqlite for development, replace the provided DATABASE variable with 
        ````
        if development:
            DATABASES = {
                'default': {
                    'ENGINE': 'django.db.backends.sqlite3',
                    'NAME': BASE_DIR / 'db.sqlite3',
                }
            }
        else:
            DATABASES = {
                'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
            }
        ````
    - Save and migrate all changes

6. Heroku Config Vars

    - Go back to Heroku dashboard and open the Settings tab
    - Add config vars
        - DATABASE_URL -> value of the database url
        - SECRET_KEY -> value of the secret key string
        - DISABLE_COLLECTSTATIC -> 1
        - ALLOWED_HOSTS -> value of the deployed Heroku app url

7. Set up Cloudinary for static and media files storage

    - In the Cloudinary dashboard, copy the API Environment variable
    - In ``env.py`` file, add new variable ``os.environ["CLOUDINARY_URL"] = "<copied_variable"``, without "CLOUDINARY_URL="
    - Add the same variable value as new Heroku config var named CLOUDINARY_URL
    - In ``settings.py``, in the INSTALLED_APPS list, above ``django.contrib.staticfiles`` add ``cloudinary_storage``, below add ``cloudinary``
    - Connect Cloudinary to the Django app in settings.py:

        ````
        CLOUDINARY_STORAGE = {
            'CLOUDINARY_URL': os.environ.get('CLOUDINARY_URL')
        }
        MEDIA_URL = '/media/'
        DEFAULT_SITE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
        ````

    - Add Heroku Hostname to ALLOWED_HOSTS

        ````
        if development:
            ALLOWED_HOSTS = [os.environ.get('LOCALHOST')]
        else:
            ALLOWED_HOSTS = [os.environ.get('HEROKU_HOSTNAME')]
        ````

8. Add JWT to the project
    - Install `dj-rest-auth` and `dj-rest-auth[with_social]`
    - Add to installed apps in settings.py
        ````
        'rest_framework.authtoken',
        'dj_rest_auth',
        'django.contrib.sites',
        'allauth',
        'allauth.account',
        'allauth.socialaccount',
        'dj_rest_auth.registration',
        ````
    - Install `djangorestframework-simplejwt`
    - Add authentication method to settings.py:
        ````
        REST_FRAMEWORK = {
            'DEFAULT_AUTHENTICATION_CLASSES': [(
                'rest_framework.authentication.SessionAuthentication'
                if 'DEV' in os.environ
                else 'dj_rest_auth.jwt_auth.JWTCookieAuthentication'
            )],
        }
        ````
        ````
        REST_USE_JWT = True
        JWT_AUTH_SECURE = True
        JWT_AUTH_COOKIE = 'my-app-auth'
        JWT_AUTH_REFRESH_COOKIE = 'my-refresh-token'
        JWT_AUTH_SAMESITE = None
        ````

9. Create Procfile

10. Heroku Deployment:

    - Click Deploy tab in Heroku
    - In the 'Deployment method' section select 'Github' and click 'Connect to Github'
    - In the 'search' field enter the repository name
    - Connect to link the heroku app with the Github repository
    - Click "Deploy Branch" or enable "Automatic Deploys"
