from flask import Flask, render_template, request
import os
from cryptography.fernet import Fernet
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = Flask(__name__)

# Load the encryption key securely (you may fetch it from environment variables)
key = b'CfVbu8IOqCc6L385tVcoZZJEc_FAcn55u9vhbi59hwQ='

# Decrypt the app-specific password
def decrypt_password(encrypted_password):
    cipher_suite = Fernet(key)
    print("Decrypting password")
    return cipher_suite.decrypt(encrypted_password.encode()).decode()

# Function to send email
def send_email(sender_email, recipient_email, subject, message):
    # Configure SMTP server settings
    smtp_server = 'smtp.gmail.com'
    print("SMTP Server")
    smtp_port = 587  # Port for TLS (587 is commonly used)
    print("SMTP Port 587")
    smtp_username = 'tokaibrian@gmail.com'
    print("SMTP Receiver name tokaibrain@gmail.com")
    
    # Decrypt the encrypted app-specific password
    encrypted_password = os.getenv('ENCRYPTED_APP_PASSWORD')
    print("Decrypted app password")
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
    print("Entered Index route")
    return render_template('index.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    print("Entered submit_form route")  # Print statement to check if the route is accessed
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        sender_email = email  # Assuming sender's email is provided in the form
        recipient_email = "tokaibrian@gmail.com"  # Fixed recipient email
        
        # Custom subject for the email
        subject = f"MYTY - from {email}"

        # Send the email with the custom subject
        send_email(sender_email, recipient_email, subject, message)

        return "Message sent successfully!"


if __name__ == '__main__':
    app.run(debug=True)
