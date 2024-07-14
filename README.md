# Messaging System with RabbitMQ, Celery, and Python Application Behind Nginx
<h3>HNG-Stage-Three</h3>
This project implements a messaging system using RabbitMQ and Celery for task queuing and a Python Flask application. The application is deployed behind Nginx and includes functionalities for sending emails and logging events. The logs can be viewed directly via an HTTP endpoint.

# Table of Contents
- Features
- Requirements
- Setup
    - Local Environment Setup
    - Nginx Configuration
    - Expose Local Server with ngrok
    - Expose External Server with ngrok
- Usage
- Enpoints
- Contributing
- License

# Features
- Send emails asynchronously using Celery and RabbitMQ.
- Log events to a file and access them via an HTTP endpoint.
- Deployed behind Nginx for production readiness.
- Expose local development server using ngrok for external access.

<h3>Create Python Application</h3>
This application has two functionality: <br>

- Send Mails: It allows you to send mails to the specified email address using this command `/?sendmail=fakeemail@mail.com` after your domain. CThe email is sent in the background using Celery. Celery has been configured to use RabbitMQ as its message broker. It generates an email message, connects to a Gmail SMTP server, logs in, and sends it. <br>

- Logs Time:
  
**Setup Log Directory**
```
sudo touch /var/log/messaging_system.log
sudo chmod 666 /var/log/messaging_system.log
```


# Requirements
- Python3
- RabbitMQ
- Celery
- Flask
- Nginx
- ngrok (for external access)


# Setup
<h3>Local Environment Setup</h3>

1. Clone the repository:
```
git clone https://github.com/yourusername/messaging-system.git
cd messaging-system
```
<br>

2. Create and activate a virtual environment:
- Install the Python virtual environment package from Ubuntu’s default repositories:
```
sudo apt-get update
sudo apt-get install python-virtualenv
```
- Use this command to create a virtual environment and activate it:
```
python3 -m venv myenv
source myenv/bin/activate
```
<br>

3. Install and start RabbitMQ locally:

  - Follow the instructions to install RabbitMQ. <https://www.rabbitmq.com/docs/install-debian> <br>
<br>


4. Install dependencies:
```
pip install -r requirements.txt
``` 
<br>

5. Nginx Configuration <br>
- Install Nginx on your local machine and replace the default `nginx.conf` file with the one provided in this repository. This allows Nginx to route requests from `localhost:5000` to where the flask app will be running.
```
sudo apt update
sudo apt install nginx
```
- Create an Nginx configuration file:
```
server {
    listen 80;
    server_name localhost;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```
- Enable the site and restart Nginx
```
sudo ln -s /etc/nginx/sites-available/messaging_system /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```
<br>

6. Setup Ngrok

It is used to expose our local development server to the Internet with minimal effort. The software makes your locally-hosted web server (like computer, laptop, rasbery PI) appear to be hosted on a subdomain of ngrok.com, meaning that no public IP or domain name on the local machine is needed.
- Install ngrok via Snap with the following command:
```
 sudo snap install ngrok
```
- Run the following command to add your authtoken to the default ngrok.yml configuration file.
```
ngrok config add-authtoken <token>
```
- Expose your local server:
```
ngrok http 80
```

- Use the static domain provided to access your application externally. You can create a free static domain from your ngrok dashboard under the setup tab.

![Screenshot from 2024-07-14 08-32-24](https://github.com/user-attachments/assets/52612cdd-3959-413e-ab9e-3735405c06b6)

- Copy and paste the command in your terminal
```
ngrok http --domain=slug-verified-airedale.ngrok-free.app 80
```

# Usage
1. Send an email:
```
curl http://localhost:5000/?sendmail=fakeemail@mail.com
```

2. Log the current time:
```
curl http://localhost:5000/?talktome
```

3. View the logs:
```
curl http://localhost:5000/logs
```
Repeat the same for your external domain, replacing localhost with your static domain.

# Endpoints
- / - Main route with parameters `sendmail` and `talktome`.

  - `sendmail` - Sends an email using Celery and RabbitMQ.
    <br>
  ![Screenshot from 2024-07-14 10-15-56](https://github.com/user-attachments/assets/d5010c38-c924-42fc-9187-ddc63950d580)
    <br>
  ![Screenshot from 2024-07-14 10-23-02](https://github.com/user-attachments/assets/9b297323-9f56-49d8-863f-994cfd8ce97b)


  - `talktome` - Logs the current time.
    <br>
  ![Screenshot from 2024-07-14 10-17-31](https://github.com/user-attachments/assets/5a634aa8-41db-4f7d-9b9c-e5068666f1ff)
    <br>
  ![Screenshot from 2024-07-14 10-24-26](https://github.com/user-attachments/assets/f4945bf5-4abc-44d6-8d95-cee883a9c04e)


- `/logs` - Displays the contents of the log file.
  <br>
![Screenshot from 2024-07-14 10-19-13](https://github.com/user-attachments/assets/8139f264-de66-401e-b7cc-10f443c3f608)
  <br>
![Screenshot from 2024-07-14 10-25-16](https://github.com/user-attachments/assets/2c1f0786-3170-4d6c-9728-3a6b0ef05e75)

- You can also access your ngrok dashboard at `http://localhost:4040/inspect/http`
  <br>
![Screenshot from 2024-07-14 10-27-40](https://github.com/user-attachments/assets/d8ee1b15-d24f-47b5-a465-023d20007c4c)


# Contributing
Contributions are welcome! Please fork the repository and submit a pull request for review.


# License

This project is licensed under the MIT License.
