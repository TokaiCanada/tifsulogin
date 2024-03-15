import requests

# Define the form data to be submitted
form_data = {
    'name': 'John Doe',
    'email': 'johndoe@example.com',
    'message': 'This is a test message from the test script.'
}

# Send a POST request to the Flask application
response = requests.post('http://127.0.0.1:5000/submit_form', data=form_data)

# Check the response
if response.status_code == 200:
    print("Form submission successful!")
    print("Response text:", response.text)
else:
    print("Form submission failed. Status code:", response.status_code)
    print("Response text:", response.text)
