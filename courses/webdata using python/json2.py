import json

data = '''
[
 { "name": "<hello>", 
   "age":"22",
   "city":"New York"
  },
 { "name": "arabi",
   "age":"44", 
   "city":"uk"
  }
]'''
info = json.loads(data)
print('user count:', len(info))
for item in info:
    print('Name:', item['name'])
    print('Age:', item['age'])
    print('City:', item['city'])
