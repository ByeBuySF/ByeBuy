import os
import requests
import json
import re
from openai import OpenAI

# json = {"name": "Sofa", "description": "Used, Gray, Leather", "condition": "Good"}
# 
# 
def pricing(json):
    """
    Estimates the price of an item based on its name, description, and condition 
    using the OpenAI API.

    Args:
        json (dict): A dictionary containing the item's name, description, and condition.

    Returns:
        int: The estimated price as a integer, returned from the OpenAI API response.
        
    Raises:
        Exception: If there is an error processing the items or communicating with the API.
    """

    # Load environment variables from .env file

    # Get the API key from the environment variables
    api_key = os.getenv('OPENAI_API_KEY')
     
    # Initialize OpenAI client
    client = OpenAI(api_key=api_key)
    
    # Define prompt message
    prompt_message = (
        "You are a pricing expert. I have an item with its names, description, and condition. "
        "Please estimate the price for an item based on the details provided.\n\n"
        f"Here is the information: {json}\n"  
        "Provide a price (as an integer) for an item based on the description and condition. "
        "Your response MUST be a single integer."
    )
    
        # ChatGPT request
    PROMPT_MESSAGES = [
        {
            "role": "user",
            "content": prompt_message,
        },
    ]

    params = {
        "model": "gpt-4o",  # Ensure the model name is correct
        "messages": PROMPT_MESSAGES,
        "max_tokens": 10,
    }

    try:
        # Send request
        response = client.chat.completions.create(**params)

        # Parse response
        response_text = response.choices[0].message.content

        return response_text

    except Exception as e:
        print(f"Error processing items: {e}")