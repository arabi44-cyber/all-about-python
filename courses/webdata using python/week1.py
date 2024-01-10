import re

file=open("hello.txt")
text = file.read()
digit = re.findall('[0-9]+',text)

sum = 0
for i in digit:
 i=int(i)
 sum=sum+i

print(sum)
file.close()

