from flask import Flask, request
from tasks import send_email, log_time

app = Flask(__name__)

@app.route('/')
def main_route():
    if 'sendmail' in request.args:
        email = request.args.get('sendmail')
        send_email.delay(email)
        return f"Email to {email} has been queued."
    elif 'talktome' in request.args:
        log_time.delay()
        return "Current time logged."
    else:
        return "No valid query parameters provided."

@app.route('/logs')
def get_logs():
    try:
        with open('/var/log/messaging_system.log', 'r') as log_file:
            log_content = log_file.read()
        return f"<pre>{log_content}</pre>"
    except Exception as e:
        return f"Error reading log file: {e}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)