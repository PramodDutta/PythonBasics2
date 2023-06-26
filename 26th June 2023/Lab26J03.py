import json

with open('file.json') as file:
    py_dict = json.load(file)

print(py_dict)