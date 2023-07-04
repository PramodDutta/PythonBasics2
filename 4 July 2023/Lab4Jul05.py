from collections import Counter

cnt = Counter()
for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
    cnt[word] = cnt[word] + 1
print(cnt)



from collections import OrderedDict
d = OrderedDict()
d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'

for key, value in d.items():
    print(key, value)


my_dict = {"name": "Pramod", "age": 32, "isMale": True, "Bal": 10.45}
print(my_dict)