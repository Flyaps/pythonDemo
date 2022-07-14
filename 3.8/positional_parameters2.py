def divmod(a, b, /):
   """Emulate the built in divmod() function"""
   return a // b, a % b


divmod(a=1, b=2)

len(obj='hello')  # The "obj" keyword argument impairs readability
