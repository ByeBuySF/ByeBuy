import os 
import requests

# Write a graphql request to insert data via hasura

def insert_data_via_graphql(data):
  # Set up the graphql request
  headers = {
    "Content-Type": "application/json",
    "X-Hasura-Admin-Secret": os.getenv("HASURA_ADMIN_SECRET")
  }
  payload = {
    "query": """
      mutation InsertTransaction($image_url: String!, $recognized_items: String!, $ai_description: String!, $estimated_price: Int!, $publish_result: String!) {
        insert_transactions_one(object: {image_url: $image_url, recognized_items: $recognized_items, ai_description: $ai_description, estimated_price: $estimated_price, publish_result: $publish_result}) {
          id
        }
      }
    """,
    "variables": {
      "image_url": data["image_url"],
      "recognized_items": data["recognized_items"],
      "ai_description": data["ai_description"],
      "estimated_price": data["estimated_price"],
      "publish_result": data["publish_result"]
    }
  }

  # Send the graphql request
  response = requests.post("https://api.hasura.io/v1/graphql", headers=headers, json=payload)
  return response.json()