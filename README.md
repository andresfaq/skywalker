# Skywalker Project
---

## How to setup the development enviroment

This project run in **(ubuntu 16.04)**

### Install Dependencies

`sudo apt-get install git python-virtualenv libpq-dev python-dev python3.5-dev libtiff5-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk postgresql postgresql-contrib`

### Create a virtual enviroment

Create the enviroment for the skywalker project

`virtualenv -p /usr/bin/python3.5 sky-env`

Activate the enviroment

`source sky-env/bin/activate`

Verify the version

`python -V`



### Clone the Repo

You can clone the repo wherever you want but we recomment to install it inside the enviroment folder (sky-env)
	
You can clone the repo Using SSH `git clone git@bitbucket.org:nezara/skywalker.git` (you need to configure the ssh key) or you can use HTTPS `git clone https://andresfaq@bitbucket.org/nezara/skywalker.git`


### Installing Django dependencies

Activate the sky-env enviroment, go to the repo folder and execute

`pip install -r requirements.txt`


### Database Configuration

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


### Execute the project

`python manage.py makemigration --settings=skywalker.settings.dev`

`python manage.py migrate_schemas --shared --settings=skywalker.settings.dev`

`python manage.py runserver --settings=skywalker.settings.dev`