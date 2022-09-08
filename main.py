import controller
import view

view.hi()

def menu():
    choice = view.menu()
    if choice == 1:
        view.view_contacts() 
        ent = input("Нажмите Enter что бы продолжить ...")
        menu()
    elif choice == 2:
        controller.add_contact()
        ent = input("Нажмите Enter что бы продолжить ...")
        menu()
    elif choice == 3:
        controller.find_contact()
        ent = input("Нажмите Enter что бы продолжить ...")
        menu()
    elif choice == 6:
        sub_menu_import()
        menu()
    elif choice == 7:
        sub_menu_export()
        menu()
    elif choice == 8:
        view.bye()
    else:
        print("Ошибка ввода. Пожалуйста выберите [от 1 до 8]\n")
        ent = input("Нажмите Enter что бы продолжить ...")
        menu()
        
def sub_menu_import():
    controller.import_contacts(input("\n\n\nВведите пусть к экспортируему файлу: "))
    return

def sub_menu_export():
    choice = view.sub_menu_export()
    if choice == 1:
        controller.exel_create()
    elif choice == 2:
        controller.html_create()
    elif choice == 3:
        controller.json_create()
    elif choice == 4:
        return
    else:
        print("Ошибка ввода. Пожалуйста выберите [от 1 до 4]\n")

menu()

