# -*- coding: utf-8 -*-
import telegram
from telegram.error import NetworkError, Unauthorized
from time import sleep
from telegram import replykeyboardmarkup,replykeyboardremove
from DataBase import salva


myToken = '501102931:AAH8ZGgJ_C4u0RYLyvpDoEDDX-0uxo1ZyUs'  
data_base = salva()
data_base.prima()

def controllo_input(valore):
    try:
        int(valore)
        return True
    except ValueError:
        return False

def process_update(u, bot):
    user = u.message.from_user
    #c = controllo_input(u.message.text)

    if u.message.photo:     
        file_id = u.message.photo[2].file_id
        data_base.aggiungi_foto(file_id)

    if u.message.text:  
        if u.message.text[0] == "/":  
            if u.message.text == "/marconi": 
                bot.send_message(chat_id=user.id, text="Ciao")
            elif u.message.text == "/Keyboard":
                tastiera_comandi(bot,u.message.from_user)
            elif u.message.text == "/RemoveKeyboard":
                elimino_tastiera(bot,u.message.from_user)
            elif u.message.text == "/photo":
                t = data_base.prendi_foto()
                tt = bot.get_file(t)
                print(tt.file_path)
                bot.send_photo(chat_id=user.id,photo=tt.file_path)
                

    #elif u.message.text == "add":
        #data_base.aggiungi_testo(u.message.text)
    #elif u.message.text == "del":
        #data_base.delete_item(u.message.text)
    #elif u.message.text == "stampa":
        #dati = data_base.get_items()
        #bot.send_message(chat_id=user.id, text=dati)


def main(): 
    bot = telegram.Bot(myToken) 
    updates = bot.get_updates()
    new_update_id = None
    if updates:
       new_update_id = updates[-1].update_id + 1
    while True:
        try:
            new_updates = bot.get_updates(offset=new_update_id, timeout=10)       
            for u in new_updates:
                user = u.message.from_user
                process_update(u, bot)          
                new_update_id = u.update_id + 1
        except NetworkError:
            sleep(1) 


def tastiera_comandi(bot,u):
    user = u.message.from_user
    keyboard = [['Opz1'],['/photo'],['/RemoveKeyboard']]
    rm = telegram.ReplyKeyboardMarkup(keyboard, resize_keyboard=False, one_time_keyboard=False)
    bot.send_message(chat_id=user.id,text="Tastiera ",reply_markup=rm)

def elimino_tastiera(bot,u):
    user = u.message.from_user
    rm = telegram.ReplyKeyboardRemove()
    bot.send_message(chat_id=user.id, text="Rimuovo Tastiera", reply_markup=rm)


if __name__ == '__main__':
    main()