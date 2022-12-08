from one_piece_bot import scrape, utils
import ezgmail
import os
import datetime


# Send email
recipients = {
  'Rakshit': 'sinharakshit@gmail.com',
}

print('Starting the scrape...')
current_chapter, chapter_url, url = scrape.scrape_OP_chapters()
print(f'Scrape and combining process complete for {chapter_url}...')

# Get the host platform
print('Getting the host platform...')
host_platform = utils.get_host_platform()
print(f'Host platform found to be {host_platform}...')

subject = f'One Piece: {chapter_url}'

body = f'Hello<br><br>\
PFA: {chapter_url}\
<br>Chapter URL: {url}\
<br><br>Your Friendly Neighbothood,<br>\
ElysiBot<br>\
(Sent from <strong>{host_platform}<strong>)'

# This is the right way you would attach a file from a different directory
# You can apply direname(dirname(dirname(...))) as much as needed to go
# up the parent directories
curr_dir = os.path.dirname(__file__)
# dest_dir = os.path.join(
#   curr_dir, '/'.join(['one_piece_chapters', chapter_url, f'{chapter_url}.jpg']))
attachments = [f'one_piece_chapters/{chapter_url}/{chapter_url}.jpg']
email_recipients = ', '.join(recipients.values())

print('Sending email...')
ezgmail.send(email_recipients, subject, body, attachments, mimeSubtype='html')
print(f'Email sent at: {datetime.datetime.now()}')

# Update chapter number
print('Starting updating chapter number...')
new_chapter = int(current_chapter) + 1
utils.update_chapter(new_chapter)

print('--------------------------------------------------')
