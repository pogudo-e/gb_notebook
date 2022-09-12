import sys
import controller

def view_contacts():
    ''' Show full contact list '''
    file_contents = controller.array(controller.file_name())
    if len(file_contents) == 0:
        print("Ой, кажется тут пусто :(")
    else:
        print()
        for i in range(0, len(file_contents)):
            for i2 in range(0, len(file_contents[i])):
                print(file_contents[i][i2], end=' ')
            print()
    print()


def menu():
    data = [" 1. Просмотр ", " 2. Добавить ", " 3. Искать ", " 4. Редактировать ", " 5. Удалить ", " 6. Импорт ", " 7. Экспорт ", " 8. Exit "]
    form = '-' * 14 + '+' + '-' * 13 + '+' + '-' * 11 + '+' + '-' * 18 + '+' + '-' * 12 + '+' + '-' * 11 + '+' + '-' * 12 + '+' + '-' * 10
    print(form +'\n|{0:}|{1:}|{2:}|{3:}|{4:}|{5:}|{6:}|{7:}|'.format(*data) + '\n' + form)
    return input("Пожалуйста, сделайте выбор: ")


def sub_menu_export():
    print("\n\n\nДля экспорта данных пожалуйста выберите формат из представленных ниже.")
    data = [" 1. Exel ", " 2. Html ", " 3. Json ", " 4. Назад "]   
    form = '-' * 10 + '+' + '-' * 9 + '+' + '-' * 9 + '+' + '-' * 11 
    print(form + '\n|{0:}|{1:}|{2:}|{3:}|'.format(*data) + '\n' + form)
    return input("Пожалуйста, сделайте выбор: ")


def hi():
    print("\nПривет, добро пожаловать в наш маленький справочник (^-^)\n")


def bye():    
	print("**************************************************")
	print("Спасибо что воспользовались нашим справочником")
	print("Будем рады видеть Вас снова!")
	print("**************************************************")
	sys.exit("\nХорошего дня!")

