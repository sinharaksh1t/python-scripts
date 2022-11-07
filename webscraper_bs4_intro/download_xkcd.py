import os, requests, bs4

dir = 'xkcd_comics'
print(f'Creating {dir} directory...')
os.makedirs(dir, exist_ok=True)

url = 'https://xkcd.com/2693/'
print(f'Downloading the webpage from {url}...')
res = requests.get(url)
try:
  res.raise_for_status()
except Exception as ex:
  print(f'Something went wrong: {ex}')

soup = bs4.BeautifulSoup(res.text, 'lxml')
print('Selecting the coming from the website...')
comicElement = soup.select('#comic > img')

if comicElement == []:
  print('Sorry, could not find the comic element.')
else:
  src = comicElement[0].get('src')
  imgUrl = f'https:{src}'
  print(f'Downloading the image {imgUrl}..')
  img = requests.get(imgUrl)
  res.raise_for_status()

  print(f'Saving the downloaded image to the folder {dir}')
  imgFile = open(os.path.join(dir, os.path.basename(imgUrl)), 'wb')
  for chunk in img.iter_content(100000):
    imgFile.write(chunk)
  imgFile.close()

