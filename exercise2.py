def checkMail(mail):
    if ("@") and (".") in mail:
        return True
    else:
        return False

email = input("Enter your e mail:\n")
if checkMail(email) == True:
    print("This e-mail is valid.")
else:
    print("Sorry, this is not a valid mail.")
