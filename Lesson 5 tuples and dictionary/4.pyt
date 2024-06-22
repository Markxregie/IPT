credentials = {
    'user1': 'password1',
    'user2': 'password2',
    'user3': 'password3',
    'user4': 'password4',
    'user5': 'password5',
    'user6': 'password6',
    'user7': 'password7',
    'user8': 'password8',
    'user9': 'password9',
    'user10': 'password10'
}
username = input("Enter username: ")
password = input("Enter password: ")

if username in credentials:
    if credentials[username] == password:
        print("Login successful! You are now logged in.")
    else:
        print("Invalid password.")
else:
    print("Invalid username. You are not a valid user of the system.")