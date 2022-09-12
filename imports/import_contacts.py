from ..controller import array, add_contact
# На вход получает пусть к файлу формата: Имя Телефон Емаил (через пробелы). Построчно записывает эти значения в БД
def new_import(name):
    db = array(name)
    for i in range(0, len(db)):
            add_contact(db[i][0], db[i][1], db[i][2])
    return True