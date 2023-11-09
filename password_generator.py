import string
import random


characters = list(string.ascii_letters + string.digits + "!@#$%&*()\?/")


def generate_password():
    password_length = int(input("Enter the password length: "))
    random .shuffle(characters)
    password = []
    for character in range(password_length):
        password.append(random.choice(characters))

    random.shuffle(password)

    password = "".join(password)
    print(password)


option = input("Do you want to generate a password (Yes/No): ").lower()

if option == 'yes':
    generate_password()
elif option == 'no':
    print("program ended")
    quit()
else:
    print("Enter valid choices (Yes/No)")
    quit()
