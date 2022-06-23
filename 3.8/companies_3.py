companies = ['Flyaps', 'Google', 'Apple']
if (n := len(companies)) == 1 and (first_company := companies[0]):
  print(f'We have only one company: {first_company}')
elif (n := len(companies)) > 1 and (first_company := companies[0]):
  print(f'We have such companies as: {", ".join(companies)}')
else:
  print(f'We have no companies')