import sqlalchemy as sq
import sqlalchemy.orm
import os
path_s = "C:/Users/22833/Desktop/Сортировка/Сортировка"
filelist = os.listdir(path_s)
paths = []
for i in range(len(filelist)):
    paths.append(path_s + f'/{filelist[i]}')
docks = []
for j in range(len(paths)):
    file_and_folders = os.listdir(paths[j])
    for t in range(len(file_and_folders)):
        docks.append(paths[j] + '/'+file_and_folders[t])

path_it = 'C:/Users/22833/Desktop/Сортировка/информатика и программирование'
filelistIt = os.listdir(path_it)
paths_It = []
for i in range(len(filelistIt)):
    paths_It.append(path_it + f'/{filelistIt[i]}')

docks_for_it = []
for j in range(len(paths_It)):
    file_and_folders = os.listdir(paths_It[j])
    for t in range(len(file_and_folders)):
        docks_for_it.append(paths_It[j] + '/'+file_and_folders[t])
#print(len(docks_for_it) + len(docks))
def physics():
    path_it = 'C:/Users/22833/Desktop/Сортировка/Физика'
    filelistIt = os.listdir(path_it)
    paths_It = []
    for i in range(len(filelistIt)):
        paths_It.append(path_it + f'/{filelistIt[i]}')

    docks_for_it = []
    for j in range(len(paths_It)):
        file_and_folders = os.listdir(paths_It[j])
        for t in range(len(file_and_folders)):
            docks_for_it.append(paths_It[j] + '/' + file_and_folders[t])
    return docks_for_it
def get_type(path):
    base, ext = os.path.splitext(path)
    return ext
def get_filename(path):
    base, ext = os.path.splitext(path)
    mas = base.split('/')
    return mas[-1]
engine = sq.create_engine('sqlite:///SortDB')

Base = sqlalchemy.orm.declarative_base()
class ModelSort(Base):
    __tablename__ = 'sorting'
    id = sq.Column(sq.Integer, primary_key=True)
    type = sq.Column(sq.String(256))
    subtype = sq.Column(sq.String(256))
    filename = sq.Column(sq.String(256))
    filetype = sq.Column(sq.String(256))
    data = sq.Column(sq.LargeBinary)
Base.metadata.create_all(engine)
counter = 0
with sqlalchemy.orm.Session(autoflush=False, bind=engine) as db:

    for i in range(len(physics())):
        if 'Физика ДЗ' in physics()[i]:
            obj = ModelSort(id = i, type = 'Физика', subtype = "Физика ДЗ",filename = get_filename(physics()[i]) , filetype = get_type(physics()[i]) , data = open(physics()[i], 'rb').read())
            db.add(obj)
            db.commit()
            counter+=1
        else:
            obj = ModelSort(id = i, type = 'Физика', subtype = "Физика ЛР", filename = get_filename(physics()[i]), filetype = get_type(physics()[i]), data = open(physics()[i], 'rb').read())
            db.add(obj)
            db.commit()
            counter+=1
