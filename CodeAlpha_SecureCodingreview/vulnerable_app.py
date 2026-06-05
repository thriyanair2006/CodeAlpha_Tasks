users = {
    "admin": "admin123",
    "user": "password"
}

username = input("Enter Username: ")
password = input("Enter Password: ")

if username in users and users[username] == password:
    print("Login Successful")
else:
    print("Invalid Credentials")

print("Current Users Database:", users)