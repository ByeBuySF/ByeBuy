from typing import Dict
import asyncio
from telegram import Bot
import os

async def send_message(message: str, image_link: str):
    """
    Sends a message to a telegram channel
    
    Args:
    message (str): message with the complete description of an item
    image_link (str): image link from AWS

    Returns:
    str: post link
    """

    channel_username = "@ByeBuySF"
    bot = Bot(token=os.environ["TELEGRAM_BOT_TOKEN"])
    
    print(image_link)
    sent_message = await bot.send_photo(chat_id=channel_username, photo=image_link, caption=message)
    
    # Generate the post link
    message_id = sent_message.message_id
    channel_name = channel_username.lstrip('@')
    post_link = f"https://t.me/{channel_name}/{message_id}"
    
    return post_link


def generate_sales_message(item):

    message = f"""
🛍️ For Sale: {item['name'].title()} 🛍️

📦 Item Description:
{item['description']}

🔍 Condition:
{item['condition']}

💰 Price: ${item['price']}

"""

    return message
