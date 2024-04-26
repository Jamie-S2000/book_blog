# Jamie's Book Blog
<br>

Jamie's book blog is a small personal blog. It is designed for persnal use and for users to be able to have conversations within posts.

## Contents
- [Planning and Development](#planning-and-development)


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
The admin site allows the admin to make posts and approve comments on posts. The approval on comments is to make sure they are appropriate for the blog.
![Screenshot of Admin site](/assets/adminsite.png)

### Testing

The project has gone through extencive testing as it has been developed. Each feature was tested when it was added and later once the site was compleated. Google Dev tools was used to test the site on different size deviced during development and the site was used on phones and tablets once finished 

#### Known bugs
- above the comment crispy form there is some text that says '*body'

#### Validator Testing

##### HTML Testing

Website used to validate HTML code: https://validator.w3.org/

The errors flagged in the HTML code were from the django that it in the code.

##### Python testing

Website used to validate Python files: https://pep8ci.herokuapp.com/

The errors flagged in this were mainly line length or spaces between lines and didn't affect the project

##### Lighthouse

Lighthouse was used to est the site load:
![Screenshot of Lighthoue test](/assets/lighthouse.png)

## Deployment
