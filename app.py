from flask import Flask, render_template, request
import os
from cryptography.fernet import Fernet
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = Flask(__name__)

# Load the encryption key securely (you may fetch it from environment variables)
key = b'1xdXT3tj7uk5K9RZvO-ze6PgWAoHo1rrxgfZC7VS0nI='

# Decrypt the email password
def decrypt_password(encrypted_password):
    cipher_suite = Fernet(key)
    return cipher_suite.decrypt(encrypted_password.encode()).decode()

# Function to send email
def send_email(sender_email, recipient_email, subject, message):
    # Configure SMTP server settings
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587  # Port for TLS (587 is commonly used)
    smtp_username = 'tokaibrian@gmail.com'
    
    # Decrypt the encrypted app-specific password
    encrypted_password = os.getenv('ENCRYPTED_APP_PASSWORD')
    smtp_password = decrypt_password(encrypted_password)

    # Create a MIME message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Add message body
    msg.attach(MIMEText(message, 'plain'))

    try:
        # Connect to SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Enable TLS encryption
        server.login(smtp_username, smtp_password)  # Login to SMTP server

        # Send email
        server.sendmail(sender_email, recipient_email, msg.as_string())
        print("Email sent successfully!")

    except Exception as e:
        print("Error sending email:", e)

    finally:
        # Close SMTP connection
        server.quit()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Decrypt the encrypted email password
        encrypted_password = os.getenv('ENCRYPTED_EMAIL_PASSWORD')
        email_password = decrypt_password(encrypted_password)

        sender_email = email  # Assuming sender's email is provided in the form
        recipient_email = "tokaibrian@gmail.com"  # Fixed recipient email

        # Send the email
        send_email(sender_email, recipient_email, "Message from Contact Form", message)

        return "Message sent successfully!"


if __name__ == '__main__':
    app.run(debug=True)
