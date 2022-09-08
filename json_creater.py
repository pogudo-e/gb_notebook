import json

def json_create():
    with open('database.txt', 'r') as f:
        for i, line in enumerate(f):
            if i == 0:
                continue
            contacts = line.strip().split()
            print(json.dumps({'id': contacts[0], 'phone': contacts[1], 'mail': contacts[2]}))
