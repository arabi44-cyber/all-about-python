import json
data = '''{
 "name": "hello",
 "class":"csit",
 "rollno":{
    "type " : "intl",
    "number" : "12378"
 },
 "email":  {
   "hide": "yes"
   }
 }'''
info = json.loads(data)
print('name:', info['name'])
print('class:', info['class'])
print('rollno:', info['rollno'])
