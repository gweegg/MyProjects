def add(x, y):
  '''Adds two numbers'''
  return x + y


def subtract(x, y):
  '''Subtracts two numbers'''
  return x - y


def multiply(x, y):
  '''Multiplies two numbers'''
  return x * y


def divide(x, y):
  '''Divides two numbers'''
  if y == 0:
    return "Cannot divide by zero!"
  else:
    return x / y

def modulus(x, y):
  '''Returns the remainder of two numbers'''
  if y == 0:
    return "Cannot divide by zero!"
  else:
    return x % y

while True:
  print("Select operation:")
  print("1. Add")
  print("2. Subtract")
  print("3. Multiply")
  print("4. Divide")
  print("5. Modulus")
  print("6. Exit")

  choice = input("Enter choice (1/2/3/4/5/6): ")

  if choice in ('1','2','3','4','5'):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
      print("Result" , add(num1, num2))
    elif choice == '2':
      print("Result:", subtract(num1, num2))
    elif choice == '3':
      print("Result:", multiply(num1, num2))
    elif choice == '4':
      print("Result:", divide(num1, num2))
    elif choice == '5':
      print("Result:", modulus(num1, num2))
    elif choice == '6':
      print("Exiting calculator...")
      break
  else:
    print("Invalid input. Please try again.")
    