with sqlalchemy.orm.Session(autoflush=False, bind=engine) as db:
    for i in range(len(docks_for_it)):
        if 'Excel' in docks_for_it[i]:
            obj = ModelSort(id=counter, type='информатика и программирование', subtype="Excel",filename = get_filename(docks_for_it[i]), filetype=get_type(docks_for_it[i]),
                            data=open(docks_for_it[i], 'rb').read())
            db.add(obj)
            db.commit()
            counter += 1
        elif 'Алгоритмизация и программирование Дерюгина' in docks_for_it[i]:
            obj = ModelSort(id=counter, type='информатика и программирование', subtype="Алгоритмизация и программирование Дерюгина",
                            filename=get_filename(docks_for_it[i]),
                            filetype=get_type(docks_for_it[i]),
                            data=open(docks_for_it[i], 'rb').read())
            db.add(obj)
            db.commit()
            counter += 1
        elif 'Алгоритмизация и Программирование Козеева' in docks_for_it[i]:
            obj = ModelSort(id=counter, type='информатика и программирование', subtype="Алгоритмизация и Программирование Козеева",
                            filename=get_filename(docks_for_it[i]),
                            filetype=get_type(docks_for_it[i]),
                            data=open(docks_for_it[i], 'rb').read())
            db.add(obj)
            db.commit()
            counter += 1
        elif 'Высокоуровневое программирование' in docks_for_it[i]:
            obj = ModelSort(id=counter, type='информатика и программирование', subtype="Высокоуровневое программирование",
                            filename=get_filename(docks_for_it[i]),
                            filetype=get_type(docks_for_it[i]),
                            data=open(docks_for_it[i], 'rb').read())
            db.add(obj)
            db.commit()
            counter += 1
        elif 'Информатика Акименко' in docks_for_it[i]:
            obj = ModelSort(id=counter, type='информатика и программирование', subtype="Информатика Акименко",
                            filename=get_filename(docks_for_it[i]),
                            filetype=get_type(docks_for_it[i]),
                            data=open(docks_for_it[i], 'rb').read())
            db.add(obj)
            db.commit()
            counter += 1
        elif 'Информатика Антипова' in docks_for_it[i]:
            obj = ModelSort(id=counter, type='информатика и программирование', subtype="Информатика Антипова",
                            filename=get_filename(docks_for_it[i]),
                            filetype=get_type(docks_for_it[i]),
                            data=open(docks_for_it[i], 'rb').read())
            db.add(obj)
            db.commit()
            counter += 1
        elif 'Информатика Глебов' in docks_for_it[i]:
            obj = ModelSort(id=counter, type='информатика и программирование', subtype="Информатика Глебов",
                            filename=get_filename(docks_for_it[i]),
                            filetype=get_type(docks_for_it[i]),
                            data=open(docks_for_it[i], 'rb').read())
            db.add(obj)
            db.commit()
            counter += 1
        elif 'Информатика Козеева' in docks_for_it[i]:
            obj = ModelSort(id=counter, type='информатика и программирование', subtype="Информатика Козеева",
                            filename=get_filename(docks_for_it[i]),
                            filetype=get_type(docks_for_it[i]),
                            data=open(docks_for_it[i], 'rb').read())
            db.add(obj)
            db.commit()
            counter += 1
        elif 'Язык программирования Си' in docks_for_it[i]:
            obj = ModelSort(id=counter, type='информатика и программирование', subtype="Язык программирования Си",
                            filename=get_filename(docks_for_it[i]),
                            filetype=get_type(docks_for_it[i]),
                            data=open(docks_for_it[i], 'rb').read())
            db.add(obj)
            db.commit()
            counter += 1
        elif 'Информатика Крысин' in docks_for_it[i]:
            obj = ModelSort(id=counter, type='информатика и программирование', subtype="Информатика Крысин",
                            filename=get_filename(docks_for_it[i]),
                            filetype=get_type(docks_for_it[i]),
                            data=open(docks_for_it[i], 'rb').read())
            db.add(obj)
            db.commit()
            counter += 1
        elif 'Информатика Лавренков' in docks_for_it[i]:
            obj = ModelSort(id=counter, type='информатика и программирование', subtype="Информатика Лавренков",
                            filename=get_filename(docks_for_it[i]),
                            filetype=get_type(docks_for_it[i]),
                            data=open(docks_for_it[i], 'rb').read())
            db.add(obj)
            db.commit()
            counter += 1
        elif 'Информатика Матлаб' in docks_for_it[i]:
            obj = ModelSort(id=counter, type='информатика и программирование', subtype="Информатика Матлаб",
                            filetype=get_type(docks_for_it[i]),
                            data=open(docks_for_it[i], 'rb').read())
            db.add(obj)
            db.commit()
            counter += 1
        elif 'Математические основы информатики' in docks_for_it[i]:
            obj = ModelSort(id=counter, type='информатика и программирование', subtype="Математические основы информатики",
                            filename=get_filename(docks_for_it[i]),
                            filetype=get_type(docks_for_it[i]),
                            data=open(docks_for_it[i], 'rb').read())
            db.add(obj)
            db.commit()
            counter += 1
        elif 'Не понятно куда деть' in docks_for_it[i]:
            obj = ModelSort(id=counter, type='информатика и программирование', subtype="Не понятно куда деть",
                            filename=get_filename(docks_for_it[i]),
                            filetype=get_type(docks_for_it[i]),
                            data=open(docks_for_it[i], 'rb').read())
            db.add(obj)
            db.commit()
            counter += 1
        elif 'ООП' in docks_for_it[i]:
            obj = ModelSort(id=counter, type='информатика и программирование', subtype="ООП",
                            filename=get_filename(docks_for_it[i]),
                            filetype=get_type(docks_for_it[i]),
                            data=open(docks_for_it[i], 'rb').read())
            db.add(obj)
            db.commit()
            counter += 1
        elif 'Основы программирования Антипова' in docks_for_it[i]:
            obj = ModelSort(id=counter, type='информатика и программирование', subtype="Основы программирования Антипова",
                            filename=get_filename(docks_for_it[i]),
                            filetype=get_type(docks_for_it[i]),
                            data=open(docks_for_it[i], 'rb').read())
            db.add(obj)
            db.commit()
            counter += 1
        elif 'Основы программной инженерии' in docks_for_it[i]:
            obj = ModelSort(id=counter, type='информатика и программирование', subtype="Основы программной инженерии",
                            filename=get_filename(docks_for_it[i]),
                            filetype=get_type(docks_for_it[i]),
                            data=open(docks_for_it[i], 'rb').read())
            db.add(obj)
            db.commit()
            counter += 1
        elif 'Программирование на основе классов и шаблонов' in docks_for_it[i]:
            obj = ModelSort(id=counter, type='информатика и программирование', subtype="Программирование на основе классов и шаблонов",
                            filename=get_filename(docks_for_it[i]),
                            filetype=get_type(docks_for_it[i]),
                            data=open(docks_for_it[i], 'rb').read())
            db.add(obj)
            db.commit()
            counter += 1
        elif 'Теоретическая информатика' in docks_for_it[i]:
            obj = ModelSort(id=counter, type='информатика и программирование', subtype="Теоретическая информатика",
                            filename=get_filename(docks_for_it[i]),
                            filetype=get_type(docks_for_it[i]),
                            data=open(docks_for_it[i], 'rb').read())
            db.add(obj)
            db.commit()
            counter += 1
        elif 'Технологии и методы программирования' in docks_for_it[i]:
            obj = ModelSort(id=counter, type='информатика и программирование', subtype="Технологии и методы программирования",
                            filename=get_filename(docks_for_it[i]),
                            filetype=get_type(docks_for_it[i]),
                            data=open(docks_for_it[i], 'rb').read())
            db.add(obj)
            db.commit()
            counter += 1
