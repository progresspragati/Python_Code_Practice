import json as j

x = '{"name" : "John", "age" : 30, "city": "NewYork"}'

y = j.loads(x)
print(y["name"])
print(y["age"])
print(y["city"])