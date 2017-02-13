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

(In progress ..)