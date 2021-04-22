import json
data = ""
with open("dak.json") as f :
    data = f.read()
    data = json.loads(data)

print(data)
for key, value in data.items():
    print(key , " : " , type(key) , value , " : " , type(value))