with sqlalchemy.orm.Session(autoflush=False, bind=engine) as db:
    for i in range(len(docks)):
        if 'Аналит' in docks[i]:
            obj = ModelSort(id=counter, type='Аналит',
                            subtype="Нет",
                            filename=get_filename(docks[i]),
                            filetype=get_type(docks[i]),
                            data=open(docks[i], 'rb').read())
            db.add(obj)
            db.commit()
            counter += 1
        elif 'Английский' in docks[i]:
            obj = ModelSort(id=counter, type='Английский',
                            subtype="Нет",
                            filename=get_filename(docks[i]),
                            filetype=get_type(docks[i]),
                            data=open(docks[i], 'rb').read())
            db.add(obj)
            db.commit()
            counter += 1
        elif 'Инжа и начерт' in docks[i]:
            obj = ModelSort(id=counter, type='Инжа и начерт',
                            subtype="Нет",
                            filename=get_filename(docks[i]),
                            filetype=get_type(docks[i]),
                            data=open(docks[i], 'rb').read())
            db.add(obj)
            db.commit()
            counter += 1
        elif 'Интегралы' in docks[i]:
            obj = ModelSort(id=counter, type='Интегралы',
                            subtype="Нет",
                            filename=get_filename(docks[i]),
                            filetype=get_type(docks[i]),
                            data=open(docks[i], 'rb').read())
            db.add(obj)
            db.commit()
            counter += 1
        elif 'Линал' in docks[i]:
            obj = ModelSort(id=counter, type='Линал',
                            subtype="Нет",
                            filename=get_filename(docks[i]),
                            filetype=get_type(docks[i]),
                            data=open(docks[i], 'rb').read())
            db.add(obj)
            db.commit()
            counter += 1
        elif 'МатАнал' in docks[i]:
            obj = ModelSort(id=counter, type='МатАнал',
                            subtype="Нет",
                            filename=get_filename(docks[i]),
                            filetype=get_type(docks[i]),
                            data=open(docks[i], 'rb').read())
            db.add(obj)
            db.commit()
            counter += 1
        elif 'Метрология и технические измерения в производстве ЭС' in docks[i]:
            obj = ModelSort(id=counter, type='Метрология и технические измерения в производстве ЭС',
                            subtype="Нет",
                            filename=get_filename(docks[i]),
                            filetype=get_type(docks[i]),
                            data=open(docks[i], 'rb').read())
            db.add(obj)
            db.commit()
            counter += 1
        elif 'ММТО' in docks[i]:
            obj = ModelSort(id=counter, type='ММТО',
                            subtype="Нет",
                            filetype=get_type(docks[i]),
                            data=open(docks[i], 'rb').read())
            db.add(obj)
            db.commit()
            counter += 1
        elif 'Практика' in docks[i]:
            obj = ModelSort(id=counter, type='Практика',
                            subtype="Нет",
                            filename=get_filename(docks[i]),
                            filetype=get_type(docks[i]),
                            data=open(docks[i], 'rb').read())
            db.add(obj)
            db.commit()
            counter += 1
        elif 'Рефераты' in docks[i]:
            obj = ModelSort(id=counter, type='Рефераты',
                            subtype="Нет",
                            filename=get_filename(docks[i]),
                            filetype=get_type(docks[i]),
                            data=open(docks[i], 'rb').read())
            db.add(obj)
            db.commit()
            counter += 1
        elif 'Схемотехника' in docks[i]:
            obj = ModelSort(id=counter, type='Схемотехника',
                            subtype="Нет",
                            filename=get_filename(docks[i]),
                            filetype=get_type(docks[i]),
                            data=open(docks[i], 'rb').read())
            db.add(obj)
            db.commit()
            counter += 1
        elif 'Теор.Мех-' in docks[i]:
            obj = ModelSort(id=counter, type='Теор.Мех-',
                            subtype="Нет",
                            filename=get_filename(docks[i]),
                            filetype=get_type(docks[i]),
                            data=open(docks[i], 'rb').read())
            db.add(obj)
            db.commit()
            counter += 1
        elif 'Тервер' in docks[i]:
            obj = ModelSort(id=counter, type='Тервер',
                            subtype="Нет",
                            filename=get_filename(docks[i]),
                            filetype=get_type(docks[i]),
                            data=open(docks[i], 'rb').read())
            db.add(obj)
            db.commit()
            counter += 1
        elif 'ТКМ' in docks[i]:
            obj = ModelSort(id=counter, type='ТКМ',
                            subtype="Нет",
                            filename=get_filename(docks[i]),
                            filetype=get_type(docks[i]),
                            data=open(docks[i], 'rb').read())
            db.add(obj)
            db.commit()
            counter += 1
        elif 'ФОМЭ' in docks[i]:
            obj = ModelSort(id=counter, type='ФОМЭ',
                            subtype="Нет",
                            filename=get_filename(docks[i]),
                            filetype=get_type(docks[i]),
                            data=open(docks[i], 'rb').read())
            db.add(obj)
            db.commit()
            counter += 1
        elif 'ФХОМиНТ' in docks[i]:
            obj = ModelSort(id=counter, type='ФХОМиНТ',
                            subtype="Нет",
                            filename=get_filename(docks[i]),
                            filetype=get_type(docks[i]),
                            data=open(docks[i], 'rb').read())
            db.add(obj)
            db.commit()
            counter += 1
        elif 'Химия' in docks[i]:
            obj = ModelSort(id=counter, type='Химия',
                            subtype="Нет",
                            filetype=get_type(docks[i]),
                            data=open(docks[i], 'rb').read())
            db.add(obj)
            db.commit()
            counter += 1
        elif 'ЭАСЗИ' in docks[i]:
            obj = ModelSort(id=counter, type='ЭАСЗИ',
                            subtype="Нет",
                            filename=get_filename(docks[i]),
                            filetype=get_type(docks[i]),
                            data=open(docks[i], 'rb').read())
            db.add(obj)
            db.commit()
            counter += 1
        elif 'Электротехника' in docks[i]:
            obj = ModelSort(id=counter, type='Электротехника',
                            subtype="Нет",
                            filename=get_filename(docks[i]),
                            filetype=get_type(docks[i]),
                            data=open(docks[i], 'rb').read())
            db.add(obj)
            db.commit()
            counter += 1
print('База данных сформированна')







