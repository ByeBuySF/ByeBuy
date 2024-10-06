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
from recognition import image_recognition
from publishing import send_message, generate_sales_message
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
        
        description = ast.literal_eval(item)
        estimated_price = estimate_price(item)
        description["price"] = estimated_price

        message = generate_sales_message(description)
        description["message"] = message

        post_link = await send_message(message, image_link)
        description["post_link"] = post_link

        posts.append(description)

    return posts
