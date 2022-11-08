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
  # url = f'https://www.essexapartmenthomes.com/apartments/seattle/fountain-court'
  url = f'https://www.essexapartmenthomes.com/apartments/seattle/fountain-court/floor-plans-and-pricing'
  print(f'Download the webpage from {url}...')
  res = requests.get(url)
  try:
    res.raise_for_status()
  except Exception as ex:
    print(f'Some problem occurred while downloading the webpage `{url}`: {ex}')

  soup = bs4.BeautifulSoup(res.text, 'lxml')
  print('Selecting the data coming from the website...')
  selector = 'section.property-offer-cta__main-container h2'
  # selector1Bed = 'div.floor-plan-card__content__main'
  selector1Bed = 'div.tabs__content'
  offer = soup.select(selector)
  oneBedInfo = soup.select(selector=selector1Bed)
  # print(f'Element found: {offer}')
  print(f'Element found: {oneBedInfo}')

  # if offer == []:
  #   print('Sorry, could not find the desired info on the website')
  # else:
  # print(offer[0].getText())
  # return (offer[0].getText(), url)
  # print(oneBedInfo[0].getText())


web_scrape()
