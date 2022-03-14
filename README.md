# dfecloud3project

1. Requirements
A web application is required to allow a school science department staff to track the chemicals and equipment stored in the school.  The development currently implements a small part fo the required functionality.

3. User Stories
The following user stories were generated from the requirements.

As a user, I want to add a new location, so I know I have storage locations available

As a user, I want to view the storage locations, so I know which locations I have available for storage

As a user, I want to add new items and how many of them there are to a storage location

As a user I want to be able to view what I have stored in each storage location

As a user I want to be able to identify if an item is a chemical

As a user I want to be able to remove items from a location when they have been consumed or discarded

As a user I want to be able to adjust the quantity of an item in a location when some of it has been used or discarded


2. Database Design
The database entity relationship diagram shows a one to many relationship between the storage locations and the equipment and chemicals stored in the location

![image](https://user-images.githubusercontent.com/21013217/158126146-f4792994-240d-4a5b-b9bf-6fe81fc8cfc3.png)

2. Documentation

3. Feature Branches

A repository was set up in GitHub which was used as the version control system (VCS) for the project.  The repository was added to a GitHub project and an automated kanban style board was initiated in GitHub to record user stories as issues to be worked on.

A feature branch model was used to develop the features for application.  Each user story was raised as an issue in GitHub project and the feature branches were created as branches of dev, itself a branch of main, with the naming convention "feature/(GitHub issue number)-short-description".  For example "feature/3-create-items".
