from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

STATE = None
HUMAN_YEAR = 1
HUMAN_HEIGHT = 2
HUMAN_WT =3
HUMAN_GEN = 4

def start(update, context):
    #firts_name = update.message.chat.firts_name
    #update.message.reply_text(f'Привет, {firts_name}')
    start_getting_human_info(update, context)

def start_getting_human_info(update, context):
    global STATE
    STATE = HUMAN_YEAR
    update.message.reply_text(f'Сколько вам лет?')

def received_human_year(update, context):
    global STATE
    year = int(update.message.text)
    context.user_data['human_year'] = year
    update.message.reply_text(f'Хорошо, теперь мне нужно знать ваш рост в см')
    STATE = HUMAN_HEIGHT

def received_human_height(update, context):
    global STATE 
    hg = int(update.message.text)
    context.user_data['human_hg'] = hg
    update.message.reply_text(f'Хорошо, теперь мне нужно знать ваш вес в кг')
    STATE = HUMAN_WT

def received_human_wt(update, context):
    global STATE 
    wt = int(update.message.text)
    context.user_data['human_wt'] = wt
    update.message.reply_text(f'Хорошо, теперь мне нужно знать ваш пол. 1 - женщина; 2 -мужчина: ')
    STATE = HUMAN_GEN

def received_human_gn(update, context):
    global STATE
    gn =int(update.message.text)
    context.user_data['human_gn'] = gn
    STATE =None
    update.message.reply_text(f'я получил все параметры')
    
    

def text(update, context):
    global STATE 

    if STATE == HUMAN_YEAR:
        return received_human_year(update, context)
    
    if STATE == HUMAN_HEIGHT:
        return received_human_height(update, context)

    if STATE == HUMAN_WT:
        return received_human_wt(update, context)
   
    if STATE == HUMAN_GEN:
        return received_human_gn(update, context)


def calculate_normakall(y, h, w, g):
    norma = {}
    if int(g) == 1:
        norma['kall']= int(655.1 + (9.563*w) + (1.85 * h) - (4.676 * y))
    else:
        norma['kall'] = int(65.5 + (13.75*w) + (5.03*h ) - (6.775 * y))
    return norma

def normakall(update, context):
    print('ok')
    user_normakall = calculate_normakall(context.user_data['human_year'],
        context.user_data['human_hg'], 
        context.user_data['human_wt'],
        context.user_data['human_gn'])
    nk = user_normakall['kall']
    update.message.reply_text(f'Ваша суточная норма калорий: {nk}')




def main():
    TOKEN = '5935128243:AAEOnk5PAmgGJF_2ONRn_oLzlu_oq5V07Kk'
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("norma", normakall))
    dispatcher.add_handler(MessageHandler(Filters.text, text))
    updater.start_polling()
    updater.idle()
 

if __name__ == '__main__':
    main()


