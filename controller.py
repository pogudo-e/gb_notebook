import logger
from templates.html_creater import new_html
from templates.json_creater import new_json
from imports.import_contacts import new_import

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
    return "ok"

def json_create():
    if new_json():
        return "Экспорт прошел успешно"

def html_create():
    if new_html():
        return "Экспорт прошел успешно"

def import_contacts():
    if new_import():
        return 'Импорт прошел успешно'

def find_contact(contact_id):
    is_in_file = False
    with open('database.txt', 'r') as f:
        for line in f:
            contacts = line.strip().split()
            if contact_id == contacts[0]:
                is_in_file = True
                print(line)
        if not is_in_file:
            return 'Контакт не найден'



# На взод получает три переменные: Имя, телефон и емаил. Присваивает уникальный идентификатор и записывает в БД
def add_contact(name, phone, email):	
    contact = (find_id() + " " + name + " " + phone + " " + email + "\n")
    file1 = open(file_name(), "a+")
    file1.write(contact)
    logger.add_logger(contact)
    file1.close
    return "Контакт:\n " + contact + "\nУспешно добавлен!"

def del_contact(contact_id):
    is_in_file = False
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
            logger.del_logger(contact_to_del)
            return f'Контакт:\n {contact_to_del} \nУспешно удалён!'
        else:
            return 'Контакт не найден'

# Редактироваине контактов
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
            logger.edit_logger(contact_to_edit)
            return f'Контакт:\n {contact_to_edit} \nУспешно изменён!'
        else:
            return 'Контакт не найден' 


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