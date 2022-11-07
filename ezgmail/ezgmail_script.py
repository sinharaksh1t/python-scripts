import ezgmail, os, variables

'''
# Read unread emails
unreadThreads = ezgmail.unread()
print(ezgmail.summary(unreadThreads))
'''

# Send email
recipients = {
  'Rakshit': 'sinharakshit7@gmail.com'
  # 'Avinash': 'singhavinash.dgh@gmail.com',
  # 'Deep': 'deep9c@gmail.com',
  # 'Kami': 'kamisetty.vineeth@gmail.com'
}

# cc = 'sinharakshit7@gmail.com'
cc = ''

subject = 'Hello Peeps!!'

body = 'Well, hello there 👋\n\n\
This email is written using the script that you \
can find in the screenshot below. Pretty cool, eh?\n\n\
(Sending this email again since Kami\'s email address was incorrect \
in the last one, lol 😝)\n\
(Sorry for the spam, I promise this is the last email for the night,\n\
had forgotten to add myself in cc 🙈)\n\n\
Your Friendly Neighborhood,\n\
Aquaman'

### This is the right way you would attach a file from a different directory
### You can apply direname(dirname(dirname(...))) as much as needed to go
### up the parent directories

currDir = os.path.dirname(__file__)
parent = os.path.dirname(currDir)
destDir = os.path.join(parent, '/'.join(['one_piece_bot', f'{variables.CHAPTER}.jpg']))
print(destDir)
attachments = [destDir]
# attachments = []

# ezgmail.send(', '.join(recipients.values()), subject, body, attachments, cc=cc)
