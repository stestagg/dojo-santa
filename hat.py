import os
import json
import random

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

def get_undrawn_users():
    return [k for k, v in get_users().items() if v is None]

def get_unassigned_users():
    users = get_users()
    from_users = users.keys()
    to_users = users.values()
    return set(from_users) - set(to_users)

def add(name):
    users = get_users()
    if name in users:
        raise ValueError("User already in hat")
    users[name] = None
    update_users(users)


def assign(name):
    users = get_users()
    if users[name] is not None:
        return users[name]
    unassigned = get_unassigned_users()
    if name in unassigned:
        unassigned.remove(name)
    unassigned = list(unassigned)
    random.shuffle(unassigned)
    partner = unassigned[0]
    users[name] = partner
    update_users(users)
    return partner


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
    print get_undrawn_users()
    print assign("matt")
    print get_undrawn_users()
