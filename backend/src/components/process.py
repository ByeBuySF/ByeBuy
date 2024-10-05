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
from recognition import recognize_items, generate_description
from publishing import publish_to_social_media
from image import upload_image

def process_listing(image_data: str, user_description: str) -> Dict:
    """
    Main pipeline function to process a listing.
    
    Args:
    image_data (str): Base64 encoded image data
    user_description (str): User-provided description of the item(s)
    
    Returns:
    Dict: Processed listing information
    """
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


