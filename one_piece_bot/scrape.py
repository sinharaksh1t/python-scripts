import os, requests, bs4, variables

def scrape_OP_chapters():
  # Create directory where downloaded files will stay
  dir = 'one_piece_chapters'
  print(f'Creating {dir} directory if it doesn\'t exist already...')
  os.makedirs(dir, exist_ok=True)

  # Download image from the One Piece chapter
  url = f'https://ww1.read-onepiece.com/manga/{variables.CHAPTER}'
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
  print(mangaEle)

  if mangaEle == []:
    print('Sorry, could not find the manga on the website')
  else:
    for i, page in enumerate(mangaEle):
      imgSrc = page.get('src')
      print(f'Downloading the image {imgSrc}...')
      img = requests.get(imgSrc)
      res.raise_for_status()

      print(f'Saving the downloaded image to the folder {dir}...')
      imgFile = open(os.path.join(dir, f'page-{i+1}.jpg'), 'wb')
      for chunk in img.iter_content(100000):
        imgFile.write(chunk)
      imgFile.close()


  # Combine all those into a single PDF

  # Use the ezgmail module to send email to yourself