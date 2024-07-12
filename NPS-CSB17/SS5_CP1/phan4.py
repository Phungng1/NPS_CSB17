# Bai 1
username = input("Enter your username: ")
password = input("Enter your password: ")
email = input("Enter your email: ")
if (username != '') and (password != '') and (email != ''):
    print("Register successfully")
else:
    print("Register unsuccessfully, please try again")
# Bai 2
username = input("Enter your username: ")
password = input("Enter your password: ")
repassword = input("Reenter your password: ")
email = input("Enter your email: ")
if (username != '') and (password != '') and (email != '') :
    while repassword != password:
        print("Password not match, please try again")
        repassword = input("Reenter your password: ")
    print("Register successfully")
else:
    print("Register unsuccessfully, please try again")
# Bai 3
username = input("Enter your username: ")
password = input("Enter your password: ")
while True:

    if len(password)>=8:
        has_letter = False
        has_digit = False
        for char in password:
            if char.isalpha():
                has_letter = True
            if char.isdigit():
                has_digit = True
        if has_letter and has_digit : 
            break
    else:
        print("Password must contain at least 8 characters including letters and numbers")
        password = input("Renter your password: ")

repassword = input("Confirm your password: ")
while True:
    if repassword == password:
        break
    else:
        print("Password not match, please try again")
        repassword = input("Reconfirm your password: ")

email = input("Enter your email: ")
while True:
    if ("@" in email) and ("." in email):
        break
    else:
        print("Email must contain @ and .")
        email = input("Reenter email: ")

print("Registered successfully")
        



