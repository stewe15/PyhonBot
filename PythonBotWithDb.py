import io
import telebot;
import asyncio
from telebot import types
from sqlalchemy import create_engine
import sqlalchemy as sq
from sqlalchemy.orm import Session
import sqlalchemy.orm
id = 0
controller = False
controllerMMTO = False
controllerChem = False
engine = create_engine('sqlite:///SortDB')
session = Session(bind=engine)
Base = sqlalchemy.orm.declarative_base()
class ModelSort(Base):
    __tablename__ = 'sorting'
    id = sq.Column(sq.Integer, primary_key=True)
    type = sq.Column(sq.String(256))
    subtype = sq.Column(sq.String(256))
    filename = sq.Column(sq.String(256))
    filetype = sq.Column(sq.String(256))
    data = sq.Column(sq.LargeBinary)

bot = telebot.TeleBot('7114499813:AAF7p88dwtfzIRCzYn6chUNyfoI_NjscL1I');
@bot.message_handler(content_types=['text'])

def get_text_messages(message):
    helloWord = '''
    Привет, этот бот содержит все файлы Сортировки.
    Взаимодействовать с ним достаточно просто
    Напиши /showDb и увидешь все доступные категории
    P.S. Бот на стадии разработки, возможны ошибки
    P.P.S. С химией получилась запара
    
    '''
    global controller
    global controllerMMTO
    if message.text == "/start":
        bot.send_message(message.from_user.id, helloWord)
        bot.send_message(message.from_user.id, "Чем я могу тебе помочь?")

    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши /showDb")
    elif message.text == "/showDb":
        keyboard = types.InlineKeyboardMarkup();  # наша клавиатура
        key_anlit = types.InlineKeyboardButton(text='Аналит', callback_data='analit');  # кнопка «Да»
        keyboard.add(key_anlit);  # добавляем кнопку в клавиатуру
        key_eng = types.InlineKeyboardButton(text='Ангиский', callback_data='eng');
        keyboard.add(key_eng);
        key_inja = types.InlineKeyboardButton(text='Инжа и начерт', callback_data='inja')
        keyboard.add(key_inja)
        key_intergers = types.InlineKeyboardButton(text='Интегралы', callback_data='intrges')
        keyboard.add(key_intergers)
        key_linal = types.InlineKeyboardButton(text='Линал',callback_data='linal')
        keyboard.add(key_linal)
        key_mmto = types.InlineKeyboardButton(text='ММТО', callback_data='mmto')
        keyboard.add(key_mmto)
        key_matanal = types.InlineKeyboardButton(text='МатАнал', callback_data='matanal')
        keyboard.add(key_matanal)
        key_metr = types.InlineKeyboardButton(text='Метрология', callback_data='metr')
        keyboard.add(key_metr)
        key_practice = types.InlineKeyboardButton(text='Практика', callback_data='practice')
        keyboard.add(key_practice)
        key_ref = types.InlineKeyboardButton(text='Рефераты', callback_data='ref')
        keyboard.add(key_ref)
        key_sxem = types.InlineKeyboardButton(text='Схемотехника', callback_data='sxem')
        keyboard.add(key_sxem)
        key_tkm = types.InlineKeyboardButton(text='ТКМ', callback_data='tkm')
        keyboard.add(key_tkm)
        key_theoryMech = types.InlineKeyboardButton(text='Теор.мех', callback_data='theoryMech')
        keyboard.add(key_theoryMech)
        key_terver = types.InlineKeyboardButton(text='Тервер', callback_data='terver')
        keyboard.add(key_terver)
        key_fome = types.InlineKeyboardButton(text='ФОМЭ', callback_data='fome')
        keyboard.add(key_fome)
        key_fxo = types.InlineKeyboardButton(text='ФХОМиНТ', callback_data='fxo')
        keyboard.add(key_fxo)
        key_phisic = types.InlineKeyboardButton(text='Физика', callback_data='phisic')
        keyboard.add(key_phisic)
        key_chem = types.InlineKeyboardButton(text='Химия', callback_data='chem')
        keyboard.add(key_chem)
        key_zacjsi = types.InlineKeyboardButton(text='ЗАГСИ', callback_data='zacjsi')
        keyboard.add(key_zacjsi)
        key_electromech = types.InlineKeyboardButton(text='Электротехника', callback_data='electro')
        keyboard.add(key_electromech)
        key_it = types.InlineKeyboardButton(text='Информатика и программирование', callback_data='it')
        keyboard.add(key_it)
        bot.send_message(message.from_user.id, text='Выберите категорию', reply_markup=keyboard)
    elif controller:
        try:
            id_send = int(message.text)
            obj = session.query(ModelSort.id, ModelSort.type, ModelSort.subtype, ModelSort.filename, ModelSort.filetype,
                                ModelSort.data).filter(ModelSort.id == id_send).all();
            for i in range(len(obj)):
                file_to_user = io.BytesIO(obj[i].data)
                file_to_user.name = obj[i].filename + obj[i].filetype
                bot.send_document(message.chat.id, file_to_user)
            controller = False
        except:
            bot.send_message(message.from_user.id, text = 'Попробуйте снова, ошибка id')
    elif controllerMMTO:
        try:
            id_send = int(message.text)
            obj = session.query(ModelSort.id, ModelSort.type, ModelSort.subtype, ModelSort.filename, ModelSort.filetype,
                                ModelSort.data).filter(ModelSort.id == id_send).all();
            for i in range(len(obj)):
                file_to_user = io.BytesIO(obj[i].data)
                file_to_user.name = str(i) + obj[i].filetype
                bot.send_document(message.chat.id, file_to_user)
            controller = False
        except:
            bot.send_message(message.from_user.id, text = 'Попробуйте снова, ошибка id')
    elif controllerChem:
        try:
            id_send = int(message.text)
            obj = session.query(ModelSort.id, ModelSort.type, ModelSort.subtype, ModelSort.filename, ModelSort.filetype,
                                ModelSort.data).filter(ModelSort.id == id_send).all();
            for i in range(len(obj)):
                file_to_user = io.BytesIO(obj[i].data)
                file_to_user.name = str(i) + obj[i].filetype
                bot.send_document(message.chat.id, file_to_user)
            controller = False
        except:
            bot.send_message(message.from_user.id, text = 'Попробуйте снова, ошибка id')
    elif message.text == "/Exel":
        bot.send_message(message.chat.id, "Информатика и программирование")
        objects = session.query(ModelSort.id, ModelSort.type, ModelSort.subtype, ModelSort.filename,
                                ModelSort.filetype).filter(ModelSort.subtype == 'Excel', ModelSort.type == 'информатика и программирование').all()
        bot.send_message(message.chat.id, "Файлы в директории")
        text = ""
        for i in range(len(objects)):
            text += str(
                str(objects[i].id) + "\t" + objects[i].type + "\t" + objects[i].subtype + "\t" + objects[i].filename +
                objects[i].filetype + '\n')
        mass = text.split('\n')
        txt = ""
        for i in range(0,20):
            txt+=mass[i] + '\n'
        txt2 = ""
        for i in range(20,len(mass)):
            txt2 += mass[i] + '\n'
        bot.send_message(message.chat.id, txt)
        bot.send_message(message.chat.id, txt2)
        bot.send_message(message.chat.id, "Введите id необходимого файла")
        controller = True
    elif message.text == "/Алгоритмизация и программирование Дерюгина":
        bot.send_message(message.chat.id, "Информатика и программирование")
        objects = session.query(ModelSort.id, ModelSort.type, ModelSort.subtype, ModelSort.filename,
                                ModelSort.filetype).filter(ModelSort.subtype == 'Алгоритмизация и программирование Дерюгина',
                                                           ModelSort.type == 'информатика и программирование').all()
        bot.send_message(message.chat.id, "Файлы в директории")
        text = ""
        for i in range(len(objects)):
            text += str(
                str(objects[i].id) + "\t" + objects[i].type + "\t" + objects[i].subtype + "\t" + objects[i].filename +
                objects[i].filetype + '\n')
        bot.send_message(message.chat.id, text)
        bot.send_message(message.chat.id, "Введите id необходимого файла")
        controller = True
    elif message.text == "/Алгоритмизация и Программирование Козеева":
        bot.send_message(message.chat.id, "Информатика и программирование")
        objects = session.query(ModelSort.id, ModelSort.type, ModelSort.subtype, ModelSort.filename,
                                ModelSort.filetype).filter(ModelSort.subtype == 'Алгоритмизация и Программирование Козеева',
                                                           ModelSort.type == 'информатика и программирование').all()
        bot.send_message(message.chat.id, "Файлы в директории")
        text = ""
        for i in range(len(objects)):
            text += str(
                str(objects[i].id) + "\t" + objects[i].type + "\t" + objects[i].subtype + "\t" + objects[i].filename +
                objects[i].filetype + '\n')
        bot.send_message(message.chat.id, text)
        bot.send_message(message.chat.id, "Введите id необходимого файла")
        controller = True
    elif message.text == "/Высокоуровневое программирование":
        bot.send_message(message.chat.id, "Информатика и программирование")
        objects = session.query(ModelSort.id, ModelSort.type, ModelSort.subtype, ModelSort.filename,
                                ModelSort.filetype).filter(ModelSort.subtype == 'Высокоуровневое программирование',
                                                           ModelSort.type == 'информатика и программирование').all()
        bot.send_message(message.chat.id, "Файлы в директории")
        text = ""
        for i in range(len(objects)):
            text += str(
                str(objects[i].id) + "\t" + objects[i].type + "\t" + objects[i].subtype + "\t" + objects[i].filename +
                objects[i].filetype + '\n')
        bot.send_message(message.chat.id, text)
        bot.send_message(message.chat.id, "Введите id необходимого файла")
        controller = True
    elif message.text == "/Информатика Акименко":
        bot.send_message(message.chat.id, "Информатика и программирование")
        objects = session.query(ModelSort.id, ModelSort.type, ModelSort.subtype, ModelSort.filename,
                                ModelSort.filetype).filter(ModelSort.subtype == 'Информатика Акименко',
                                                           ModelSort.type == 'информатика и программирование').all()
        bot.send_message(message.chat.id, "Файлы в директории")
        text = ""
        for i in range(len(objects)):
            text += str(
                str(objects[i].id) + "\t" + objects[i].type + "\t" + objects[i].subtype + "\t" + objects[i].filename +
                objects[i].filetype + '\n')
        bot.send_message(message.chat.id, text)
        bot.send_message(message.chat.id, "Введите id необходимого файла")
        controller = True
    elif message.text == "/Информатика Антипова":
        bot.send_message(message.chat.id, "Информатика и программирование")
        objects = session.query(ModelSort.id, ModelSort.type, ModelSort.subtype, ModelSort.filename,
                                ModelSort.filetype).filter(ModelSort.subtype == 'Информатика Антипова',
                                                           ModelSort.type == 'информатика и программирование').all()
        bot.send_message(message.chat.id, "Файлы в директории")
        text = ""
        for i in range(len(objects)):
            text += str(
                str(objects[i].id) + "\t" + objects[i].type + "\t" + objects[i].subtype + "\t" + objects[i].filename +
                objects[i].filetype + '\n')
        bot.send_message(message.chat.id, text)
        bot.send_message(message.chat.id, "Введите id необходимого файла")
        controller = True
    elif message.text == "/Информатика Глебов":
        bot.send_message(message.chat.id, "Информатика и программирование")
        objects = session.query(ModelSort.id, ModelSort.type, ModelSort.subtype, ModelSort.filename,
                                ModelSort.filetype).filter(ModelSort.subtype == 'Информатика Глебов',
                                                           ModelSort.type == 'информатика и программирование').all()
        bot.send_message(message.chat.id, "Файлы в директории")
        text = ""
        for i in range(len(objects)):
            text += str(
                str(objects[i].id) + "\t" + objects[i].type + "\t" + objects[i].subtype + "\t" + objects[i].filename +
                objects[i].filetype + '\n')
        bot.send_message(message.chat.id, text)
        bot.send_message(message.chat.id, "Введите id необходимого файла")
        controller = True
    elif message.text == "/Информатика Козеева":
        bot.send_message(message.chat.id, "Информатика и программирование")
        objects = session.query(ModelSort.id, ModelSort.type, ModelSort.subtype, ModelSort.filename,
                                ModelSort.filetype).filter(ModelSort.subtype == 'Информатика Козеева',
                                                           ModelSort.type == 'информатика и программирование').all()
        bot.send_message(message.chat.id, "Файлы в директории")
        text = ""
        for i in range(len(objects)):
            text += str(
                str(objects[i].id) + "\t" + objects[i].type + "\t" + objects[i].subtype + "\t" + objects[i].filename +
                objects[i].filetype + '\n')
        bot.send_message(message.chat.id, text)
        bot.send_message(message.chat.id, "Введите id необходимого файла")
        controller = True
    elif message.text == "/Информатика Крысин":
        bot.send_message(message.chat.id, "Информатика и программирование")
        objects = session.query(ModelSort.id, ModelSort.type, ModelSort.subtype, ModelSort.filename,
                                ModelSort.filetype).filter(ModelSort.subtype == 'Информатика Крысин',
                                                           ModelSort.type == 'информатика и программирование').all()
        bot.send_message(message.chat.id, "Файлы в директории")
        text = ""
        for i in range(len(objects)):
            text += str(
                str(objects[i].id) + "\t" + objects[i].type + "\t" + objects[i].subtype + "\t" + objects[i].filename +
                objects[i].filetype + '\n')
        bot.send_message(message.chat.id, text)
        bot.send_message(message.chat.id, "Введите id необходимого файла")
        controller = True
    elif message.text == "/Информатика Лавренков":
        bot.send_message(message.chat.id, "Информатика и программирование")
        objects = session.query(ModelSort.id, ModelSort.type, ModelSort.subtype, ModelSort.filename,
                                ModelSort.filetype).filter(ModelSort.subtype == 'Информатика Лавренков',
                                                           ModelSort.type == 'информатика и программирование').all()
        bot.send_message(message.chat.id, "Файлы в директории")
        text = ""
        for i in range(len(objects)):
            text += str(
                str(objects[i].id) + "\t" + objects[i].type + "\t" + objects[i].subtype + "\t" + objects[i].filename +
                objects[i].filetype + '\n')
        bot.send_message(message.chat.id, text)
        bot.send_message(message.chat.id, "Введите id необходимого файла")
        controller = True
    elif message.text == "/Информатика Матлаб":
        bot.send_message(message.chat.id, "Информатика и программирование")
        objects = session.query(ModelSort.id, ModelSort.type, ModelSort.subtype, ModelSort.filename,
                                ModelSort.filetype).filter(ModelSort.subtype == 'Информатика Матлаб',
                                                           ModelSort.type == 'информатика и программирование').all()
        bot.send_message(message.chat.id, "Файлы в директории")
        text = ""
        for i in range(len(objects)):
            text += str(
                str(objects[i].id) + "\t" + objects[i].type + "\t" + objects[i].subtype + "\t" + objects[i].filename +
                objects[i].filetype + '\n')
        bot.send_message(message.chat.id, text)
        bot.send_message(message.chat.id, "Введите id необходимого файла")
        controller = True
    elif message.text == "/Математические основы информатики":
        bot.send_message(message.chat.id, "Информатика и программирование")
        objects = session.query(ModelSort.id, ModelSort.type, ModelSort.subtype, ModelSort.filename,
                                ModelSort.filetype).filter(ModelSort.subtype == 'Математические основы информатики',
                                                           ModelSort.type == 'информатика и программирование').all()
        bot.send_message(message.chat.id, "Файлы в директории")
        text = ""
        for i in range(len(objects)):
            text += str(
                str(objects[i].id) + "\t" + objects[i].type + "\t" + objects[i].subtype + "\t" + objects[i].filename +
                objects[i].filetype + '\n')
        bot.send_message(message.chat.id, text)
        bot.send_message(message.chat.id, "Введите id необходимого файла")
        controller = True
    elif message.text == "/Не понятно куда деть":
        bot.send_message(message.chat.id, "Информатика и программирование")
        objects = session.query(ModelSort.id, ModelSort.type, ModelSort.subtype, ModelSort.filename,
                                ModelSort.filetype).filter(ModelSort.subtype == 'Не понятно куда деть',
                                                           ModelSort.type == 'информатика и программирование').all()
        bot.send_message(message.chat.id, "Файлы в директории")
        text = ""
        for i in range(len(objects)):
            text += str(
                str(objects[i].id) + "\t" + objects[i].type + "\t" + objects[i].subtype + "\t" + objects[i].filename +
                objects[i].filetype + '\n')
        bot.send_message(message.chat.id, text)
        bot.send_message(message.chat.id, "Введите id необходимого файла")
        controller = True
    elif message.text == "/ООП":
        bot.send_message(message.chat.id, "Информатика и программирование")
        objects = session.query(ModelSort.id, ModelSort.type, ModelSort.subtype, ModelSort.filename,
                                ModelSort.filetype).filter(ModelSort.subtype == 'ООП',
                                                           ModelSort.type == 'информатика и программирование').all()
        bot.send_message(message.chat.id, "Файлы в директории")
        text = ""
        for i in range(len(objects)):
            text += str(
                str(objects[i].id) + "\t" + objects[i].type + "\t" + objects[i].subtype + "\t" + objects[i].filename +
                objects[i].filetype + '\n')
        bot.send_message(message.chat.id, text)
        bot.send_message(message.chat.id, "Введите id необходимого файла")
        controller = True
    elif message.text == "/Основы программирования Антипова":
        bot.send_message(message.chat.id, "Информатика и программирование")
        objects = session.query(ModelSort.id, ModelSort.type, ModelSort.subtype, ModelSort.filename,
                                ModelSort.filetype).filter(ModelSort.subtype == 'Основы программирования Антипова',
                                                           ModelSort.type == 'информатика и программирование').all()
        bot.send_message(message.chat.id, "Файлы в директории")
        text = ""
        for i in range(len(objects)):
            text += str(
                str(objects[i].id) + "\t" + objects[i].type + "\t" + objects[i].subtype + "\t" + objects[i].filename +
                objects[i].filetype + '\n')
        bot.send_message(message.chat.id, text)
        bot.send_message(message.chat.id, "Введите id необходимого файла")
        controller = True
    elif message.text == "/Основы программной инженерии":
        bot.send_message(message.chat.id, "Информатика и программирование")
        objects = session.query(ModelSort.id, ModelSort.type, ModelSort.subtype, ModelSort.filename,
                                ModelSort.filetype).filter(ModelSort.subtype == 'Основы программной инженерии',
                                                           ModelSort.type == 'информатика и программирование').all()
        bot.send_message(message.chat.id, "Файлы в директории")
        text = ""
        for i in range(len(objects)):
            text += str(
                str(objects[i].id) + "\t" + objects[i].type + "\t" + objects[i].subtype + "\t" + objects[i].filename +
                objects[i].filetype + '\n')
        bot.send_message(message.chat.id, text)
        bot.send_message(message.chat.id, "Введите id необходимого файла")
        controller = True
    elif message.text == "/Программирование на основе классов и шаблонов":
        bot.send_message(message.chat.id, "Информатика и программирование")
        objects = session.query(ModelSort.id, ModelSort.type, ModelSort.subtype, ModelSort.filename,
                                ModelSort.filetype).filter(ModelSort.subtype == 'Программирование на основе классов и шаблонов',
                                                           ModelSort.type == 'информатика и программирование').all()
        bot.send_message(message.chat.id, "Файлы в директории")
        text = ""
        for i in range(len(objects)):
            text += str(
                str(objects[i].id) + "\t" + objects[i].type + "\t" + objects[i].subtype + "\t" + objects[i].filename +
                objects[i].filetype + '\n')
        bot.send_message(message.chat.id, text)
        bot.send_message(message.chat.id, "Введите id необходимого файла")
        controller = True
    elif message.text == "/Теоретическая информатика":
        bot.send_message(message.chat.id, "Информатика и программирование")
        objects = session.query(ModelSort.id, ModelSort.type, ModelSort.subtype, ModelSort.filename,
                                ModelSort.filetype).filter(ModelSort.subtype == 'Теоретическая информатика',
                                                           ModelSort.type == 'информатика и программирование').all()
        bot.send_message(message.chat.id, "Файлы в директории")
        text = ""
        for i in range(len(objects)):
            text += str(
                str(objects[i].id) + "\t" + objects[i].type + "\t" + objects[i].subtype + "\t" + objects[i].filename +
                objects[i].filetype + '\n')
        bot.send_message(message.chat.id, text)
        bot.send_message(message.chat.id, "Введите id необходимого файла")
        controller = True
    elif message.text == "/Технологии и методы программирования":
        bot.send_message(message.chat.id, "Информатика и программирование")
        objects = session.query(ModelSort.id, ModelSort.type, ModelSort.subtype, ModelSort.filename,
                                ModelSort.filetype).filter(ModelSort.subtype == 'Технологии и методы программирования',
                                                           ModelSort.type == 'информатика и программирование').all()
        bot.send_message(message.chat.id, "Файлы в директории")
        text = ""
        for i in range(len(objects)):
            text += str(
                str(objects[i].id) + "\t" + objects[i].type + "\t" + objects[i].subtype + "\t" + objects[i].filename +
                objects[i].filetype + '\n')
        bot.send_message(message.chat.id, text)
        bot.send_message(message.chat.id, "Введите id необходимого файла")
        controller = True
    elif message.text == "/Язык программирования Си":
        bot.send_message(message.chat.id, "Информатика и программирование")
        objects = session.query(ModelSort.id, ModelSort.type, ModelSort.subtype, ModelSort.filename,
                                ModelSort.filetype).filter(ModelSort.subtype == 'Язык программирования Си',
                                                           ModelSort.type == 'информатика и программирование').all()
        bot.send_message(message.chat.id, "Файлы в директории")
        text = ""
        for i in range(len(objects)):
            text += str(
                str(objects[i].id) + "\t" + objects[i].type + "\t" + objects[i].subtype + "\t" + objects[i].filename +
                objects[i].filetype + '\n')
        bot.send_message(message.chat.id, text)
        bot.send_message(message.chat.id, "Введите id необходимого файла")
        controller = True
    elif message.text == "/Физика ЛР":
        bot.send_message(message.chat.id, "Физика ЛР")
        objects = session.query(ModelSort.id, ModelSort.type, ModelSort.subtype, ModelSort.filename,
                                ModelSort.filetype).filter(ModelSort.subtype == 'Физика ЛР',
                                                           ModelSort.type == 'Физика').all()
        bot.send_message(message.chat.id, "Файлы в директории")
        text = ""
        for i in range(len(objects)):
            text += str(
                str(objects[i].id) + "\t" + objects[i].type + "\t" + objects[i].subtype + "\t" + objects[i].filename +
                objects[i].filetype + '\n')
        mass = text.split('\n')
        txt1 = ""
        txt2 = ""
        txt3 = ""
        txt4 = ""
        txt5 = ""
        for i in range(0,50):
            txt1 += mass[i] + '\n'
        for i in range(50,100):
            txt2 += mass[i] + '\n'
        for i in range(100, 150):
            txt3 += mass[i] + '\n'
        for i in range(150,200):
            txt4 += mass[i] + '\n'
        for i in range(200, len(mass)):
            txt5 += mass[i] + '\n'
        bot.send_message(message.chat.id, txt1)
        bot.send_message(message.chat.id, txt2)
        bot.send_message(message.chat.id, txt3)
        bot.send_message(message.chat.id, txt4)
        bot.send_message(message.chat.id, txt5)
        bot.send_message(message.chat.id, "Введите id необходимого файла")
        controller = True
    elif message.text == "/Физика ДЗ":
        bot.send_message(message.chat.id, "Физика ДЗ")
        objects = session.query(ModelSort.id, ModelSort.type, ModelSort.subtype, ModelSort.filename,
                                ModelSort.filetype).filter(ModelSort.subtype == 'Физика ДЗ',
                                                           ModelSort.type == 'Физика').all()
        bot.send_message(message.chat.id, "Файлы в директории")
        text = ""
        for i in range(len(objects)):
            text += str(
                str(objects[i].id) + "\t" + objects[i].type + "\t" + objects[i].subtype + "\t" + objects[i].filename +
                objects[i].filetype + '\n')
        mass = text.split('\n')
        txt1 = ""
        for i in range(0,50):
            txt1 += mass[i] + '\n'
        txt2 = ""
        for i in range(50,100):
            txt2 += mass[i] + '\n'
        txt3 = ""
        for i in range(100, len(mass)):
            txt3 += mass[i] + '\n'



        bot.send_message(message.chat.id, txt1)
        bot.send_message(message.chat.id, txt2)
        bot.send_message(message.chat.id, txt3)
        bot.send_message(message.chat.id, "Введите id необходимого файла")
        controller = True
    else:
        bot.send_message(message.chat.id, "Я тебя не понимаю, напиши /start")



