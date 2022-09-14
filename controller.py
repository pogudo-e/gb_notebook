import time
import os
import logger

# Имя файла БД. В последующем можно добавить настройки с возможностью смены файла
def file_name():
    '''DATABASE . TXT'''
    return 'database.txt'

# def export_contacts():
#     dir_name = 'export/'
#     i == 1
#     while os.path.exists(dir_name + f'export{i}.txt'):
#         i += 1

#     new_path = dir_name + f'export{i}.txt'
#     with open('database.txt', 'r') as d, open(new_path, 'w') as e:
#         e.write(d.read())
#     print('Экспорт прошел успешно :)')

def exel_create():
    print("ok")

def json_create():
    print("ok")

def find_contact(contact_id):
    is_in_file = False
    res = ''
    with open('database.txt', 'r') as f:
        for line in f:
            contacts = line.strip().split()
            if contact_id == contacts[0]:
                is_in_file = True
                res = line
        if not is_in_file:
            res = 'Контакт не найден'
    return res

# На вход получает пусть к файлу формата: Имя Телефон Емаил (через пробелы). Построчно записывает эти значения в БД
def import_contacts(name):
    db = array(name)
    for i in range(0, len(db)):
            add_contact(db[i][0], db[i][1], db[i][2])
    return 'Импорт заверщен успешно.'

# На взод получает три переменные: Имя, телефон и емаил. Присваивает уникальный идентификатор и записывает в БД
def add_contact(name, phone, email):	
    contact = (find_id() + " " + name + " " + phone + " " + email + "\n")
    file1 = open(file_name(), "a+")
    file1.write(contact)
    logger.add_logger(contact)
    file1.close
    return

def del_contact(contact_id):
    is_in_file = False
    res = ''
    with open('database.txt', 'r') as f:
        contacts = []
        for contact in f:
            contact_lst = contact.split()
            if contact_lst[0] == contact_id:
                contact_to_del = contact 
                is_in_file = True
            else:
                contacts.append(contact)

    with open('database.txt', 'w') as f:
        f.writelines(contacts)
        if is_in_file:
            res = f'Контакт:\n {contact_to_del} \nУспешно удалён!'
            logger.del_logger(contact_to_del)
        else:
            res = 'Контакт не найден'
    return res

# Надо бы сделать как нибудь
def edit_contact(contact_id, name, phone, email):
    is_in_file = False
    with open('database.txt', 'r') as f:
        contacts = ''
        for contact in f:
            contact_lst = contact.split()
            if contact_lst[0] == contact_id:
                contact_to_edit = contact_id + ' ' + name + ' ' + phone + ' ' + email + '\n'
                contacts += contact_to_edit
                is_in_file = True
            else:
                contacts += contact

    with open('database.txt', 'w') as f:
        f.write(contacts)
        if is_in_file:
            print(f'Контакт:\n {contact_to_edit} \nУспешно изменён!')
            logger.edit_logger(contact_to_edit)
        else:
            print('Контакт не найден')  


# На вход получает файл и возвращает двумерный массив
def array(file):
    '''Full array objects: [[1,2,3][1,2,3][1,2,3]]'''
    file1 = open(file)
    file1.close
    res = []
    for line in file1:
        arr = line.split()
        res.append(arr)
    return res

# Находит максимальный id из имеющихся и возвращает id+1
def find_id():
    '''Folling the maximum identificator max < id '''
    count = 1
    arr = array(file_name())
    for i in range(0, len(arr)):
        if int(arr[i][0]) > count:
            count = int(arr[i][0])  
    return str(count+1)

# Из массива формирует html файл и записывает его в папку export с именем файла: текущая дата и время.html
def html_create():
    mas = array(file_name())
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

