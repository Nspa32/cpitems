# Sorry about all of the comments...
# That is what happens when I write a test code.

import urllib.request
import base64
import json

# Informaion
username = 'pyhax'
password = 'haxyou'
# Item you want to add
item = '1880'
api = 'FD 9B407F96-418B-4E0B-93DB-3AD33CC7D72E:205EF7823B24EE5277E318E061E5557F4648F1BF4CCFB457'

# Looks like this is required

# def base64encoder(string):
#	return base64.b64encode(string.encode('utf-8'))

# Start the request
# Change this
# ..
base = username + ':' + password
# Change this
encode = base64.b64encode(base.encode('ascii'))
decode = encode.decode('utf-8')
auth = urllib.request.Request('https://api.disney.com/clubpenguin/mobile/v2/authToken?appId=CPMCAPP&appVersion=1.4&language=en', None, headers={'Authorization' : 'Basic ' + str(decode) + ',' + api})
# Just to check
# print(str(decode))
auth = urllib.request.urlopen(auth).read()

# Print
# print(auth)
print('Successfully logged in')

# Load the json
auth = auth.decode('utf-8')
json = json.loads(auth)

# Save the authToken
authToken = json['authToken']
# Check
# print(authToken)

# Add the item
base = authToken + ':'
encode = base64.b64encode(base.encode('ascii'))
decode = encode.decode('utf-8')
# Check
# print(decode)
# Request
# Change this
purchase = urllib.request.Request('https://api.disney.com/clubpenguin/mobile/v2/purchase?catalogId=500435792&itemType=paper_item&itemId=' + item, 'POST'.encode('utf-8'), headers={'Authorization' : 'Basic ' + str(decode) + ',' + api})
# Now check the purchase
purchase = urllib.request.urlopen(purchase).read()

# Print
# print(purchase)
print('Successfully added item')
