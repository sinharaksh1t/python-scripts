import requests
import os
from dotenv import load_dotenv
from tmf import tmf
import sys
import datetime

# Get todays TMF
print("Fetching today's TMF...")
tmf = tmf()

load_dotenv()
token = os.getenv('GROUPME_TOKEN')
EAST_KING_COUNTY_REGION = os.getenv('EAST_KING_COUNTY_REGION')
ELYSIBOT_TEST = os.getenv('ELYSIBOT_TEST')

headers = {"Content-Type": "application/json"}

data = {
  "message": {
    "source_guid": "123456",
    "text": tmf
  }
}

print(f'Sending message to group...')
response = requests.post(
  f'https://api.groupme.com/v3/groups/{EAST_KING_COUNTY_REGION}/messages?token={token}',
  headers=headers,
  json=data
)

try:
  response.raise_for_status()
except Exception as ex:
  print(f'Some problem occurred while sending the GroupMe message`: {ex}')
  sys.exit(1)

# response = requests.get(f'https://api.groupme.com/v3/groups?token={token}')
# print(response.text)

print(f'Message sent at: {datetime.datetime.now()}')
print('--------------------------------------------------')
