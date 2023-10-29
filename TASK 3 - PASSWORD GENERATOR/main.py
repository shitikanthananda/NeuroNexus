import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
print("NeuroNexus Password Generator")
input_letters = int(input("How many letters would you like in your password?\n")) 
input_symbols = int(input("How many symbols would you like?\n"))
input_numbers = int(input("How many numbers would you like?\n"))

password_list = []

for i in range(1, input_letters + 1):
  password_list.append(random.choice(letters))

for i in range(1, input_symbols + 1):
  password_list.append(random.choice(symbols))

for i in range(1, input_numbers + 1):
  password_list.append(random.choice(numbers))

random.shuffle(password_list)

password = ""
for i in password_list:
  password += i

print(f"Your generated password is: {password}")
