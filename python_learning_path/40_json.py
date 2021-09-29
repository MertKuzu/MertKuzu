import json

person_string = '{"name":"Ali", "languages":["python","C#"]}'

#JSON string to Dict

result = json.loads(person_string)

#result = result["name"]
#result = result["languages"][0]

# print(type(result))
# print(result)


# with open("40.5_person.json") as f:
#     data = json.load(f)
#     print(data)
#     print(data["name"])
#     print(data["languages"])



#Dict to JSON string

person_dict = {
    "name":"mert",
    "languages":"['python','c++']"
}

# result = json.dumps(person_dict)

# print(type(result))
# print(result)

with open("40.5_person.json","w") as f:
    json.dump(person_dict, f)