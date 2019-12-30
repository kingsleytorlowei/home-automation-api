# HOME AUTOMATION API

A submission by Kingsley Torlowei


Features:

* Django
* Celery
* Heroku compatible

* data model (including admin pages) for `Room`,`Sensor`, `Light`, `Thermostat`,  `Attribute` (numerical observations with units), and `PowerStatus` (boolean  of on/off status)

* placeholder tasks to interact with devices (`pull_attributes`, `set_status`, etc)
* management commands to run tasks on the command line (or via Heroku Scheduler, cron, etc)

* celery infrastructure to schedule and run periodic background tasks

* tests

# How to Run 
## RabbitMQ
You should start by installing and running the [RabbitMQ (amqp) backend]([https://www.rabbitmq.com/download.html](https://www.rabbitmq.com/download.html)) with celery as a backgroud service:
``` 
rabbitmq-server
```
 I used this service because of the asynchenous nature of the project. I'm also using it to monitor the state changes in the sensor.
 
 ## Django 
 ```
 
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
 ```
## Runserver
```
python manage.py runserver 8100
```
If you navigate to [http://localhost:8100/admin](http://localhost:8100/admin), you should be able to sign in using your superuser account and see admin pages for the `Room`,`Sensor`, `Light`, `Thermostat`,  `Attribute` models.
