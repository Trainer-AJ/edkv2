import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    # Read the environment variable with a fallback value
    my_var = os.getenv("MY_VAR_DEFAULT", "fallback_value")

    # Print it to the console for debugging purposes
    print(f"MY_VAR_DEFAULT is set to: {my_var}")

    # Return a JSON response with the value of the environment variable
    return jsonify({"MY_VAR_DEFAULT": my_var})

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
