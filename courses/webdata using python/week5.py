import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
url = input("Enter the URL to: ")
uh = urllib.request.urlopen(url)
data= uh.read()

tree = ET.fromstring(data)
result = tree.findall('comments/comment')
sum = 0
count = 0
for comment in result:
    x = int(comment.find('count').text.strip())
    count = count+1
    sum = sum + x

print('sum',sum)
print('count',count)

