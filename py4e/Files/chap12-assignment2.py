# chapter 12 - assignment 2


import urllib.request, urllib.parse, urllib.error
import json, ssl

ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE


serviceurl='http://py4e-data.dr-chuck.net/json?'

place=input("Enter location: ")
parm=dict()

parm['address']=place
parm['key']=42
url=serviceurl+urllib.parse.urlencode(parm)

print('Retrieving url:', url)
data=urllib.request.urlopen(url,context=ctx).read().decode()

print('Retrieved', len(data), 'bytes')

jsdata=json.loads(data)

print(json.dumps(jsdata,indent=2))
print('Place ID:',jsdata['results'][0]['place_id'])



