Provided_number = int(input("Enter a NATURAL number: "))
def factorial(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n * factorial(n - 1)
factorial(Provided_number)