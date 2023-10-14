# collect email from user
# splt the email using @, and get username for the first part
#  get domain for the second part by splitting using .,

def main():
    print("Welcome to the email slicer")
    print("")

    email_input = input("Enter your email address:")

    (username, domain) = email_input.split("@")
    (domain, extension) = domain.split(".")

    print("Username: ", username)
    print("Domain: ", domain)
    print("Extension: ", extension)

    print("\n")
    print("\n")


while True:
    main()
