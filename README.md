# Authentication System for User Login and Registration
## Complete Implementation of User Registration and Login using Django Framework
### Description:
There are four views: index, login_view, register, and logout_view. The index view simply renders the index.html template.

The login_view view handles user login. If the request method is POST, it takes the username and password from the request and tries to authenticate the user with Django's built-in authenticate() function. If the user is authenticated, the view logs in the user and redirects them to the home page. If the user is not authenticated, the view renders the login.html template with a message indicating that the login failed.

The register view handles user registration. If the request method is POST, it takes the username, password, and confirmation password from the request. It checks that the password and confirmation password match, then tries to create a new user in the User model with the given username and password. If the username is already in use, the view renders the register.html template with a message indicating that the username is already registered. If the user is successfully created, the view logs in the user and redirects them to the home page.

The logout_view view simply logs out the user and redirects them to the index page.

The home view renders the home.html template, which is the main page of the website after the user has logged in.
