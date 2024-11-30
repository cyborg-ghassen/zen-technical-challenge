from http.server import HTTPServer, SimpleHTTPRequestHandler
from flask import Flask, render_template, request, jsonify, redirect, url_for
import threading

# Flask app setup
app = Flask(__name__)

# Example user for login
# This is a placeholder user. In a real application, you'd store this in a database or file.
users = {'test': 'password'}

# Route for the index page (login and register form)
@app.route('/')
def index():
    # Renders the 'index.html' page which contains the login and registration form
    return render_template('index.html')

# Function to load users from a JSON file
def load_users():
    try:
        # Attempt to open the 'users.json' file and load its contents
        with open('users.json', 'r') as file:
            users = json.load(file)  # Load users from the JSON file
    except FileNotFoundError:
        # If the file doesn't exist, return an empty dictionary
        users = {}  
    return users

# Route for logging in a user
@app.route('/login', methods=['POST'])
def login():
    # Get JSON data from the incoming request
    data = request.get_json()
    username = data.get('username')  # Extract the username from the request
    password = data.get('password')  # Extract the password from the request

    # Load the users from the JSON file
    users = load_users()

    # Check if the user exists and if the password matches
    if username in users and users[username] == password:
        # If login is successful, return a message and a fake token for authentication
        return jsonify({'message': 'Login successful!', 'access_token': 'fake-token'})
    else:
        # If the login fails, return an error message with a 401 status code
        return jsonify({'message': 'Invalid credentials!'}), 401

# Route for registering a new user
@app.route('/register', methods=['POST'])
def register():
    # Get JSON data from the incoming request
    data = request.get_json()
    username = data.get('username')  # Extract the username from the request
    password = data.get('password')  # Extract the password from the request

    # Add the new user to the 'users' dictionary (In a real application, save to a file or database)
    users[username] = password
    return jsonify({'message': f'User {username} registered successfully!'})

# Route for the page displayed after successful login
@app.route('/index1')
def index1():
    # Renders the 'index1.html' page which is shown after login is successful
    return render_template('index1.html')

# Function to start an HTTP server in the background (independent of Flask)
def run_http_server():
    PORT = 8000
    # Set up the HTTP server to serve static files
    httpd = HTTPServer(('localhost', PORT), SimpleHTTPRequestHandler)
    print(f"Serving static files at http://localhost:{PORT}")
    httpd.serve_forever()  # Start serving static files forever

# Function to start the Flask server
def run_flask_server():
    # Start the Flask app with debugging enabled and use_reloader set to False to avoid double start
    app.run(debug=True, use_reloader=False)

# Start Flask and HTTPServer in separate threads
if __name__ == '__main__':
    # Start the HTTP server in a separate thread
    http_thread = threading.Thread(target=run_http_server)
    http_thread.start()

    # Start Flask in the main thread
    run_flask_server()
