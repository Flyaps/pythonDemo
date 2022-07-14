def f(a, b, /, c, d, *, e, g):
   print(a, b, c, d, e, g)


# The following is a valid call:
f(10, 20, 30, d=40, e=50, g=60)


# However, these are invalid calls:
f(10, b=20, c=30, d=40, e=50, g=60)   # b cannot be a keyword argument
f(10, 20, 30, 40, 50, g=60)           # e must be a keyword argument
