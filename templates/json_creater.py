import json
import time

def new_json():
    result = []
    with open('database.txt', 'r', encoding='utf-8') as f:
        for i, line in enumerate(f):
            if i == 0:
                continue
            contacts = line.split()
            result.append(json.dumps({'id': contacts[0], 'name': contacts[1], 'phone': contacts[2], 'mail': contacts[3]}, ensure_ascii=False))
    result = '\n'.join(result)
    time_string = time.strftime("%m-%d-%Y-%H-%M", time.localtime())
    t = 'export/{}.json'.format(time_string)
    with open(t, 'w') as page:
        page.write(result)
    return True