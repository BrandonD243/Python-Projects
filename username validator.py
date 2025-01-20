#USERNAME VALIDATOR

while True:
    username = input("Enter a strong username: ")

    if len(username) > 12:
        print("Your username can't contain more than 12 characters.")
    if username.count(" ") > 0:
        print("Your username can't contain any spaces.")
    if not username.isalpha():
        print("Your username can't contain digits.")
    else:
        print(f"{username} is a successful username!")