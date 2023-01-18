from art import logo
from replit import clear
#addition
def add(n1, n2):
  return n1 + n2

#subtraction
def subtract(n1, n2):
  return n1 - n2

#multiply
def multiply(n1, n2):
  return n1 * n2

#divide
def divide(n1, n2):
  return n1 / n2

def modulus(n1, n2):
  return n1 % n2

def floordivide(n1, n2):
  return n1 // n2
  
operations = {
  "*": multiply,
  "-": subtract,
  "+": add,
  "/": divide,
  "//": floordivide,
  "%": modulus,
}

def calculator():
  print(logo)
  num1 = float(input("Enter the first number: "))

  should_continue = False
  while not should_continue:
    
    for operator in operations:
      print(operator)
  
    operation_type = input("Pick an operator: ")
    num2 = float(input("Enter the next number: "))
    to_perform = operations[operation_type]
    answer = to_perform(num1, num2)
    print(f"{num1} {operation_type} {num2} = {answer}")

    if input(f"Type 'yes' to continue calculating with {answer}.  or  type 'no' to start a new calculation \n").lower() == "yes":
      num1 = answer
    else:
      should_continue = True
      clear()
      calculator()
calculator()
   
