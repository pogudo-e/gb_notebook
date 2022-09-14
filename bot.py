from view import *
from controller import *
import telebot

bot = telebot.TeleBot("5476194400:AAE9AhXJXQcBuyGe2moWYXqkHQ5xfgLAuyk")

# Приветственное сообщение при запуске бота
@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.send_message(message.chat.id, hi() + '\n' + 'Предлагаю начать с команды меню: /menu\nА вот и само меню:\n' + menu_bot())

# Меню со списком команд
@bot.message_handler(commands=['menu'])
def send_menu(message):
    bot.send_message(message.chat.id, menu_bot())

# Вывод списка контактов
@bot.message_handler(commands=['view'])
def send_view(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, view_contacts())
    bot.send_message(chat_id, 'Что-нибудь еще?\n' + menu_bot())

# Инфо о командах
@bot.message_handler(commands=['help'])
def send_help(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, help())
    bot.send_message(chat_id, 'Что-нибудь еще?\n' + menu_bot())


# Добавление контактов
user_dict = {}
class User:
    def __init__(self, name):
        self.name = name
        self.phone = None
        self.mail = None

@bot.message_handler(commands=['add'])
def send_welcome(message):
    msg = bot.reply_to(message, """\
Введите имя
""")
    bot.register_next_step_handler(msg, process_name_step)

def process_name_step(message):
    chat_id = message.chat.id
    name = message.text
    user = User(name)
    user_dict[chat_id] = user
    msg = bot.reply_to(message, 'Введите номер')
    bot.register_next_step_handler(msg, process_phone_step)


def process_phone_step(message):
    chat_id = message.chat.id
    user = user_dict[chat_id]
    user.phone = message.text
    msg = bot.reply_to(message, 'Введите mail')
    bot.register_next_step_handler(msg, process_mail_step)

def process_mail_step(message):
    chat_id = message.chat.id
    user = user_dict[chat_id]
    user.mail = message.text
    add_contact(user.name, user.phone, user.mail)
    bot.send_message(chat_id, 'Успешно добавлено!\nИмя: ' + user.name + '\nТелефон: ' + str(user.phone) + '\nMail: ' + user.mail)



# Удаление контатов
@bot.message_handler(commands=['del'])
def delete_contacts(message):
    msg = bot.reply_to(message, """\
Введите id который хотите удалить:
""")
    bot.register_next_step_handler(msg, process_del_step)

def process_del_step(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, del_contact(str(message.text)))
    bot.send_message(chat_id, 'Что-нибудь еще?\n' + menu_bot())


# Поиск контатов
@bot.message_handler(commands=['find'])
def find_contacts(message):
    msg = bot.reply_to(message, """\
Введите искомый id:
""")
    bot.register_next_step_handler(msg, process_find_step)

def process_find_step(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, find_contact(str(message.text)))


# Импорт контактов. Просто отправляешь боту файл
@bot.message_handler(content_types=['document'])
def upload_doc(message):

    doc = bot.get_file(message.document.file_id)
    doc_name = message.document.file_name
    doc_path = doc.file_path
    doc_as_file = bot.download_file(doc_path)

    with open(f'{doc_name}', 'wb') as new_file:
        new_file.write(doc_as_file)
    msg = import_contacts(f'{doc_name}')
    bot.send_message(message.chat.id, msg)





bot.infinity_polling()