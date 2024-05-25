given_number = int(input("Enter a number: "))
def recusive_sum(n):
  if n < 0:
    print("number should be positive integer")
  else:
    try:
      if n == 0:
        return 0
      else:
        return n + recusive_sum(n - 1)
    except ValueError:
      print("Provide and interger")
result = recusive_sum(given_number)
print(result)
