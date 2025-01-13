# Testing

All web page Testing was conducted on an iMac (safari, Google Chrome), Windows Laptop (google Chrome, Microsoft Edge), Samsung Tablet (Google Chrome and Samsung internet) and Samsung Phone (Google Chrome and Samsung Internet). This was to make sure all features worked on different operating systems and screen sizes.
The Admin testing was done on an iMac and was done to check the database functionality.

## Web Page testing

### Nav Bar:

**Nav bar links:**
Expected - when a user clicks each link, the links take the user to the desired web page (Home, Register, Login and Logout)
Test - by clicking the link to each page
Result - the feature acted normally and directed the user to the desired page

**Nav bar links when signed in/signed out**
Expected -  when the user is signed out, the nav bar should display Register and Login, when the user is signed in the nav bar should display Logout
Test - check the navbar links are correct when signed in and signed out
Result - the feature works as expected and displays the correct links when signed in and signed out

**Nav bar dropdown:**
Expected - on smaller screens, a dropdown button is displayed instead of the full menu. When the user presses the dropdown button, the nav bar displays a drop-down menu
Test - by viewing on a smaller screen and clicking the dropdown button
Result - the feature did not respond due to Bootstrap 4 being used in the HTML while the site was using Bootstrap 5
Fix - HTML was updated to Bootstrap 5 and now works

### Social links

Expected - when user clicks a social link, each social link would open the appropriate website in a new tab
Test - Clicked each social link
Result - the feature worked normally and all social links open the correct website in a new tab

### Blog Post Links

Expected - when the users click a blog post, the user would be presented with the relevant post 
Test - clicked each blog post
Result - the feature worked normally and each blog post displayed the correct post

### Register Page

**Register a new user**
Expected - when the user fills out the sign-up form correctly, the user creates a new user
Test - form filled out correctly: unique username, with and without email, a password within the rules and the password repeated exactly
Result - the feature worked normally, and a new user was created

**Repeated username**
Expected - when the user fills out the sign-up form with a username that is already in use, the form should not allow a new user to be created and ask for a unique username
Test - enter a username already in use
Result - the feature worked normally and tells the user “A user with that username already exists.”

**Password not following rules**
Expected - when the user fills out a sign-up form correctly but uses a password breaking the rules, the form should not allow the user to be created and will tell the user what they need to do for the password
Test - fill out the form correctly breaking each password rule in turn
Result - the feature worked as expected and tells the user what they need to do to change the password

**Password Repeated incorrectly**
Expected - when the users fills out the form correctly but does not repeat the password correctly, the form should not create the new user and ask them to re input the passwords
Test - fill out the form correctly, using different values for the passwords
Result - the feature worked as expected and advised the user of the  password error

### Sign in page

**Sign in**
Expected - when the user signs in with the correct information, the user will be signed in and redirected to the home page
Test - fill out the form with a registered username and correct password
Result - the feature worked as expected, signed in the user and redirected to the home page

**Unregistered username**
Expected - when the user attempts to sign in with an unregistered username, they should not be signed in and be asked to input the correct username
Test - fill out the form with an incorrect username
Result - the feature worked as expected, informed the user the username or password is incorrect

**Incorrect password**
Expected - when the user inputs a correct username and incorrect password, they should not be signed in and asked to input the correct password
Test - fill out the form with a correct username and incorrect password
Result -  the feature worked as expected, informed the user the username or password is incorrect

**Sign up link**
Expected - when the user presses the sign up link, they should be redirected to the sign up page
Test - click on the sign up link
Result -  the feature worked as expected and redirected the user to the signup link

### Logout Page

Expected - when the user clicks the sign out button while signed in, they should be signed out
Test - while signed in, click the sign out button
Result -  the feature worked as expected and signs the user out

### Comments

**Submitting comments**
Expected - when the user submits a comment, they should be able to see the comment, edit and delete it and see a message that says, “This comment is awaiting approval”. Other users should not be able to see this comment until it is approved.
Test - Write a comment and submit it, check it as both the user who wrote it and another user who didn’t
Result - feature works as expected, the user who submitted the comment can see it, edit and delete it, and see the awaiting approval message, other users cannot see the comment.

**Editing comments**
Expected - when the user presses edit, the comment should show in the text box to be edited and submit should change to update, once the comment has been updated the post should show the new comment and should need approval
Test - press edit, edit a comment and press update
Result -  the feature works and expected, the comment shows as edited to the user but needs approval again

**Deleting comments**
Expected -  when the user presses delete comment, a pop up should show and ask for confirmation. When the user presses close the pop up should close and when the user presses delete the comment should delete
Test - press delete on a comment, press close then press delete and press delete on the pop up.
Result -  feature works as expected, pressing delete shows a pop up and when the user presses close, it closes and when the user presses delete it permanently deletes the comment

## Admin Testing

### Login

**Admin sign in**
Expected - when the user signs in as an admin on the admin sign in, they are redirected to the Django administration home page
Test - on the admin site, sign in with the correct username and password
Result - feature works as expected and allows admin to sign into Django Administration

**User sign in**
Expected - when a regular user tries to sign into the admin page, the user should not be allowed to sign in
Test - on the admin site, attempt to log in as a basic user
Result - feature works as expected and the user is asked to sign is as an admin account

##### Posts

**Post creation**
Expected - when ‘ADD POST +’ is clicked, a new post should be created
Test - click on ‘ADD POST +’
Result - Feature works as expected and creates a new post

**Saving posts**
Expected - when the user clicks save, the post should not be saved until all of the required fields are filled 
Test - fill out all fields and delete one required one and attempt to save, repeat this for each required field
Result - feature works correctly and will not allow the user to save until each field is filled out

**Draft Posts**
Expected - when a post is written but kept as a draft and saved, it should not show on the blog site but be saved on the admin site
Test -  write a new post, keep the status as draft then save the post
Result - the feature works as expected and does not show on the blog site when saved as a draft

**Published posts**
Expected - when a post is written, published and saved, it should show on the blog site to all users
Test -  write a new post, set the status as published then save the post
Result - the feature works as expected and shows on the blog site when saved as published

**Editing posts**
Expected - when a post is edited and saved the new edited post should show on the site and be saved to the database 
Test - edit each element on a post and save the post
Result - the feature works as expected and the database and site updates with the new post

**Deleting posts**
Expected -  when the delete button is pressed on a post, the user should be redirected to a confirmation page, when the user clicks to confirm the post should be deleted
Test - press delete on the post that the user wants deleting, then confirm
Result -  the feature works as expected and removes the post from the database and site

### Comments

**Comment approval**
Expected - When a comment is approved, it should show on the site under the post the comment was written for
Test - click approve on a user comment
Result -  the feature works as expected and shows the comment under the correct post
