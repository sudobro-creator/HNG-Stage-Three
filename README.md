# HNG-Stage-Three
This deploys a Python application behind Nginx that interacts with RabbitMQ/Celery for email sending and logging functionality. The below architecture diagram visualizes the process: 

Setup RabbitMQ Locally
- Installation for RabbitMQ:
```

```

Install Celery
Celery is written in Python, and as such, it is easy to install in the same way that we handle regular Python packages.

We will follow the recommended procedures for handling Python packages by creating a virtual environment to install our messaging system. This helps us keep our environment stable and not effect the larger system.

Install the Python virtual environment package from Ubuntu’s default repositories:
```
sudo apt-get update
sudo apt-get install python-virtualenv
```

- Use this command to create a virtual environment and activate it:
```
python3 -m venv myenv
source myenv/bin/activate
```
- Install requirements.txt file
```
pip install -r requirements.txt
```

# Setup Log Directory
sudo touch /var/log
