# import os
import requests
import bs4
import datetime


def web_scrape():
  # Create directory where downloaded files will stay
  # dir = 'downloads'
  # print(f'Creating "{dir}" directory if it doesn\'t exist already...')
  # os.makedirs(dir, exist_ok=True)

  # Download image from the One Piece chapter
  url = f'https://www.essexapartmenthomes.com/apartments/seattle/fountain-court'
  print(f'Download the webpage from {url}...')
  res = requests.get(url)
  try:
    res.raise_for_status()
  except Exception as ex:
    print(f'Some problem occurred while downloading the webpage `{url}`: {ex}')

  soup = bs4.BeautifulSoup(res.text, 'lxml')
  print('Selecting the data coming from the website...')
  selector = 'section.property-offer-cta__main-container h2'
  offer = soup.select(selector)
  print(f'Element found: {offer}')

  if len(offer) > 0:
    print(offer[0].getText())
    return (offer[0].getText(), url)

  no_offer = 'Sorry, looks like there is no on-going offer at the moment.'
  return (no_offer, url)

# web_scrape()
