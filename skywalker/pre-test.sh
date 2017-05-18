#!/bin/bash
python manage.py makemigrations --settings=skywalker.settings.dev_ci
python manage.py migrate_schemas --shared --settings=skywalker.settings.dev_ci
python manage.py shell < ../utilities/create-tenants.py --settings=skywalker.settings.dev_ci
