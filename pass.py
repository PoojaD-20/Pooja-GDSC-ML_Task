import random
import string
pass_length=int(input("Enter the length of the password: "))
lists=string.ascii_letters + string.digits + string.punctuation
# print(lists)
password=""
if(pass_length<8):
    print("Password should have at least 8 characters")
else:
    print("Your password is: ")
    for i in range(pass_length):
        password+=random.choice(lists)
    print(password)        
