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

def html_create():
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


def find_id():
    '''Folling the maximum id'''
    file1 = open(file_name())
    file1.close
    count = 1
    for line in file1:
        arr = line.split()
        if int(arr[0]) > count:
            count = int(arr[0])  
    return str(count+1)