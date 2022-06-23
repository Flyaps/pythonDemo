companies = []
if (n := len(companies)) == 1 and (first_company := companies[0]):
   print(f'We have only one company: {first_company}')
elif (n := len(companies)) > 1 and (first_company := companies[0]):
   print(f'We have such companies as: {", ".join(companies)}')
else:
   print(f'We have no companies')

print(n)
# 1
print(first_company)
# Traceback (most recent call last):
#   File "/home/user/main.py", line 12, in <module>
#     print(first_company)
# NameError: name 'first_company' is not defined
