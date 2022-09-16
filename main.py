import controller
import json_creater
import view

print(view.hi())

def menu():
    
    print(view.menu())
    choice = input("Пожалуйста, сделайте выбор: ")
    if choice == '1':
        print(view.view_contacts()) 
        ent = input("Нажмите Enter что бы продолжить ...")
        menu()
    elif choice == '2':
        name = input('Введите имя: ')
        phone = input('Введите номер телефона: ')
        email = input('Введите E-mail: ')
        print(controller.add_contact(name, phone, email))
        ent = input("Нажмите Enter что бы продолжить ...")
        menu()
    elif choice == '3':
        print(controller.find_contact(input("Введите id: ")))
        ent = input("Нажмите Enter что бы продолжить ...")
        menu()
    elif choice == '4':
        contact_id = input('Введите id: ')
        name = input('Введите новое имя: ')
        phone = input('Введите новый номер телефона: ')
        email = input('Введите новый E-mail: ')
        print(controller.edit_contact(contact_id, name, phone, email))
        ent = input("Нажмите Enter что бы продолжить ...")
        menu()
    elif choice == '5':
        print(controller.del_contact(input("Введите id: ")))
        menu()
    elif choice == '6':
        print(controller.import_contacts(input("\n\n\nВведите путь к импортируемому файлу: ")))
        menu()
    elif choice == '7':
        sub_menu_export()
        menu()
    elif choice == '8':
        view.bye()
    else:
        print("Ошибка ввода. Пожалуйста выберите [от 1 до 8]\n")
        ent = input("Нажмите Enter что бы продолжить ...")
        menu()
        

def sub_menu_export():
    choice = view.sub_menu_export()
    if choice == '1':
        print(controller.html_create())
    elif choice == '2':
        print(json_creater.json_create())
    elif choice == '3':
        return
    else:
        print("Ошибка ввода. Пожалуйста выберите [от 1 до 4]\n")

menu()

