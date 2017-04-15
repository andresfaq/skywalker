# Skywalker Project
---

## How to contribute to the project

![Untitled Diagram.png](https://bitbucket.org/repo/MyGzrq/images/1091835688-Untitled%20Diagram.png)

### Repositories
##### Origin (Bitbucket)

This is our main repository, here is the code that will be in our production server. It will contain two branches, **Integration** branch that contain the new code that will be tested and then move to the **Master** branch that contains the code that will be in our production server.

#### Fork (Bitbucket)

This is a copy of the **Origin** repository, here you will push your story branches from your local repository and then you will create the pull request from your story branches against the integration branch in the Origin repository

#### Your Repo (Local Machine)

Here you will be working in your code, you can do whatever you want, just remember create an independent branch for each user story that you work, then when you finish your work push the branch to your fork repository so you can create the pull request against the integration branch


## How to setup the development enviroment

This project run in **(ubuntu 16.04)**

### Update and Install Dependencies

`sudo apt-get update`

`sudo apt-get install git python-virtualenv libpq-dev python-dev python3.5-dev libtiff5-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk postgresql postgresql-contrib libjpeg-dev build-essential libssl-dev libffi-dev`

### Create a virtual enviroment

Create the enviroment for the skywalker project

`virtualenv -p /usr/bin/python3.5 sky-env`

Activate the enviroment

`source sky-env/bin/activate`

Verify the version

`python -V`


### Fork and Clone

Create a fork of the project


You can clone the repo wherever you want but we recommend to install it inside the enviroment folder (sky-env)


**Clone the origin repo**

You can clone the repo Using SSH
(you need to configure the ssh key in bitbucket)

`git clone git@bitbucket.org:nezara/skywalker.git`

**Add a remote for your fork repo**

you can add a remote in your local machine using this commmand

`git remote add fork git@bitbucket.org:USERNAME/skywalker.git`


### Installing Django dependencies

Activate the sky-env enviroment then go to the repo folder and execute

`pip install -r dev.txt`

this will install all the base and the development requirements that you need to work


### Database Configuration (PostgreSQL)

Ìnstall pgadmin3 (optional)

`sudo apt-get install pgadmin3`

create a database named skywalker

`sudo -u postgres createdb skywalker`

Change the password for the user postgres (or any other you have)

`sudo -u postgres psql`

`ALTER USER postgres WITH SUPERUSER;`

`ALTER USER postgres PASSWORD 'newpassword';`

configure the pgadmin3 connection with the user and the password that you create


![pgadmin.png](https://bitbucket.org/repo/jqbXE8/images/663939298-pgadmin.png)

### Configure the settings

Go to the settings folder  ( /skywalker/skywalker/settings/ ) then make a copy of the dev.py.example and rename it with the name dev.py

This is the content of each file:

**base.py**: contain the base settings that are shared in the development and the production enviroments

**dev.py**: contain the specific settings for the development enviroment

**prod.py**: contain the specific settings for the production enviroment


### Execute the project

Create the migrations files

`python manage.py makemigration --settings=skywalker.settings.dev`

Create the tables

`python manage.py migrate_schemas --shared --settings=skywalker.settings.dev`

create-tenants.py will create some example tenants (public and a tenant named 'tenant')

`python manage.py shell < ../utilities/create-tenants.py --settings=skywalker.settings.dev`

run the development server

`python manage.py runserver --settings=skywalker.settings.dev`


### Extras

#### Reset Database
To delete and create again the skywalker database in your local machine, please execute the script **resetdb.sh** that its located in the **utilities** folder

NOTE: *It only works if your database is named skywalker and you are using the postgres user*