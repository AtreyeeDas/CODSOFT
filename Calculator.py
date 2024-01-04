def main():
  # Prompt user for numbers
  num1 = float(input("Enter first number: "))
  num2 = float(input("Enter second number: "))

  # Prompt user for operation choice
  operation = input("Choose an operation (+, -, *, /): ")

  # Perform operation based on user choice
  result = None
  if operation == "+":
    result = num1 + num2
  elif operation == "-":
    result = num1 - num2
  elif operation == "*":
    result = num1 * num2
  elif operation == "/":
    if num2 == 0:
      print("Error: Division by zero is not allowed.")
    else:
      result = num1 / num2
  else:
    print("Invalid operation.")

  # Print the result if valid operation
  if result is not None:
    print(f"{num1} {operation} {num2} = {result}")

if __name__ == "__main__":
  main()
