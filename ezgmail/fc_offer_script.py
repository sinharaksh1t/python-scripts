from web_scrapers import scrape
import ezgmail

recipients = {
  'Rakshit': 'sinharakshit7@gmail.com'
}

subject = 'EZGmail Bot: Fountain Court current offer'

offerText, fcWebsite = scrape.web_scrape()

body = f'<h2>{offerText}</h2>\n\n\
Click here to verify: {fcWebsite}\n\n\
Thanks,\n\
EZGmail Bot'

ezgmail.send(recipients.get('Rakshit'), subject, body, mimeSubtype='html')
