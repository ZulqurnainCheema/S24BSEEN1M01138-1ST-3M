#I "1138" was the first to make this program Sir! at 12:48,24/5/2024
def calculator():
  try:
    Num1 = int(input("Put your number here:"))
    Num2 = int(input("Put your second number here:"))
    opt = input('Specify the math operator here: ')
    if (opt == "+"):
      print(Num1 + Num2)
    elif (opt == "-"):
      print(Num1 - Num2)
    elif (opt == "*"):
      print(Num1 * Num2)
    elif (opt == "/"):
      print(Num1 / Num2)
    else:
      print("Invalid operator")
  except ValueError:
    print("Please provide the right integer value")
  except ZeroDivisionError:
    print("Can't divide by zero")
  option_to_rerun = input("Do you want to rerun the calculator? (y/    n)")
  if option_to_rerun == "y":
      calculator()
  elif option_to_rerun == "n":
      print("calculator closing!")
calculator()
