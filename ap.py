import os
from flask import Flask, request, render_template
from flask_mail import Mail, Message

app = Flask(__name__)

# Configure mail using environment variables
app.config['MAIL_SERVER'] = 'smtp-mail.outlook.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
mail = Mail(app)

@app.route('/')
def index():
    return render_template('form.html')  # Ensure you have a 'form.html' file with your form

@app.route('/submit_form', methods=['POST'])
def submit_form():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    location = request.form.get('search-keyword', 'Not specified')

    msg = Message("New contact from {}".format(name),
                  sender=app.config['MAIL_USERNAME'],
                  recipients=["recipient@example.com"])
    msg.body = f"Name: {name}\nEmail: {email}\nLocation: {location}\nMessage:\n{message}"
    mail.send(msg)

    return "Thank you for your message."

if __name__ == '__main__':
    app.run(debug=True)
