import hashlib

users = {
    "admin": hashlib.sha256("admin123".encode()).hexdigest(),
    "user": hashlib.sha256("password".encode()).hexdigest()
}

username = input("Enter Username: ")
password = input("Enter Password: ")

hashed_password = hashlib.sha256(password.encode()).hexdigest()

if username in users and users[username] == hashed_password:
    print("Login Successful")
else:
    print("Invalid Credentials")