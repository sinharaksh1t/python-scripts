import os
import requests
import bs4
from one_piece_bot import combine_pages
from one_piece_bot import utils
# import combine_pages
# import utils


def scrape_OP_chapters():
  current_chapter, chapter_url = utils.get_latest_chaper_url()
  print(chapter_url)

  # Create directory where downloaded files will stay
  dir = f'one_piece_chapters/{chapter_url}'
  print(f'Creating {dir} directory if it doesn\'t exist already...')
  os.makedirs(dir, exist_ok=True)

  # Download image from the One Piece chapter
  url = f'https://ww1.read-onepiece.com/manga/{chapter_url}'
  print(f'Download the webpage from {url}...')
  res = requests.get(url)
  try:
    res.raise_for_status()
  except Exception as ex:
    print(f'Some problem occurred while downloading the webpage `{url}`: {ex}')

  soup = bs4.BeautifulSoup(res.text, 'lxml')
  print('Selecting the data coming from the website...')
  selector = 'img'
  mangaEle = soup.select(selector)

  if mangaEle == []:
    print('Sorry, could not find the manga on the website')
  else:
    for i, page in enumerate(mangaEle):
      imgSrc = page.get('src')
      print(f'Downloading the image {imgSrc}...')
      img = requests.get(imgSrc)
      res.raise_for_status()

      imgFile = open(os.path.join(dir, f'page-{i+1}.jpg'), 'wb')
      for chunk in img.iter_content(100000):
        imgFile.write(chunk)
      imgFile.close()

  print('All images downloaded successfully...')

  # Combine all those into a single PDF
  print('Starting the combining process...')
  combine_pages.combine_all_pages()
  print('All images have been combined successfully...')

  # # Update chapter number
  # print('Starting updating chapter number...')
  # new_chapter = int(current_chapter) + 1
  # utils.update_chapter(new_chapter)

  return current_chapter, chapter_url, url


# scrape_OP_chapters()
