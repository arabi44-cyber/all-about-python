import urllib.request, urllib.parse, urllib.error
import json
service_url = 'http://py4e-data.dr-chuck.net/json?'
while True:
    address = input('enter the address: ')
    if len(address) < 1: break
    url = service_url + urllib.parse.urlencode({'address': address})

    print("Retrieving", url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode('utf-8')
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None
    if not js or "status" not in js or js["status"] != "OK":
        print("==== No results found ====")
        print(data)
        continue
    print(json.dumps(js, indent=4))

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print("Latitude:", lat,"Longitude:", lng)
    location = js["results"][0]["formatted_address"]
    print("Location:", location)
