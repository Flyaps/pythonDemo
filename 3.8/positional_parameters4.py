def f(a, b, /, *args, **kwargs):
   print(a, b, args, kwargs)


f(10, 20, 1, 2, 3, a=1, b=2, c=3)         # a and b are used in two ways
#  10 20 (1, 2, 3) {'a': 1, 'b': 2, 'c': 3}