textIT = '''
    Выюерите категорию:
/Exel
/Алгоритмизация и программирование Дерюгина
/Алгоритмизация и Программирование Козеева
/Высокоуровневое программирование
/Информатика Акименко
/Информатика Антипова
/Информатика Глебов
/Информатика Козеева
/Информатика Крысин
/Информатика Лавренков
/Информатика Матлаб
/Математические основы информатики
/Не понятно куда деть
/ООП
/Основы программирования Антипова
/Основы программной инженерии
/Программирование на основе классов и шаблонов
/Теоретическая информатика
/Технологии и методы программирования
/Язык программирования Си
    
'''
textPhys ='''
/Физика ЛР
/Физика ДЗ
'''



@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    global controller
    global controllerMMTO
    global controllerChem
    if call.data == 'analit':
        bot.send_message(call.message.chat.id, "Аналит")
        objects = session.query(ModelSort.id,ModelSort.type,ModelSort.subtype,ModelSort.filename,ModelSort.filetype).filter(ModelSort.subtype == 'Нет', ModelSort.type == 'Аналит').all()
        bot.send_message(call.message.chat.id,"Файлы в директории")
        text = ""
        for i in range(len(objects)):
            text += str(str(objects[i].id)+ "\t" +objects[i].type+ "\t"+objects[i].subtype + "\t" + objects[i].filename + objects[i].filetype +'\n')
        bot.send_message(call.message.chat.id, text)
        bot.send_message(call.message.chat.id, "Введите id необходимого файла")
        controller = True




    elif call.data == 'eng':
        bot.send_message(call.message.chat.id, "Английский")
        objects = session.query(ModelSort.id, ModelSort.type, ModelSort.subtype, ModelSort.filename,
                                ModelSort.filetype).filter(ModelSort.subtype == 'Нет', ModelSort.type == 'Английский').all()
        bot.send_message(call.message.chat.id, "Файлы в директории")
        text = ""
        for i in range(len(objects)):
            text += str(
                str(objects[i].id) + "\t" + objects[i].type + "\t" + objects[i].subtype + "\t" + objects[i].filename +
                objects[i].filetype + '\n')
        bot.send_message(call.message.chat.id, text)
        bot.send_message(call.message.chat.id, "Введите id необходимого файла")
        controller = True
    elif call.data == 'inja':
        bot.send_message(call.message.chat.id, "Инжа и начерт")
        objects = session.query(ModelSort.id, ModelSort.type, ModelSort.subtype, ModelSort.filename,
                                ModelSort.filetype).filter(ModelSort.subtype == 'Нет', ModelSort.type == 'Инжа и начерт').all()
        bot.send_message(call.message.chat.id, "Файлы в директории")
        text = ""
        for i in range(len(objects)):
            text += str(
                str(objects[i].id) + "\t" + objects[i].type + "\t" + objects[i].subtype + "\t" + objects[i].filename +
                objects[i].filetype + '\n')
        mass = text.split('\n')
        txt = ""
        for i in range(50):
            txt+=mass[i] + '\n'
        txt2 = ""
        for i in range(50,100):
            txt2+=mass[i]+'\n'
        txt3 = ""
        for i in range(100, 150):
            txt3 += mass[i] + '\n'
        txt4 = ""
        for i in range(150, 200):
            txt4 += mass[i] + '\n'
        txt5 = ""
        for i in range(200, 250):
            txt5 += mass[i] + '\n'
        txt6 = ""
        for i in range(250, 300):
            txt6 += mass[i] + '\n'
        txt7 = ""
        for i in range(250, 300):
            txt7 += mass[i] + '\n'
        txt8 = ""
        for i in range(300, 350):
            txt8 += mass[i] + '\n'
        txt9 = ""
        for i in range(350, 400):
            txt9 += mass[i] + '\n'
        txt10 = ""
        for i in range(400, len(mass)):
            txt10 += mass[i] + '\n'
        bot.send_message(call.message.chat.id, txt)
        bot.send_message(call.message.chat.id, txt2)
        bot.send_message(call.message.chat.id, txt3)
        bot.send_message(call.message.chat.id, txt4)
        bot.send_message(call.message.chat.id, txt5)
        bot.send_message(call.message.chat.id, txt6)
        bot.send_message(call.message.chat.id, txt7)
        bot.send_message(call.message.chat.id, txt8)
        bot.send_message(call.message.chat.id, txt9)
        bot.send_message(call.message.chat.id, txt10)
        bot.send_message(call.message.chat.id, "Введите id необходимого файла")
        controller = True
    elif call.data == 'intrges':
        bot.send_message(call.message.chat.id, "Интегралы")
        objects = session.query(ModelSort.id, ModelSort.type, ModelSort.subtype, ModelSort.filename,
                                ModelSort.filetype).filter(ModelSort.subtype == 'Нет',
                                                           ModelSort.type == 'Интегралы').all()
        bot.send_message(call.message.chat.id, "Файлы в директории")
        text = ""
        for i in range(len(objects)):
            text += str(
                str(objects[i].id) + "\t" + objects[i].type + "\t" + objects[i].subtype + "\t" + objects[i].filename +
                objects[i].filetype + '\n')
        bot.send_message(call.message.chat.id, text)
        bot.send_message(call.message.chat.id, "Введите id необходимого файла")
        controller = True
    elif call.data == 'linal':
        bot.send_message(call.message.chat.id, "Линал")
        objects = session.query(ModelSort.id, ModelSort.type, ModelSort.subtype, ModelSort.filename,
                                ModelSort.filetype).filter(ModelSort.subtype == 'Нет',
                                                           ModelSort.type == 'Линал').all()
        bot.send_message(call.message.chat.id, "Файлы в директории")
        text = ""
        for i in range(len(objects)):
            text += str(
                str(objects[i].id) + "\t" + objects[i].type + "\t" + objects[i].subtype + "\t" + objects[i].filename +
                objects[i].filetype + '\n')
        bot.send_message(call.message.chat.id, text)
        bot.send_message(call.message.chat.id, "Введите id необходимого файла")
        controller = True
    elif call.data == 'mmto':
        bot.send_message(call.message.chat.id, "ММТО")
        objects = session.query(ModelSort.id, ModelSort.type, ModelSort.subtype, ModelSort.filename,
                                ModelSort.filetype).filter(ModelSort.subtype == 'Нет',
                                                           ModelSort.type == 'ММТО').all()
        bot.send_message(call.message.chat.id, "Файлы в директории")
        text = ""
        for i in range(len(objects)):
            text += str(
                str(objects[i].id) + "\t" + str(objects[i].type) + "\t" + str(objects[i].subtype) + "\t" + str(i) +
                ".ewb" + '\n')
        bot.send_message(call.message.chat.id, text)
        bot.send_message(call.message.chat.id, "Введите id необходимого файла")
        controllerMMTO = True
    elif call.data == 'matanal':
        bot.send_message(call.message.chat.id, "МатАнал")
        objects = session.query(ModelSort.id, ModelSort.type, ModelSort.subtype, ModelSort.filename,
                                ModelSort.filetype).filter(ModelSort.subtype == 'Нет',
                                                           ModelSort.type == 'МатАнал').all()
        bot.send_message(call.message.chat.id, "Файлы в директории")
        text = ""
        for i in range(len(objects)):
            text += str(
                str(objects[i].id) + "\t" + objects[i].type + "\t" + objects[i].subtype + "\t" + objects[i].filename +
                objects[i].filetype + '\n')
        bot.send_message(call.message.chat.id, text)
        bot.send_message(call.message.chat.id, "Введите id необходимого файла")
        controller = True
    elif call.data == 'metr':
        bot.send_message(call.message.chat.id, "Метрология и технические измерения в производстве ЭС")
        objects = session.query(ModelSort.id, ModelSort.type, ModelSort.subtype, ModelSort.filename,
                                ModelSort.filetype).filter(ModelSort.subtype == 'Нет',
                                                           ModelSort.type == 'Метрология и технические измерения в производстве ЭС').all()
        bot.send_message(call.message.chat.id, "Файлы в директории")
        text = ""
        for i in range(len(objects)):
            text += str(
                str(objects[i].id) + "\t" + objects[i].type + "\t" + objects[i].subtype + "\t" + objects[i].filename +
                objects[i].filetype + '\n')
        bot.send_message(call.message.chat.id, text)
        bot.send_message(call.message.chat.id, "Введите id необходимого файла")
        controller = True
    elif call.data == 'practice':
        bot.send_message(call.message.chat.id, "Практика")
        objects = session.query(ModelSort.id, ModelSort.type, ModelSort.subtype, ModelSort.filename,
                                ModelSort.filetype).filter(ModelSort.subtype == 'Нет',
                                                           ModelSort.type == 'Практика').all()
        bot.send_message(call.message.chat.id, "Файлы в директории")
        text = ""
        for i in range(len(objects)):
            text += str(
                str(objects[i].id) + "\t" + objects[i].type + "\t" + objects[i].subtype + "\t" + objects[i].filename +
                objects[i].filetype + '\n')
        mass = text.split('\n')
        txt1 = ""
        for i in range(0,50):
            txt1+=mass[i]+ '\n'
        bot.send_message(call.message.chat.id, txt1)
        txt2 = ""
        for i in range(50,104):
            txt2+=mass[i]+'\n'
        bot.send_message(call.message.chat.id, txt2)
        bot.send_message(call.message.chat.id, "Введите id необходимого файла")
        controller = True
    elif call.data == 'ref':
        bot.send_message(call.message.chat.id, "Рефераты")
        objects = session.query(ModelSort.id, ModelSort.type, ModelSort.subtype, ModelSort.filename,
                                ModelSort.filetype).filter(ModelSort.subtype == 'Нет',
                                                           ModelSort.type == 'Рефераты').all()
        bot.send_message(call.message.chat.id, "Файлы в директории")
        text = ""
        for i in range(len(objects)):
            text += str(
                str(objects[i].id) + "\t" + objects[i].type + "\t" + objects[i].subtype + "\t" + objects[i].filename +
                objects[i].filetype + '\n')
        mass = text.split('\n')
        txt1 = ""
        for i in range(0,50):
            txt1+=mass[i]+'\n'
        txt2 = ""
        for i in range(50,len(mass)):
            txt2+=mass[i]+'\n'
        bot.send_message(call.message.chat.id, txt1)
        bot.send_message(call.message.chat.id, txt2)
        bot.send_message(call.message.chat.id, "Введите id необходимого файла")
        controller = True
    elif call.data == 'sxem':
        bot.send_message(call.message.chat.id, "Схемотехника")
        objects = session.query(ModelSort.id, ModelSort.type, ModelSort.subtype, ModelSort.filename,
                                ModelSort.filetype).filter(ModelSort.subtype == 'Нет',
                                                           ModelSort.type == 'Схемотехника').all()
        bot.send_message(call.message.chat.id, "Файлы в директории")
        text = ""
        for i in range(len(objects)):
            text += str(
                str(objects[i].id) + "\t" + objects[i].type + "\t" + objects[i].subtype + "\t" + objects[i].filename +
                objects[i].filetype + '\n')
        bot.send_message(call.message.chat.id, text)
        bot.send_message(call.message.chat.id, "Введите id необходимого файла")
        controller = True
    elif call.data == 'tkm':
        bot.send_message(call.message.chat.id, "ТКМ")
        objects = session.query(ModelSort.id, ModelSort.type, ModelSort.subtype, ModelSort.filename,
                                ModelSort.filetype).filter(ModelSort.subtype == 'Нет',
                                                           ModelSort.type == 'ТКМ').all()
        bot.send_message(call.message.chat.id, "Файлы в директории")
        text = ""
        for i in range(len(objects)):
            text += str(
                str(objects[i].id) + "\t" + objects[i].type + "\t" + objects[i].subtype + "\t" + objects[i].filename +
                objects[i].filetype + '\n')
        bot.send_message(call.message.chat.id, text)
        bot.send_message(call.message.chat.id, "Введите id необходимого файла")
        controller = True
    elif call.data == 'theoryMech':
        bot.send_message(call.message.chat.id, "Теор.Мех-")
        objects = session.query(ModelSort.id, ModelSort.type, ModelSort.subtype, ModelSort.filename,
                                ModelSort.filetype).filter(ModelSort.subtype == 'Нет',
                                                           ModelSort.type == 'Теор.Мех-').all()
        bot.send_message(call.message.chat.id, "Файлы в директории")
        text = ""
        for i in range(len(objects)):
            text += str(
                str(objects[i].id) + "\t" + objects[i].type + "\t" + objects[i].subtype + "\t" + objects[i].filename +
                objects[i].filetype + '\n')
        bot.send_message(call.message.chat.id, text)
        bot.send_message(call.message.chat.id, "Введите id необходимого файла")
        controller = True
    elif call.data == 'terver':
        bot.send_message(call.message.chat.id, "Тервер")
        objects = session.query(ModelSort.id, ModelSort.type, ModelSort.subtype, ModelSort.filename,
                                ModelSort.filetype).filter(ModelSort.subtype == 'Нет',
                                                           ModelSort.type == 'Тервер').all()
        bot.send_message(call.message.chat.id, "Файлы в директории")
        text = ""
        for i in range(len(objects)):
            text += str(
                str(objects[i].id) + "\t" + objects[i].type + "\t" + objects[i].subtype + "\t" + objects[i].filename +
                objects[i].filetype + '\n')
        bot.send_message(call.message.chat.id, text)
        bot.send_message(call.message.chat.id, "Введите id необходимого файла")
        controller = True
    elif call.data == 'fome':
        bot.send_message(call.message.chat.id, "ФОМЭ")
        objects = session.query(ModelSort.id, ModelSort.type, ModelSort.subtype, ModelSort.filename,
                                ModelSort.filetype).filter(ModelSort.subtype == 'Нет',
                                                           ModelSort.type == 'ФОМЭ').all()
        bot.send_message(call.message.chat.id, "Файлы в директории")
        text = ""
        for i in range(len(objects)):
            text += str(
                str(objects[i].id) + "\t" + objects[i].type + "\t" + objects[i].subtype + "\t" + objects[i].filename +
                objects[i].filetype + '\n')
        bot.send_message(call.message.chat.id, text)
        bot.send_message(call.message.chat.id, "Введите id необходимого файла")
        controller = True
    elif call.data == 'fxo':
        bot.send_message(call.message.chat.id, "ФХОМиНТ")
        objects = session.query(ModelSort.id, ModelSort.type, ModelSort.subtype, ModelSort.filename,
                                ModelSort.filetype).filter(ModelSort.subtype == 'Нет',
                                                           ModelSort.type == 'ФХОМиНТ').all()
        bot.send_message(call.message.chat.id, "Файлы в директории")
        text = ""
        for i in range(len(objects)):
            text += str(
                str(objects[i].id) + "\t" + objects[i].type + "\t" + objects[i].subtype + "\t" + objects[i].filename +
                objects[i].filetype + '\n')
        bot.send_message(call.message.chat.id, text)
        bot.send_message(call.message.chat.id, "Введите id необходимого файла")
        controller = True
    elif call.data == 'phisic':
        bot.send_message(call.message.chat.id, textPhys)
    elif call.data == 'chem':
        bot.send_message(call.message.chat.id, "Химия")
        objects = session.query(ModelSort.id, ModelSort.type, ModelSort.subtype, ModelSort.filename,
                                ModelSort.filetype).filter(ModelSort.subtype == 'Нет',
                                                           ModelSort.type == 'Химия').all()
        bot.send_message(call.message.chat.id, "Файлы в директории")
        text = ""
        for i in range(len(objects)):
            text += str(
                str(objects[i].id) + "\t" + objects[i].type + "\t" + objects[i].subtype + "\t" + str(i) +
                objects[i].filetype + '\n')
        mass = text.split('\n')
        txt1 = ""
        txt2 = ""
        txt3=""
        for i in range(0,50):
            txt1 += mass[i]+'\n'
        for i in range(50,100):
            txt2 += mass[i]+'\n'
        for i in range(100,len(mass)):
            txt3+=mass[i]+'\n'
        bot.send_message(call.message.chat.id, txt1)
        bot.send_message(call.message.chat.id, txt2)
        bot.send_message(call.message.chat.id, txt3)

        bot.send_message(call.message.chat.id, "Введите id необходимого файла")
        controllerChem = True
    elif call.data == 'zacjsi':
        bot.send_message(call.message.chat.id, "ЭАСЗИ")
        objects = session.query(ModelSort.id, ModelSort.type, ModelSort.subtype, ModelSort.filename,
                                ModelSort.filetype).filter(ModelSort.subtype == 'Нет',
                                                           ModelSort.type == 'ЭАСЗИ').all()
        bot.send_message(call.message.chat.id, "Файлы в директории")
        text = ""
        for i in range(len(objects)):
            text += str(
                str(objects[i].id) + "\t" + objects[i].type + "\t" + objects[i].subtype + "\t" + objects[i].filename +
                objects[i].filetype + '\n')
        bot.send_message(call.message.chat.id, text)
        bot.send_message(call.message.chat.id, "Введите id необходимого файла")
        controller = True
    elif call.data == 'electro':
        bot.send_message(call.message.chat.id, "Электротехника")
        objects = session.query(ModelSort.id, ModelSort.type, ModelSort.subtype, ModelSort.filename,
                                ModelSort.filetype).filter(ModelSort.subtype == 'Нет',
                                                           ModelSort.type == 'Электротехника').all()
        bot.send_message(call.message.chat.id, "Файлы в директории")
        text = ""
        for i in range(len(objects)):
            text += str(
                str(objects[i].id) + "\t" + objects[i].type + "\t" + objects[i].subtype + "\t" + objects[i].filename +
                objects[i].filetype + '\n')
        bot.send_message(call.message.chat.id, text)
        bot.send_message(call.message.chat.id, "Введите id необходимого файла")
        controller = True
    elif call.data == 'it':
        bot.send_message(call.message.chat.id, textIT)




bot.polling(none_stop=True, interval=0)
