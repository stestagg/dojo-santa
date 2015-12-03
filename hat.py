import os
import json

def get_users():
    current_directory = os.path.dirname(__file__)
    users_db = os.path.join(current_directory, 'users.json')
    with open(users_db) as fh:
        return json.load(fh)


def add(name):
    users = get_users()
    pass

def assign(name):
    pass

def remove(name):
    pass

if __name__ == "__main__":
    print get_users()
