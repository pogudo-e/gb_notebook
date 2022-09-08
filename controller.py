import time

def file_name():
    '''DATABASE . TXT'''
    return 'database.txt'

# Заглушки
def import_contacts(n):
    print("ok", n)

def exel_create():
    print("ok")

def json_create():
    print("ok")

def find_contact():
    ''' Для поиска '''
    print("ok")


def add_contact():	
    name = input('Введите имя: ')
    phone = input('Введите номер телефона: ')
    email = input('Введите E-mail: ')
    contact = (find_id() + " " + name + " " + phone + " " + email + "\n")
    file1 = open(file_name(), "a+")
    file1.write(contact)
    file1.close
    print( "Контакт:\n " + contact + "\nУспешно добавлен!")




def contact_array():
    '''Full array DB objects: [[1,2,3][1,2,3][1,2,3]]'''
    file1 = open(file_name())
    file1.close
    res = []
    for line in file1:
        arr = line.split()
        res.append(arr)
    return res

def find_id():
    '''Folling the maximum identificator max < id '''
    count = 1
    arr = contact_array()
    for i in range(0, len(arr)):
        if int(arr[i][0]) > count:
            count = int(arr[i][0])  
    return str(count+1)

def html_create():
    mas = contact_array()
    style = '<style>table{font-family:arial,sans-serif;border-collapse:collapse;width:100%}td,th{border:1px solid #ddd;text-align:left;padding:8px}tr:nth-child(even){background-color:#ddd}</style>'
    html = '<html>\n  <head>{}</head>\n  <body>\n'.format(style)
    html += '<h2>HTML Table</h2>'
    html += '<table>\n<tr><th>ID</th><th>Name</th><th>Phone</th><th>Email</th></tr>'
    for i in range(0, len(mas)):
        html += '<tr>\n<td>{}</td>\n<td>{}</td>\n<td>{}</td>\n<td>{}</td>\n</tr>'.format(mas[i][0], mas[i][1], mas[i][2], mas[i][3])
    html += '\n</table>\n</body>\n</html>'
    time_string = time.strftime("%m-%d-%Y-%H-%M", time.localtime())
    t = 'export/{}.html'.format(time_string)
    with open(t, 'w') as page:
        page.write(html)
    print('Экспорт прошел успешно :)')
    return html

