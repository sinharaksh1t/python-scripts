import requests
import bs4

url = 'https://cms.sgi-usa.org/tmf/'
response = requests.get(url)
try:
  response.raise_for_status()
except Exception as ex:
  print(f'Something went wrong: {ex}')

soup = bs4.BeautifulSoup(response.text, 'lxml')

print('Selecting today\'s TMF...')
tmf = soup.select('div.quote-inner')

print(tmf[0].text)
