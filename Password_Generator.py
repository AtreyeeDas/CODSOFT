import random
import string

# Define character sets for password generation
letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation

def generate_password(length):
  # Create a pool of available characters
  character_pool = letters + digits + symbols

  # Generate random password characters
  password = "".join(random.sample(character_pool, length))

  return password

def main():
  # Prompt user for password length
  password_length = int(input("Enter desired password length (8-32 characters): "))

  # Validate length
  if password_length < 8 or password_length > 32:
    print("Error: Password length must be between 8 and 32 characters.")
    return

  # Generate and display password
  password = generate_password(password_length)
  print(f"Your generated password: {password}")
if __name__ == "__main__":
  main()
