# Jamie's Book Blog
<br>

Jamie's book blog is a small personal blog. It is designed for persnal use and for users to be able to have conversations within posts.

Live site: https://book-blog-a67e7f179c17.herokuapp.com/

## Contents
- [Planning and Development](#planning-and-development)
- [Deployment](#deployment)
- [Languages and Frameworks](#languages-and-frameworks)
- [Credits](#credits)


## Planning and Development

### Site Objectives
- Write and display review content on books
- Give users the ability to comment on posts
- Give users the CRUD usability
- Allow the site admin to approve comments
- Allow the site admin to edit and delete posts
- Allow users to register an account, log in and log out

### Database Schema
![Screenshot of database image](/assets/tabels.png)

### Target Audience
The target audience is any book readers.

### User storys
Admin:
- As a site admin, I'd like to create, read, update and delete blog posts
- As a site admin, I'd like to be able to approve of comments on posts
- As a site admin, I'd like to log in and out of the website
- As a site admin, I'd like to be able to access the Django Admin Portal

User:
- As a site user, I'd like to be able to read posts
- As a site user, I'd like to be able to register an account and log in and out of that account
- As a site user, I'd like to be able to create, read, edit and delete comments
- As a site user, I'd like to have easy navigation of the site

### Agile
The agile methodolology was used to plan and track the project's progress. This was kept track of with GitHub's project page.

### Colour Scheme
The colour scheme used was from the 'minty' bootstrap template created by Bootswatch.

### Features

#### Nav bar
The Navbar is permanant accross the entire website allowing the user easy navigation. It allows users to:
- Go back to home
- Register
- Log in
- Log out

![Screenshot of navbar](/assets/navbar.png)
![Screenshot of navbar](/assets/navbar2.png)

It also features a dropdown menu for smaller screens:

![Screenshot of dropdown button](/assets/dropdownbutton.png)
![Screenshot of dropdown menu](/assets/dropdownopen.png)

#### Footer
The footer is also permanent across the site giving users access to linked social media sites.

![Screenshot of footer](/assets/footer.png)

#### Post List
The post list if on the home page of the site. It allows users to navigate between posts and provides a small quote from the book.

![Screenshot of post list](/assets/postlist.png)

#### Comment
The site uses a crispy form to allow users to comment on posts. These comments can be edited and deleted by the user who posted them and viewed by all the users.

![Screenshot of comments](/assets/comments.png)
![Screenshot of comments](/assets/comments2.png)

#### Registration, sign in, sign out
The site allows users to register an account so they can comment on posts. It also allows them to sign in and out once they have an account.

![Screenshot of registration](/assets/register.png)
![Screenshot of login](/assets/signin.png)
![Screenshot of logout](/assets/signout.png)

#### Admin site
The admin site allows the admin to make posts and approve comments on posts.

![Screenshot of Admin site](/assets/adminsite.png)

#### Admin Posts
The admin site allows the admin to create, edit and delete posts on the blog.

![Screenshot of post list](/assets/postlistadmin.png)
![Screenshot of post edit page](/assets/postpageadmin.png)

#### Admin Comments
The admin site allows the admin to create, edit, delete and approve comments. This is mainy to make sure all comments are appropriate.

![Screenshot of list of comments](/assets/commentlistadmin.png)
![Screenshot of comment page](/assets/commentpageadmin.png)

### Testing

The project has gone through extencive testing as it has been developed. Each feature was tested when it was added and later once the site was compleated. Google Dev tools was used to test the site on different size deviced during development and the site was used on phones and tablets once finished

Here is the full documentation: [Testing](/TESTING.md)

#### Known bugs
- above the comment crispy form there is some text that says '*body'

#### Validator Testing

##### HTML Testing

Website used to validate HTML code: https://validator.w3.org/

The error in the HTML code on the sign up page is from a 3rd party source and cannot be changed. Other than this all pages passed the HTML validator test.

##### Python testing

Website used to validate Python files: https://pep8ci.herokuapp.com/

The errors flagged in this were mainly line length or spaces between lines and didn't affect the project

##### Lighthouse

Lighthouse was used to test the site load:

![Screenshot of Lighthoue test](/assets/lighthouse.png)

## Deployment
The site was deployed to Heroku and uses ElephantSQL for the database.

### ElaphantSQL

A database was created with SQL:
- Select 'Create New Instance'
- Give a database a 'name' and select a plan
- Click ' Select Region', choose your region and then click 'Review'
- Cick on your recently created instance
- Copy the database URL. This will needed to be inserted in the GitHub repository under 'settings.py' and in Heroku

### Heroku
- click "New" then "Create new app".
- Create a unique app name , select the correct region and create app.
- This will direct you to the deploy tab.
- Navigate to settings.
- Go to the Config Vars section, click add and add with:
- config var named 'SECRET_KEY' and create a secret key for this
- config var names 'DATABASE_URL', this will use the ElephantSQL url
- Once this is done navigate to deploy.
- Select GitHub as your deployment method.
- Search for the repository and select it to connect.
- select the deployment type you would like to use and deploy.

### env.py
In the project create an env.py file in the root directory.
The elephantSQL database URL should be used as the DATABASE_URL
A secret key should be pasted as the SECRET_KEY value, this does not need to be the same as the Heroku one.

### settings.py
In settings.py add:
```
from pathlib import Path
import os
import dj_database_url
if os.path.isfile('env.py'):
    import env
```

### Final Steps
- Link file to the templates directory in Heroku, place under BASE_DIR:
```
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
```

- Change the template direcory to TEMPLATES_DIR and place in templates array:
```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

- Add heroku to the ALLOWED_HOSTS:
```
ALLOWED_HOSTS=["project_name.herokuapp.com", "localhost"]
```

- create static and template files at the top leavel of the directory

- create a Profile and add:
```
web: gunicorn project_name.wsgi
```

### Final Heroku deployment
- **Make sure debug is set to 'False'**
- click deploy
- deploy branch

## Languages and frameworks
The languages and framewokrs used are:
- HTML
- CSS
- Python
- Django
- Bootstrap

## Credits
- https://bootswatch.com - minty style used in the blog
- https://fontawsome.com - socialmeda icons