import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
  address = ' '.join(sys.argv[1:])
else:
  address = pyperclip.paste()

mapsAddress = f'https://www.google.com/maps/place/{address.replace(" ", "+")}'
print(mapsAddress)
webbrowser.open(mapsAddress)