## API Docmentation 

The API can be accessed at `http://15.206.92.229/` and has the following endpoints.

1. `/bank/list/` : Lists all Banks and their IDs
2. `/bank/<bank_id>/` : Get the bank with a given Bank ID
3. `/bank/<bank_id>/branches/` : Get all the branches for the given Bank ID
4. `/branch/list/` : Get the list of all branches
5. `/branch/<branch_ifsc>/` : Get the details of a branch based on the IFSC code.

## API Creation

Here are the steps I followed to create this API for the assignment

### 1. Setting up a PostgreSQL database.

I decided to use an RDS instance from AWS for the database, as setting up a database wasn't in the scope of the assignment.
Then ran the SQL file to create all the entries.

`psql <db credentials> < indian_banks.sql`

### 2. Django installation and setup

Created a Python virtual environment for DRF and installed the `django`, `djangorestframework` and `psycopg2` packages.

`pip install django djangorestframework psycopg2`

and then created a Django project and app.

 `django-admin startproject bankapi`
 
 `python manage.py startapp api`

After that, I added the `api` app to `INSTALLED_APPS` and configured the database credentials (replaced with garbage values in the repository for security).

### 3. Django Models and Migrations

Since we were using an existing database, I could just use the `inspectdb` command provided by Django to inspect the database and generate models.

`python manage.py inspectdb > models.py`

Once that's done, we will apply the migrations.

`python manage.py makemigrations`

`python manage.py migrate`

### 4. Making the API

First, we create `serializers.py` and create serializers for both the db tables.

Next, we import those serializers into `views.py` and create a view for every endpoint.

Lastly, We import those views into `urls.py` and create the URL endpoints. Then we add this URL endpoint to the `bankapi`'s `urls.py` and the API is ready.

[Note: I also added pagination to the API since the number of branches is around 128,000. Which causes extremely long load times and out-of-memory errors.]

### 5. Running the API Server.

I have hosted the API Server on an EC2 instance for convenience. You can access it at `http://15.206.92.229/` (HTTP only).

`python manage.py runserver 80`
