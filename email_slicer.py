def email_slicer():
    email_input = input("Enter your email: ")

    username, domain = email_input.split('@')
    domain, extension = domain.split('.')
    print(f"Username: {username}")
    print(f"Domain: {domain}")
    print(f"Extension: {extension}")


email_slicer()
