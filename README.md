# Footie 365

Footie 365 is a web application blog designed for visitors to read reviews on recent high profiled football matches, comment on these matches and for users to interact with each other. Inspirational came from sports news sites, reddit and to a small extent Pintrest. 

Visitors to the site can read the reviews and there is a call to action with the register / sign up button on the top navigation bar of the site, where they will be taken to the sign up form requesting a username and password as mandatory fields with an option email address. After registering an creating an account the user can then proceed to log into the site and enjoy full benefits of becoming a member such as the ability to comment on the posts on the site, like or unlike posts and also the ability to interact with other members of the site in the comments section.

Users already registered can login upon landing on the homepage, which is a tidy grid of "match cards", containing a title and in some reports a sub-title underneath. The user can click to take them into the full macth report page where they have a form on the page to leave their comment. It is also where the user can like or unlike a match report. The User can create a comment, read other comments and the report, after liking a post if the user decides they've changed their mind they can update their like by unlikng a post.

************
Insert my mock up pic here last minute


*********

Footie365's live sit can be found here : [Footie365](https://     )

# Table of Contents
- [User Experience](#user-experience)
- [Features](#features)
  - [General](#general)
  - [Website Pages](#Website-pages)
  - [Registration](#accounts)
- [Design](#design)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)

# User Experience

### User Stories

- As a Site User I can view the home page where I can see the site's goal and also be encouraged to sign up
- As a Site User I can register for an account so that I can then log in to gain access to the site's features
- As a Site User I can log in and therefore I can gain access to the site's features
- As a Site User I can Log Out meaning someone else log in on my computer, change accounts or leave myself signed out on public devices
- As a Site User I can view the Home page when logged in so that I can view recent match reports
- As a Site User I can navigate betweens the different pages of blog reports

- As a Site Administrator I can view administrator features so that I can add, edit and remove match reportson  the site
- As a Site Administrator I can view the blog CRUD forms so that I can create, add, edit and remove reports from the site
- As a Developer I can create a model for the match report database so that it is available for administrators to add new match blog reports and reviews


# Features
## General
### Navigation Bar

<details>
<summary>Navbar</summary>

![Navbar](readme-docs/site-images/navbar.jpg)
![Navbar](readme-docs/site-images/navbar-loggedin.jpg)
![Navbar](readme-docs/site-images/admin-navbar.jpg)
</details>

The site's navigation bar is featured across all pages.

The navigation bar displays "Home", "Login" and "Sign Up" for all unregistered visitors to the site as well as to registered members who are logged out. When viewing the site on a smaller screen such as on a mobile, the navibar collapses froma  list to a hamburger menu which when clicked toggles the list in and out of view for the user.

When a regsitered user is logged into the site they will see both the home page and logged out option on the navbar.

This narbar is based on "navbar-expand-lg navbar-light bg-white" from Bootstrap.

The logo can also be seen on the navbar and when clicked from any part of the site will always bring the user quickley back to the home page, as it's an index page link. This logo was made with Designevo's Logo generator, details of which are discussed further down this report.

### Footer

<details>
<summary>Footer</summary>

![Footer](readme-docs/site-images/footer.jpg)
</details>


Just like the navbar, the footer is featured across all of the site's pages. It contains social media icons which are also clickable links to their respected site's homepage. When Footie365 moves on from the MVP stage these will take the user to proper social media pages of Footie365. Here in the footer the user can also see that the site is currently just for educational purposes only.

## Website Pages


### Index Page

<details>
<summary>Home Page Unregistered</summary>

![Index Page](readme-docs/site-images/index.jpg)
</details>

<details>
<summary>Home Page Logged In</summary>

![Index Page](readme-docs/site-images/home.png)
</details>

Depending on the type of user viewing the index page it can have two different states (Logged in / Logged Out).

New users to the site, and users who are logged out, will see a batch of card blogs on display on the home page. These are neatly and clearly laid out and the user can instantly recognise what kind of a site Footie365 is upon landing on the home page, incase they hadn't already gussed form the site's name and the images used for each blog report on the home page. Layered over these images is a container banner stating who wrote the blog and underneath the image is the match's scoreline for both teams and this is a clickable link which will take the user to a new page where they can read the full match report.

All of these pages as well as the home page are responsive and will displays different amounts of match report cards on screen depending on the size of the user's device, such as 3 blog reports on a wide desktop screen or 1 single report one underneath another ona  smaller mobile device screen.

### Individual Match Blog Reports

<details>
<summary>Match Reports</summary>

![Match Reports](readme-docs/site-images/matchreports.jpg)
</details>

When a iser clicks ona  match title on the home page they will be taken to a new page with the full blog report write up for that specific game. 

For users who are registered and are logged in they can interact with this match report content by liking or unliking the blog reports. Logged in users can also interact with other users here by commenting on blog reports.
These pages are also repsonsive and will change to suit the user's device screen width. All content is contered to keep a good design look to the site.

## Accounts

### Registration Page

<details>
<summary>Registration Page</summary>

![Registration](readme-docs/site-images/signup.jpg)
</details>

Through the call to action 'Sign Up' link on the navbar users can access the registration page, where they can create an account. The sign up form has been kept as simple as possible so as not to discourage users from signing up. The user is asked to create a username, a password which they must repeat to make sure they have entered it correctly, and also an optional email address.

When a user creates an account they are automatically taken to thehome page where they can seee that they are now logged in as the login option will have changed to logout.

### Login Page

<details>
<summary>Login Page</summary>

![Login](readme-docs/site-images/sign.jpg)
</details>

The user can find the log in page by clicking the link in the navbar. The user will be presented with a simple form requesting their username and password.

After the user successfully logs in they will be taken back to the index page again where they can choose which match report blog they would like to view.

![Logout](readme-docs/site-images/logout.jpg)
</details>

When the user is finished on the site they can choose to log themselves out of the site with the call to action link button on the navbar "log out". This will bring the user to a log out form where after logging out successfully they will be once again brought back to the home page.

## Admin Panel

### Admin Panel

<details>
<summary>Admin Panel</summary>

![Admin Panel](readme-docs/site-images/adminpanel.jpg)
</details>

###############

Fill out this section later

### Create Comment

<details>
<summary>Create Comment</summary>

![Create Meal](readme-docs/site-images/create-comment.png)
</details>



#######################################

















#############################################

# Deployment
## Steps to deploy the site using Heroku:
- After having installed the foloowing; psycopg2, dj3-cloudinary-storage, dj_database_url and gunicorn
- Use the Heroku dashboard to select "New" and then click to "Create a new app"
  - Must create app with a new unique name - this then needs to be added in the project settings to allow hosts
  - Select your specific region
  - Then click to "Create app"
- Next, go to the Resources tab:
  - In the add-ons search bar search for 'postgres' and then select 'Heroku Postgres'
  - Then click to 'Submit order form'
- Next go to the settings tab
- In the 'Config Vars' section select 'Reveal Config Vars'
- P



#########################################################


Colour theme is from shutterstock
https://www.shutterstock.com/blog/sports-color-palettes-branding-marketing
colours used:

#97FB57 (a bright green)
#121212 (a dark grey / light black)
#909090 (a grey)
#F6F2F2 (a baige colour)



Images taken from BBC Sport's website. Match review content also taken from BBC sport but rewritten by myself for the purposes of this project.


Logo created with Designevo's Logo generator at https://www.designevo.com/apps/logo/?name=black-and-white-football-icon