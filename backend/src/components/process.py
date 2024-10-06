# Define a pipeline for processing listings that involves:
# 1. Recognition
#   a. Object detection to detemrine how many items are found in the image (using AI component; ChatGPT)
#   b. Text description generation (using AI component; ChatGPT)
# 2. Pricing
#   a. Price estimation (using external API)
# 3. Publishing
#   a. Publishing to social media via Facebook Graph API 

import requests

from typing import List, Dict
from pricing import estimate_price
<<<<<<< HEAD
from recognition import recognize_items, generate_description
from publishing import publish_to_social_media
from image import upload_image
=======
from recognition import image_recognition
from publishing import send_message, generate_sales_message
import ast
>>>>>>> main

async def process_listing(image:str, image_link: str) -> List:
    """
    Main pipeline function to process a listing.
    
    Args:
    image (str): Base64 encoded image data
    image_link: link for image AWS
    
    Returns:
    list: Processed listing information
    """
<<<<<<< HEAD
    image_url = upload_image(image_data)
    recognized_items = recognize_items(image_url)
    ai_description = generate_description(image_url, recognized_items, user_description)
    estimated_price = estimate_price(recognized_items, ai_description)
    publish_result = publish_to_social_media(image_url, ai_description, estimated_price)
    
    return {
        "recognized_items": recognized_items,
        "ai_description": ai_description,
        "estimated_price": estimated_price,
        "publish_result": publish_result
    }
=======
>>>>>>> main

    recognized_items = ast.literal_eval(
                        image_recognition(image)
                        )
                        
    posts = []
    for item in recognized_items:
        
        description = ast.literal_eval(item)
        estimated_price = estimate_price(item)
        description["price"] = estimated_price

        message = generate_sales_message(description)
        description["message"] = message

        post_link = await send_message(message, image_link)
        description["post_link"] = post_link

        posts.append(description)

    return posts
