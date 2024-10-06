# Define a pipeline for processing listings that involves:
# 1. Recognition
#   a. Object detection to detemrine how many items are found in the image (using AI component; ChatGPT)
#   b. Text description generation (using AI component; ChatGPT)
# 2. Pricing
#   a. Price estimation (using external API)
# 3. Publishing
#   a. Publishing to social media via Facebook Graph API 

import requests
import json
from typing import List, Dict
from components.pricing.pricing import pricing
from components.recognition.recognition import image_recognition
from components.publishing.publishing import send_message, generate_sales_message
import ast

async def process_listing(image:str, image_link: str) -> List:
    """
    Main pipeline function to process a listing.
    
    Args:
    image (str): Base64 encoded image data
    image_link: link for image AWS
    
    Returns:
    list: Processed listing information
    """

    

    recognized_items = ast.literal_eval(
                        image_recognition(image)
                        )
                        
    posts = []
    for item in recognized_items:
        description = item
        estimated_price = pricing(item)
        description["price"] = estimated_price

        message = generate_sales_message(description)
        description["message"] = message

        post_link = await send_message(message, image_link)
        description["post_link"] = post_link

        posts.append(description)

    return posts
