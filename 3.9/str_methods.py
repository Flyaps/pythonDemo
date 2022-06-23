string = '12|34|56'

string = string.removeprefix('34')  # No effect
print(string)                       # 12|34|56

string = string.removeprefix('12')
print(string)                       # |34|

string = string.removesuffix('56')
print(string)                       # |34|

string = string.removesuffix('34')  # No effect
print(string)                       # |34|
