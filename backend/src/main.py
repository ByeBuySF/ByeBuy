# Simple Python web server 
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

# This is the endpoint for creating a new listing, which receives an image in base64 format
# and then forwards the data into the pipeline.
@app.route('/api/v1/listings', methods=['POST'])
def post_listing():
    return "Hello, World!"

@app.route('/api/v1/listings/<id>', methods=['GET'])
def get_listing(id):
    return "Hello, World!" + id

if __name__ == '__main__':
    app.run(debug=True)