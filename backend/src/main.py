# Simple Python web server 
import requests
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

# This is the endpoint for creating a new listing, which receives an image in base64 format
# and then forwards the data into the pipeline.
@app.route('/api/v1/listings', methods=['POST'])
def post_listing():

    image_data = request.json['image_data']
    user_description = request.json['user_description']
    processed_listing = process_listing(image_data, user_description)
    

    return jsonify(processed_listing)

@app.route('/api/v1/listings/<id>', methods=['GET'])
def get_listing(id):
    return "Hello, World!" + id

if __name__ == '__main__':
    app.run(debug=True)