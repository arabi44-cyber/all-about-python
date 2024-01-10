import urllib.request, urllib.parse, urllib.error
import json

url = input("Enter the URL: ")
uh = urllib.request.urlopen(url)
data = uh.read().decode('utf-8')

info = json.loads(data)
sum = 0

for item in info["comments"]:
    x = int(item["count"])
    sum = sum + x
print("The sum of:",sum)
