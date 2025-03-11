import random
letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numbers = ["0","1","2","3","4","5","6","7","8","9"]
symbols = ["@","#","$","%","^","&","!"]
print("welcome to passwordGenerator:")
new_letters = int(input("how many letters would you like in password"))
new_numbers= int(input("how many numbers would you like in password"))
new_symbols = int(input("how many symbols would you like in password"))
password = " "
for char in range(0,new_letters):
    password += random.choice(letters)
for char in range(0,new_numbers):
    password += random.choice(numbers)
for char in range(0,new_symbols):
    password += random.choice(symbols)
print(password)



