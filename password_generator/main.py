import logic
from cryptography.fernet import Fernet

key = Fernet.generate_key()
print(key)

fernet = Fernet(key)

def encrypt_password(password):
  encoded_message = fernet.encrypt(password.encode())
  return encoded_message

def decrypt_message(encoded_password):
  decoded_message = fernet.decrypt(encoded_password).decode()
  return decoded_message


no_of_lower = int(input("Please enter the number of lower letters :"))
no_of_upper = int(input("Please enter the number of upper letters: "))
no_of_symbols = int(input("Please enter the number for symbols: "))

password_generator = logic.Password_generator(no_of_lower=no_of_lower,no_of_upper=no_of_upper,no_of_symbols=no_of_symbols)

password_generated = password_generator.join_list_and_display_list()
print(password_generated)

response = input("Please enter whether do u want to encode password or not. Please enter yes or no: ").lower()

if response == "yes":
  to_display = encrypt_password(password_generated)
  print(f"Your encoded password is: {to_display}")

