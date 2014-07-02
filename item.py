# Including items you already have breaks the script
# Simple item adder
# Python 3.x
# Written by master Astro260
import urllib.request
import base64
import json

# Penguin information
username = 'pyhax'
password = 'haxyou'
# Items
items = [413, 444]
# The API
api = 'FD 9B407F96-418B-4E0B-93DB-3AD33CC7D72E:205EF7823B24EE5277E318E061E5557F4648F1BF4CCFB457'

# Request
base = username + ':' + password
base = base64.b64encode(base.encode('ascii'))
base = base.decode('utf-8')
login = urllib.request.Request('https://api.disney.com/clubpenguin/mobile/v2/authToken?appId=CPMCAPP&appVersion=1.4&language=en', None, headers={'Authorization' : 'Basic ' + str(base) + ',' + api})
login = urllib.request.urlopen(login).read()

# Success
print('Logged in %s : %s' % (username, password))

# Base
base = login.decode('utf-8')
base = json.loads(base)

# Store the authToken
authToken = base['authToken']

# Add the items
base = authToken + ':'
base = base64.b64encode(base.encode('ascii'))
base = base.decode('utf-8')

# Foreach item
for item in items:
  # Don't bother asking about POST
  purchase = urllib.request.Request('https://api.disney.com/clubpenguin/mobile/v2/purchase?catalogId=500435792&itemType=paper_item&itemId=' + str(item), 'POST'.encode('utf-8'), headers={'Authorization' : 'Basic ' + str(base) + ',' + api})
  purchase = urllib.request.urlopen(purchase).read()
  
  # Get the purchase data
  # ..
  pur_base = purchase.decode('utf-8')
  pur_base = json.loads(pur_base)
  
  # The date
  date = pur_base['purchaseDate']
  
  if(date != None):
    print('Added item %s' % item)
  else:
    print('Error adding item %s - %s' % (item, purchase))
