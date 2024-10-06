from typing import List, Dict
from openai import OpenAI
import base64
import io
import os

def image_recognition(base64_image: str) -> list:
    """
    Pipeline for recognizing objects on the image
    
    Args:
    base64_image (str): Base64 encoded image data
    
    Returns:
    List: JSON for each object consisting of name, description and condition
    """

    client = OpenAI(api_key = os.environ["OPENAI_API_KEY"])

    prompt_message = """You are the best image recognition model in the world. 
    I want you to scan the image and analyze all the items you see there. 
    For each item that you were able to recognize I want you to provide a name, a description and evaluate the condition of the item.
    Condition includes: how old is the item, is it broken or not, does it look good, is it damaged, is it dirty. Be precise and explain everything.
    Your response MUST be a list of jsons that looks like:
    [{"name": "item1_name", "description": "item1 description", "condition": "item1 condition explanation"}, {item2 json here}]
    where each json corresponds to 1 item from the image. Do not add any additional keys, jsons or lists. All quotation marks should use double quotes."""

    PROMPT_MESSAGES = [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": prompt_message},
                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}}
            ],
        },
    ]

    params = {
        "model": "gpt-4-vision-preview",
        "messages": PROMPT_MESSAGES,
        "max_tokens": 1024,
    }

    result = client.chat.completions.create(**params)
    text = result.choices[0].message.content
    return text
