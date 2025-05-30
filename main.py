import telebot
from telebot import types
import datetime
import gdown
import shutil
import pandas as pd


bot = telebot.TeleBot('7449098710:AAGqxBE-es6LVge8sF2CRWNABnPiJ1-LEBw')
today = datetime.date.today()
tomorrow = today + datetime.timedelta(days=1)
format_t = tomorrow.strftime("%d-%m-%y")
url = "https://drive.google.com/drive/folders/1qa2tjL7gQGSKy-vbe7JCaPtFqJZJXhJL"
template = "{teath} - {kab} "
res = ".xls"
format = format_t + res


#def load_schedule(filename):
  #  df = pd.read_excel(filename)  # Используй только дату без расширения

   # return df

#def get_schedule_for_group(df, group_name):
 #   rows = df.query(f"Группа == '{group_name}'")
 #   return rows




@bot.message_handler(commands=['start'])
def start(message):
    gdown.download_folder("https://drive.google.com/drive/folders/1qa2tjL7gQGSKy-vbe7JCaPtFqJZJXhJL")
    download_1()
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Р-142', callback_data='/Р-142')
    btn2 = types.InlineKeyboardButton('Р-143', callback_data='/Р-143')
    btn3 = types.InlineKeyboardButton('Р-232', callback_data='/Р-232')
    btn4 = types.InlineKeyboardButton('Р-322', callback_data='/Р-322')
    btn5 = types.InlineKeyboardButton('Р-411', callback_data='/Р-411')
    btn6 = types.InlineKeyboardButton('Сн-323', callback_data='/Сн-323')
    btn7 = types.InlineKeyboardButton('Сн-232', callback_data='/Сн-232')
    btn8 = types.InlineKeyboardButton('Ан-143', callback_data='/Ан-143')
    btn9 = types.InlineKeyboardButton('Ан-233', callback_data='/Ан-233')
    btn10 = types.InlineKeyboardButton('Ан-234', callback_data='/Ан-234')
    btn11 = types.InlineKeyboardButton('Ан-322', callback_data='/Ан-322')
    btn12 = types.InlineKeyboardButton('Ан-323', callback_data='/Ан-323')
    btn13 = types.InlineKeyboardButton('Ад-321', callback_data='/Ад-321')
    btn14 = types.InlineKeyboardButton('ОП-141', callback_data='/ОП-141')
    btn15 = types.InlineKeyboardButton('ОПд-231', callback_data='/ОПд-231')
    btn16 = types.InlineKeyboardButton('Сн-142', callback_data='/Сн-142')
    btn17 = types.InlineKeyboardButton('Сн-143', callback_data='/Сн-143')
    btn18 = types.InlineKeyboardButton('Сн-233', callback_data='/Сн-233')
    btn19 = types.InlineKeyboardButton('Сн-234', callback_data='/Сн-234')
    btn20 = types.InlineKeyboardButton('Сн-324', callback_data='/Сн-324')
    btn21 = types.InlineKeyboardButton('Сн-325', callback_data='/Сн-325')
    btn22 = types.InlineKeyboardButton('Э-321', callback_data='/Э-321')
    btn23 = types.InlineKeyboardButton('Э-411', callback_data='/Э-411')
    btn24 = types.InlineKeyboardButton('Р-141', callback_data='/Р-141')
    btn25 = types.InlineKeyboardButton('Р-231', callback_data='/Р-231')
    btn26 = types.InlineKeyboardButton('Р-321', callback_data='/Р-321')
    btn27 = types.InlineKeyboardButton('Р-412', callback_data='/Р-412')
    btn28 = types.InlineKeyboardButton('С-141', callback_data='/С-141')
    btn29 = types.InlineKeyboardButton('С-231', callback_data='/С-231')
    btn30 = types.InlineKeyboardButton('С-321', callback_data='/С-321')
    btn31 = types.InlineKeyboardButton('С-322', callback_data='/С-322')
    btn32 = types.InlineKeyboardButton('С-411', callback_data='/С-411')
    btn33 = types.InlineKeyboardButton('Э-141', callback_data='/Э-141')
    btn34 = types.InlineKeyboardButton('А-141', callback_data='/А-141')
    btn35 = types.InlineKeyboardButton('А-142', callback_data='/А-142')
    btn36 = types.InlineKeyboardButton('А-231', callback_data='/А-231')
    btn37 = types.InlineKeyboardButton('А-232', callback_data='/А-232')
    btn38 = types.InlineKeyboardButton('А-321', callback_data='/А-321')
    btn39 = types.InlineKeyboardButton('А-411', callback_data='/А-411')
    btn40 = types.InlineKeyboardButton('Т-141', callback_data='/Т-141')
    btn41 = types.InlineKeyboardButton('Т-231', callback_data='/Т-231')
    btn42 = types.InlineKeyboardButton('Т-321', callback_data='/Т-321')
    btn43 = types.InlineKeyboardButton('Т-411', callback_data='/Т-411')
    btn44 = types.InlineKeyboardButton('Т-412', callback_data='/Т-412')
    btn45 = types.InlineKeyboardButton('Э-231', callback_data='/Э-231')
    btn46 = types.InlineKeyboardButton('Эд-231', callback_data='/Эд-231')
    btn47 = types.InlineKeyboardButton('Эд-321', callback_data='/Эд-321')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12, btn13, btn14, btn15, btn16,
               btn17, btn18, btn19, btn20, btn21, btn22, btn23, btn24, btn25, btn26, btn27, btn28, btn29, btn30, btn31,
               btn32, btn33, btn34, btn35, btn36, btn37, btn38, btn39, btn40, btn41, btn42, btn43, btn44, btn45, btn46,
               btn47)
    bot.send_message(message.from_user.id, 'Привет я бот Типк! Я вывожу расписание вашей группы.Выберите вашу группу.', reply_markup=markup)

def download_1():
    try:
        shutil.move(rf"C:\Users\Maksz\PycharmProjects\telebot_raspis\Расписание\{format}",
                   rf"C:\Users\Maksz\PycharmProjects\telebot_raspis\ras_doc")
        shutil.rmtree(rf"C:\Users\Maksz\PycharmProjects\telebot_raspis\Расписание")
        print("Файл успешно перемещён.")
    except FileNotFoundError:
        print("Файл не найден!")
        shutil.rmtree(rf"C:\Users\Maksz\PycharmProjects\telegram_bot\Расписание", dir_fd=None)





@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.message:
        if call.data == '/Р-142':
            groop = call.data.upper()
            df = pd.read_excel(rf"C:\Users\Maksz\PycharmProjects\telebot_raspis\ras_doc\{format})",
                               skiprows = 6, usecols='D:S', header=4, nrows=8)
            df = df.drop(how='all')
            temp = {}
            for row_1, row_2 in zip(df[groop], df ["Unnamed: 6"]):
                if not groop in temp:
                    temp[groop] = []
                if pd.notna(row_1) and row_1 != "-":
                    if pd.isna(row_2):
                        row_2 = ""
                        temp[groop].append((row_1, row_2))
            text = ""
            for i in temp[groop]:
                if i[1] is not None:
                    kab = str(i[1])
                    kab = kab.replace("-", "")
                    text += template.format(teath=i[0], kab=kab) + "\n"
                else:
                    text += template.format(teath=i[0], kab="") + "\n"
                bot.send_message(call.message.chat.id, f'Расписание таково')
                print(format)







bot.infinity_polling()
