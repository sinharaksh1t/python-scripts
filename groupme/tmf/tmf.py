import requests
import bs4
import sys


def tmf():
  url = 'https://cms.sgi-usa.org/tmf/'
  response = requests.get(url)
  try:
    response.raise_for_status()
  except Exception as ex:
    print(f'Something went wrong: {ex}')
    sys.exit(1)

  soup = bs4.BeautifulSoup(response.text, 'lxml')

  tmf_soup = soup.select('div.quote-inner')
  tmf = tmf_soup[0].text

  return tmf
