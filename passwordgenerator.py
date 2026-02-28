import random


#Variables
symbols = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
len = int(input("Please enter the password lenght:  "))
password = ""

#Loop
for i in range(len):
    random_character = random.choice(symbols)
    password = password + random_character

#Console 
print("Generated password:", password)

