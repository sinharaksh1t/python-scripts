import requests, bs4, sys

res = requests.get('http://nostarch.com')
try:
  res.raise_for_status()
except Exception as ex:
  print(f'There seems to have been a problem: {ex}')
  sys.exit(1)

# noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')
noStarchSoup = bs4.BeautifulSoup(res.text, 'lxml') # Apparently lxml is faster

print(len(res.text))
