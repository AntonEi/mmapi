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