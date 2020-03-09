# AWSInventoryTool

'Quick glance' AWS infrastructure without need to login into AWS web console

# Running tool

Application is writen in Python, using Django framework, hence no specifics to run application, except installing required packages:
```
pip install -r requirements.txt
```
or

```
pip install django
pip install django_tables2
pip install boto3
```

Application can be started by triggering following command in project folder:
```./manage.py runserver 0.0.0.0:80```

# Accessing tool
http://<ip_of_your_docker_host>:8000

# Configuration
Configuration is stored in config.ini where cloud access information is saved. Multiple accounts can be added to application configuration file at .\backend\config.ini

Example of config file:
```
[AWS-Account-1]
region_name=eu-west-1
key_id=my_aws_account_key_id
secret=my_aws_account_secret_string

[My another aws account]
region_name=eu-west-1
key_id=my_another_aws_account_key_id
secret=my_another_aws_account_secret_string
```

Each section name (text in brackets) will appear as a radio button choice in WEB GUI, meanwhile rest of the data in "section" serves as a prerequisites to reach out AWS for an information.

# AWS permissions
In order to allow boto3 read information in your AWS account, following permission policies must be assigned to an account, defined in config.ini:
AmazonEC2ReadOnlyAccess
AmazonRoute53ReadOnlyAccess
AmazonRDSReadOnlyAccess

# Tests

Unit and integration tests stored in ./tests folder and can be triggered with command:
```python ./manage.py test tests/```

Coverage can been measured with coverage.py:

```pip install coverage```

Run for a report:
```
coverage run --omit=*/migrations/*  --omit=*/tests/* manage.py test tests/
coverage report -m
```
or
```
coverage html 
```

for more friendly format of a report


# More information:
https://coverage.readthedocs.io/en/coverage-5.0/

https://www.djangoproject.com/

https://django-tables2.readthedocs.io/en/latest/

https://aws.amazon.com/iam/features/manage-permissions/
