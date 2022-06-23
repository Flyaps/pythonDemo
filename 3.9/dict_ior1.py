x = {"key1": "value1 from x", "key2": "value2 from x"}
y = {"key2": "value2 from y", "key3": "value3 from y"}
print(x | y)
# {'key1': 'value1 from x', 'key2': 'value2 from y', 'key3': 'value3 from y'}
print(y | x)
# {'key2': 'value2 from x', 'key3': 'value3 from y', 'key1': 'value1 from x'}
