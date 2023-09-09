import sqlite3


def CommitAndClose():
    db.commit()
    db.close()


def Add():
    print(" Add new number ".center(25, "-"))
    name = input("Enter your name: ").capitalize()
    number = input("Enter your number: ")

    cr.execute(
        f"SELECT * FROM contact WHERE name = '{name}' AND ID = {user_id} OR number = '{number}' AND ID = {user_id}")
    row = cr.fetchone()
    if row == None:
        cr.execute(
            f"INSERT INTO contact(name, number, ID) VALUES('{name}', '{number}', {user_id})")
        print("Added successfully")
    else:
        if row[0] == name:
            print("Sorry this name is already exist")
        else:
            print("Sorry this number is already exist")


def Delete():
    print(" Delete a number ".center(25, "-"))
    name = input("Enter the name: ").capitalize()

    cr.execute(f"DELETE FROM contact WHERE name = '{name}' AND ID = {user_id}")
    print("Deleted successfully")


def Update():
    print(" Update a number ".center(25, "-"))
    name = input("Enter the name: ").capitalize()
    number = input("Enter your number: ")

    cr.execute(
        f"UPDATE contact SET number = '{number}' WHERE name = '{name}' AND ID = {user_id}")
    print("Updated successfully")


def Search():
    print(" Search for a number ".center(25, "-"))
    name = input("Enter the name: ").capitalize()

    cr.execute(
        f"SELECT * FROM contact WHERE name = '{name}' AND ID = {user_id}")
    row = cr.fetchone()

    if row != None:
        print(f"{row[1]}")
    else:
        print("Sorry Cannot find this name")
        print("Do You Want Add This Contact?")
        v = input("Y/N \n").upper()
        if (v == 'Y'):
            Add()


def Show():
    cr.execute(f"SELECT * FROM contact WHERE ID = '{user_id}'")
    contact = cr.fetchall()
    n = 0
    for row in contact:
        print(f"Name: {row[0]}, Number: {row[1]}")
        n += 1
    if n == 0:
        print("Contact List Is Empty")

def Operation():
    value = input("Enter A Command: ").strip().lower()

    if value == 'a':
        Add()
    elif value == 'd':
        Delete()
    elif value == 'u':
        Update()
    elif value == 's':
        Search()
    elif value == 'c':
        Show()
    elif value == 'q':
        print("Exited..")
        exit()
    else:
        print("Sorry This Command Is Not Defined")
        Operation()

    print("\n----------------\n")
    Operation();


    db.commit()


user_id = 1

db = sqlite3.connect("data.db")

cr = db.cursor()

cr.execute(
    "CREATE TABLE if not exists contact (name TEXT, number TEXT, ID INTEGER)")

print("""A/a => Add new contact
D/d => Delete Contact
U/u => Update Contact
S/s => Search Cor Contact
C/c => Show All Contact
Q/q => Exit The Program""")


print("\n")

Operation()

CommitAndClose()