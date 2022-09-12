import controller
import view

def menu():
    choice = view.menu()
    if choice == '1':
        view.view_contacts() 
        ent = input("Нажмите Enter что бы продолжить ...")
        menu()
    elif choice == '2':
        name = input('Введите имя: ')
        phone = input('Введите номер телефона: ')
        email = input('Введите E-mail: ')
        p = controller.add_contact(name, phone, email)
        print(p)
        ent = input("Нажмите Enter что бы продолжить ...")
        menu()
    elif choice == '3':
        p = controller.find_contact(input("Введите id: "))
        print(p)
        ent = input("Нажмите Enter что бы продолжить ...")
        menu()
    elif choice == '4':
        contact_id = input('Введите id: ')
        name = input('Введите новое имя: ')
        phone = input('Введите новый номер телефона: ')
        email = input('Введите новый E-mail: ')
        p = controller.edit_contact(contact_id, name, phone, email)
        print(p)
        ent = input("Нажмите Enter что бы продолжить ...")
        menu()
    elif choice == '5':
        p = controller.del_contact(input("Введите id: "))
        print(p)
        menu()
    elif choice == '6':
        p = controller.import_contacts(input("\n\n\nВведите путь к импортируемому файлу: "))
        print(p)
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
        p = controller.exel_create()
        print(p)
    elif choice == '2':
        p = controller.html_create()
        print(p)
    elif choice == '3':
        p = controller.json_create()
        print(p)
    elif choice == '4':
        return
    else:
        print("Ошибка ввода. Пожалуйста выберите [от 1 до 4]\n")
