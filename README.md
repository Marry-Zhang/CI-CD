 ## Development requirements

 * If a developer were to set this up on their machine or a remote server, what are the technical requirements (e.g. OS, libraries, etc.)?

Users must install Python 3.8 and PostgreSQL.

The libraries that our back end server uses are Django, djangorestframework, django-rest-auth, django-cors-headers, psycopg, django-filter, pandas, sqlalchemy, which are recorded in requirements.txt. We describe how to install these dependencies locally down below.

 * Briefly describe instructions for setting up and running the application (think a true README).
### Setting up the Back End

#### Install Postgresql
More details can be found here: https://www.postgresql.org/download/

#### Set up Postgresql
Please use the following credentials/information:

* USER: markv
* HOST: 127.0.0.1
* PORT: 5432 
* PASSWORD: LunA9

#### Create a local database
Create a local database called “korotu”. Detailed instructions on how to create a postgresqul databse can be found on https://www.guru99.com/postgresql-create-database.html

#### Available Scripts

Under the team-project-11-korotu/django_react_proj directory (the outer django_react_proj)，you can run:

#### `pip install -r requirements.txt`

to install dependencies

#### `python manage.py runserver`

to run the backend of the application

### Setting up the Frontend 

Under the team-project-11-korotu/react_app/ project directory, you can run:

#### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits.\
You will also see any lint errors in the console.

#### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

#### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.


