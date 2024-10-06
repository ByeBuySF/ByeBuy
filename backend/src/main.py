# Simple Python web server 
from flask import Flask, jsonify, request
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
from components.image.image_storage import upload_image
from components.process import process_listing
from components.db.pg import insert_data_via_graphql
@app.route('/')
def home():
    return "Hello, World!"

# This is the endpoint for creating a new listing, which receives an image in base64 format
# and then forwards the data into the pipeline.
@app.route('/api/v1/listings', methods=['POST'])
async def post_listing():
    data = request.get_json()
    image_data = data['image_data']
    
    # processed_listing = process_listing(image_data)
    image_link = upload_image(image_data)
    processed_listing = await process_listing(image_data, image_link)

    for post in processed_listing:
        insert_data_via_graphql(post)

    return "ok"

@app.route('/api/v1/listings/<id>', methods=['GET'])
def get_listing(id):
    return "Hello, World!" + id

if __name__ == '__main__':
    app.run(debug=True)