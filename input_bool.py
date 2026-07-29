username = "preeshaan"
password = "ABC"
show_password = input("Do you want to show password?")

if (show_password == "Yes") or (show_password == "yes"):
    print("Username: ", username, " and password is: ", password)
else:
    print("Username: ", username)