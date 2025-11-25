# Exercise 6: Brute Force Attack
correct_password = "12345"
max_tries = 5
tries = 0

while tries < tries:
    password = input("Enter the password: ")
    tries += 1

    if password == correct_password:
        print("Access granted")
        break
    else:
        remaining = max_tries -  tries
        if remaining > 0:
            print(f"incorrect password. you have {remaining} attempt(s) left. ")
        else:
            print("too many failed attempts. System locked")
