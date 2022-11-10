from one_piece_bot import scrape
import ezgmail
import os
import datetime


# Send email
recipients = {
  'Rakshit': 'sinharakshit@gmail.com'
}

print('Starting the scrape...')
chapter_url = scrape.scrape_OP_chapters()
print(f'Scrape and combining process complete for {chapter_url}...')

subject = f'One Piece: {chapter_url}'

body = f'Hello<br><br>\
PFA: {chapter_url}\
<br><br>Your Friendly Neighbothood,<br>\
ElysiBot'

# This is the right way you would attach a file from a different directory
# You can apply direname(dirname(dirname(...))) as much as needed to go
# up the parent directories
curr_dir = os.path.dirname(__file__)
dest_dir = os.path.join(
    curr_dir, '/'.join(['one_piece_chapters', chapter_url, f'{chapter_url}.jpg']))
attachments = [dest_dir]

print('Sending email...')
ezgmail.send(', '.join(recipients.values()), subject, body, attachments, mimeSubtype='html')
print(f'Email sent at: {datetime.datetime.now()}')
print('--------------------------------------------------')
