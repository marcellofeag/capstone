Thanks for reviewing my Project, please test the following routes that i've planned for the "Grading Criteria Overview"
Please turn on the MYSQL80 service

--!!Please use this token for the user "testuser" on Insomnia: 417a7ed815ff3be941f3d464819e97bbac7127c5

Q1. Does the web application use Django to serve static HTML content?
http://127.0.0.1:8000/restaurant/
Shows basic static HTML content from the restaurant, if not please authenticate as shown in QUESTION 4.

Q2. Has the learner committed the project to a Git repository?
https://github.com/marcellofeag/capstone

Q3. Does the application connect the backend to a MySQL database?
Yes, so remember to turn on the MYSQL80 service on Windows

Q4. Are the menu and table booking APIs implemented?
http://127.0.0.1:8000/restaurant/api/menus/              GET, POST
http://127.0.0.1:8000/restaurant/api/menus/1/            GET, PUT, PATCH, DELETE,
http://127.0.0.1:8000/restaurant/api/bookings/           GET, POST
http://127.0.0.1:8000/restaurant/api/bookings/1/         GET, PUT, PATCH, DELETE,

BROWSER: First login in http://127.0.0.1:8000/admin/  with user:admin pass:admin, then feel free to test.

INSOMNIA: Use the given token in Insomnia to test this routes, the general view of these tables and the single view for instances.
You can also add or delete information, there's only one object for each table, with id=1, as shown in the routes.

Q5.Is the application set up with user registration and authentication?
http://127.0.0.1:8000/restaurant/api/users/     POST new user registration

Yes, you can't visit specific routes if you're not authenticated.
For admin user, password admin
For testuser user, token 417a7ed815ff3be941f3d464819e97bbac7127c5
If you create a new user and want a token, use the admin interface or 
POST a JSON form with the user and its password to http://127.0.0.1:8000/restaurant/api-token-auth/

Q6.Does the application contain unit tests?
Yes, in capstone/littlelemon/test_models.py there's a runnable test.

Q7.Can the API be tested with the Insomnia REST client?
Yes, the user testuser has the token 417a7ed815ff3be941f3d464819e97bbac7127c5
All the routes are working in Insomnia when you're authenticated with a token.