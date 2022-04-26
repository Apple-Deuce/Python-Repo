#the following code is not yet complete

from cryptography.fernet import Fernet

 

#The enclosed function and call should only be ran once, before starting the password manager
'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


write_key()
'''

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


key = load_key()
fer = Fernet(key)

def view():
    with open('encryptedpasswords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            account, user, passw = data.split("|")
            print("Account:", account, "| Username/Email:", user, "| Password:", fer.decrypt(passw.encode()).decode())

def add():
    identity = input('What is this account for?: ')
    name = input('Username/Email: ')
    pwd = input("Password: ")

    with open('encryptedpasswords.txt', 'a') as f:
        f.write(identity + "|" + name + "|" + fer.encrypt(pwd.encode().decode()) + "\n")

while True:
    mode = input("add,view or q to quit: ")
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid Input. Please enter 'add' or 'view'.")
        continue