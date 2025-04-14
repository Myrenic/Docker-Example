# Import the Flask class and the jsonify function from the flask module
from flask import Flask, jsonify

# Create an instance of the Flask class. This instance will be our WSGI application.
app = Flask(__name__)

# Define a route for the URL /api/hello. This means that when a user visits /api/hello,
# the function hello() will be called.
@app.route('/api/hello', methods=['GET'])
def hello():
    # Return a JSON response with a message "Hello, World!"
    return jsonify(message="Hello, World!")

# This block ensures that the Flask application runs only if the script is executed directly
# and not when imported as a module in another script.
if __name__ == '__main__':
    # Run the Flask application on the local development server.
    # host='0.0.0.0' makes the server publicly available, and port=5000 specifies the port number.
    app.run(host='0.0.0.0', port=5000)
