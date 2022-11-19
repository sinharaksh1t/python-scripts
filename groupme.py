import requests
import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv('GROUPME_TOKEN')
print(token)

headers = {"Content-Type": "application/json"}
data = {
  "message": {
    "source_guid": "123456",
    "text": "No problem!"
  }
}

EAST_KING_COUNTY_REGION = '32210061'
EAST_REGION_4D = '32536590'

response = requests.post(
  f'https://api.groupme.com/v3/groups/{EAST_REGION_4D}/messages?token={token}',
  headers=headers,
  json=data
)

# response = requests.get(f'https://api.groupme.com/v3/groups?token={token}')

print(response)
print('-----------------------------')
print(response.text)
