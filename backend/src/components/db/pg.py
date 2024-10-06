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
      mutation InsertProduct($data: jsonb, $pricing: Int, $state: String) {
        insert_Product_one(object: {
          pricing: $pricing,
          data: $data,
          state:$state,
        }) {
          id
        }
      }
    """,
    "variables": {
      "pricing": data["pricing"],
      "state": data["state"],
      "data": data["data"],
    }
  }

  # Send the graphql request
  response = requests.post("https://tomegg-dev.hasura.app/v1/graphql", headers=headers, json=payload)
  return response.json()