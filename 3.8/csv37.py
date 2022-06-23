import csv

with open('file.csv', 'rt') as f:
   reader = csv.DictReader(f)
   for i in reader:
       print(type(i))          # OrderedDict
       print(type(i) == dict)  # False
