import json
# JSON

# API Response  - JSON String
json_data_str = '{"name": "John", "age": 30, "city": "New York"}'
# JSON to dic

py_dict = json.loads(json_data_str)

print(type(py_dict))
print(py_dict["name"])
print(py_dict["age"])
print(py_dict.get("name"))
print(py_dict.keys())
print(py_dict.values())


# dict to JSON String

python_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

json_data_str_back = json.dumps((python_dict))

print(json_data_str_back)
print(type(json_data_str_back))