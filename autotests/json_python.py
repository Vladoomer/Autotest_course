import json

json_data = '''{
  "name": "Иван",
  "age" : 30,
  "is_Student" : false,
  "courses" : [
    "Python",
    "QA",
    "API TESTING"
  ],
  "address" : {
    "city" : "Moscow",
    "zip" : "10100",
    "point":
    {
      "name" : "dotov"
    }
  }
}'''
parsed_data = json.loads(json_data)

print(parsed_data["address"]["city"])

data = {
    "name": "Иван",
    "age" : 30,
    "is_Student" : False
}

json_string = json.dumps(data, indent=4)
print(json_string)

with open("json_example.json", 'r', encoding='utf-8') as f:
    read_data = json.load(f)
    print(read_data)

with open("json_user.json", 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
