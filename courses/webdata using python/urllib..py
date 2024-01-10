import urllib.request,urllib.parse,urllib.error
fhand = urllib.request.urlopen('https://hamrocsit.com/semester/fourth/toc/question-bank/2080')
count = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        count[word] = count.get(word,0)+1
        print(word,count[word])
