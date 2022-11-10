from web_scrapers import scrape
import ezgmail
import datetime

print('Script started...')

recipients = {
  'Rakshit': 'sinharakshit@gmail.com',
}

subject = 'Fountain Court current offer'

print('Starting the scrape...')
offerText, fcWebsite = scrape.web_scrape()
print(offerText, fcWebsite)

body = f'<h2>{offerText}</h2>\n\n\
  <hr>\
Click here to verify: {fcWebsite} \
<br>\
<br>\
Your friendly Neighbothood,\
<br>\
ElysiBot'

print('Sending email...')
ezgmail.send(', '.join(recipients.values()), subject, body, mimeSubtype='html')
print(f'Email sent at: {datetime.datetime.now()}')
print('--------------------------------------------------')
