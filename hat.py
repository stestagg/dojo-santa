import os
import json

def get_users():
    current_directory = os.path.dirname(__file__)
    users_db = os.path.join(current_directory, 'users.json')
    with open(users_db) as fh:
        return json.load(fh)

def update_users(data):
    current_directory = os.path.dirname(__file__)
    users_db = os.path.join(current_directory, 'users.json')
    with open(users_db, "wb") as fh:
        return json.dump(data, fh)


def add(name):
    users = get_users()
    if name in users:
        raise ValueError("User already in hat")
    users[name] = None
    update_users(users)


def assign(name):
    pass

def remove(name):
    users = get_users()
    if name not in users:
        raise ValueError("User not there hat")
    del users[name]
    for key, value in users.items():
        if value == name:
            users[key] = None
    update_users(users)   

if __name__ == "__main__":
    print get_users()
    add("bill")
    print get_users()
    remove("matt")
    print get_users()
