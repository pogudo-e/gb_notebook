# Телефонный справочник

## Описание задачи.
Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах.
Под форматами понимаем структуру файлов, например: в файле на одной строке хранится одна часть записи, пустая строка - разделитель.

---
## Команда

- Женя (https://github.com/pogudo-e)
- Карэн (https://github.com/karenyaylyan)

---
## Структура приложения (модули)

- main - Точка входа в консольную версию (*Женя*)
- bot - Точка входа в программу телеграм бота (*Женя*)
- logger - Логироваине данных: add, del, edit (*Карэн*)
- html_creater - Генерирует html файл, сохраняет в папке export (*Женя*)
- json_creater - Генерирует json файл сохраняет в папке export (*Карэн*)
- import_contacts - Испортирует данные из указанного файла с разделителем (перевод строки), Присваивает уникальный id и построчно добавляет в БД (*Женя*)
- database.txt - База данных содержащая в себе уникальный  id, name, phone, email. Разделителем служит перевод строки (*Карэн*)
- add_contact - Добавление нового контакта (*Женя*)
- edit_contact - Редактироваине существующего контакта по id (*Карэн*)
- del_contact - Удаление контакта по id (*Карэн*)
- view_contacts - Вывод полного списка (*Женя*)

---
## Как запустить проект (рекомендуем использовать VSC)

### Для запуска с помощью консоли:
- Скачать проект в локальный репозиторий с помощью команды:

        git clone https://github.com/pogudo-e/gb_notebook

-  Перейти в папку с проектом
        
        cd gb_notebook

- Установить необходимые для работы зависимости:

        pip install -r requirements.txt

- В консоли ввести команду для запуска телеграм бота
        
        python3 bot.py

- Перейти в по адресу: https://t.me/complimentik_bot и нажать /start 

- Или команду для запуска консольного приложения
        
        python3 main.py

- Следовать инструкциям в консоли (телеграм бота при этом необходимо остановить или производить запуск в другом терминале).
