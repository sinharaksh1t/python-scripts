from web_scrapers import scrape
import ezgmail

print('Script started...')

recipients = {
  'Rakshit': 'sinharakshit7@gmail.com'
}

subject = 'EZGmail Bot: Fountain Court current offer'

print('Starting the scrape...')
offerText, fcWebsite = scrape.web_scrape()
print(offerText, fcWebsite)

body = f'<h2>{offerText}</h2>\n\n\
  <hr>\
Click here to verify: {fcWebsite} \
<br>\
Your friendly Neighbothood,\
<br>\
ElysiBot'

print('Sending email...')
ezgmail.send(recipients.get('Rakshit'), subject, body, mimeSubtype='html')
