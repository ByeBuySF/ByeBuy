# Image storage using cloudinary 

import os
import boto3
import six
import uuid
import imghdr
import io
import base64

def upload_image(image_data: str) -> str:
    """
    Upload an image to Cloudinary and return the URL.

    Args:
    image_data (str): Base64 encoded image data

    Returns:
    str: URL of the uploaded image
    """

    # Set up the AWS credentials
    boto3.setup_default_session(
        aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
        aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'],
        region_name=os.environ['AWS_REGION']
    )

    # Upload the image to Amazon S3
    s3 = boto3.client('s3')
    file, file_name = decode_base64_file(image_data)

    # Upload the image to the bucket with the name of the image 
    s3.upload_fileobj(
        file,
        os.environ['AWS_BUCKET_NAME'],
        file_name,
        ExtraArgs={'ACL': 'public-read'}
    )

    # Get the URL of the uploaded image
    url = s3.generate_presigned_url(
        'get_object',
        Params={'Bucket': os.environ['AWS_BUCKET_NAME'], 'Key': file_name},
        ExpiresIn=3600
    )

    return url


def decode_base64_file(data):
    """
    Fuction to convert base 64 to readable IO bytes and auto-generate file name with extension
    :param data: base64 file input
    :return: tuple containing IO bytes file and filename
    """
    # Check if this is a base64 string
    if isinstance(data, six.string_types):
        # Check if the base64 string is in the "data:" format
        if 'data:' in data and ';base64,' in data:
            # Break out the header from the base64 content
            header, data = data.split(';base64,')

        # Try to decode the file. Return validation error if it fails.
        try:
            decoded_file = base64.b64decode(data)
        except TypeError:
            TypeError('invalid_image')

        # Generate file name:
        file_name = str(uuid.uuid4())[:12]  # 12 characters are more than enough.
        # Get the file name extension:
        file_extension = get_file_extension(file_name, decoded_file)

        complete_file_name = "%s.%s" % (file_name, file_extension,)

        return io.BytesIO(decoded_file), complete_file_name

def get_file_extension(file_name, decoded_file):
    extension = imghdr.what(file_name, decoded_file)
    extension = "jpg" if extension == "jpeg" else extension
    return extension

# Write a python main script to test upload image function
if __name__ == "__main__":
    import base64

    image_data = '/Users/darrenkarlsapalo/go/src/github.com/ByeBuySF/backend/src/components/image/test.png'

    # Load a sample image file and encode it to base64
    with open(image_data, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    
    # Call the upload_image function
    image_url = upload_image(encoded_string)
    
    # print(f"Uploaded image URL: {image_url}")
