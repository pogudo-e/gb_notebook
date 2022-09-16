import logger
from app.core import *
from app.export.e_html import *
from app.export.e_json import *

def view_contacts():
    ''' Show full contact list '''
    res = ''
    file_contents = array(file_name())
    if len(file_contents) == 0:
        res = "Ой, кажется тут пусто :("
    else:
        print()
        for i in range(0, len(file_contents)):
            for i2 in range(0, len(file_contents[i])):
                res += file_contents[i][i2] + ' '
            res += '\n'
    return res

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
    res = ''
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
            res = f'Контакт:\n {contact_to_edit} \nУспешно изменён!'
            logger.edit_logger(contact_to_edit)
        else:
            res = 'Контакт не найден'
    return res 

def html_create():
    e_html(array(file_name()))

def json_creater():
    e_json(file_name())