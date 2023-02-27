import os
import shutil
from zipfile import ZipFile

path = 'D:/Мотлох/'
list_ = os.listdir(path)
slovn = {'video': ['AVI', 'MP4', 'MOV', 'MKV'],
         'images': ['JPEG', 'PNG', 'JPG', 'SVG'],
         'documents': ['DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX'],
         'audio': ['MP3', 'OGG', 'WAV', 'AMR'],
         'archives': ['ZIP', 'GZ', 'TAR'], }
# Створюємо функцію для переміщення файлів, окрім архіва, бо для архівів є окрема функція


def move(type):
    # Перевіряю чи існує папка, а потім переміщаю, у випадку якщо такої  папки нема створюю її
    if os.path.exists(path+'/'+type):
        shutil.move(re_name_path, path+'/'+type+'/'+re_name)
    else:
        os.makedirs(path+'/'+type)
        shutil.move(re_name_path, path+'/'+type+'/'+re_name)


# Окрема функція для архівів
def zip_unpack():
    if os.path.exists(path+'/'+'archives'):
        # Створюємо папку з назвою архіва
        path_zip = os.path.join(path+'/'+'archives', name)
        os.mkdir(path_zip)
        # Беремо розпаковуємо архів у папку
        with ZipFile(re_name_path, 'r') as zip_file:
            zip_file.extractall(
                path=path+'/'+'archives'+'/'+name)
        # Я не дуже впевнений потрібно лі видаляти старий архів з папки Мотлох, так як у завданні не написано видаляти старий архів, але я це добавив не знаю добре чи погано це..
        os.remove(re_name_path)
    else:
        os.makedirs(path+'/'+'archives')
        with ZipFile(re_name_path, 'r') as zip_file:
            zip_file.extractall(
                path=path+'/'+'archives'+'/'+name)

        os.remove(re_name_path)


def normalize(name):
    Ukr = "абвгдежзийклмнопрстуфхцчшщъыьэюяєіїґ"
    Eng = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
           "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")
    TRANS = {}
    for c, l in zip(Ukr, Eng):
        TRANS[ord(c)] = l
        TRANS[ord(c.upper())] = l.upper()
    return name.translate(TRANS)


for file_ in list_:
    # Спершу беремо им'я та тип файла та створюємо шлях до файла
    name, ext = os.path.splitext(file_)
    file_ = os.path.join(path, file_)
    ext = ext[1:]
    # Перевіряю чи це папка и чи вона пуста
    if ext == '':
        if name == 'images' or name == 'documents' or name == 'audio' or name == 'video' or name == 'archives':
            continue
        else:
            if not os.listdir(file_):
                os.rmdir(file_)
            else:
                continue
    else:
        # Далі нормалізую им'я файла та змінюю ім'я файла
        re_name = normalize(name)+'.'+ext
        re_name_path = path+re_name
        os.rename(file_, re_name_path)
        # Перевіряю до якої папки відправляти файл
        for k, v in slovn.items():
            for i in v:
                if ext.upper() == i:
                    if k != 'archives':
                        move(k)
                    else:
                        zip_unpack()
                else:
                    continue
        else:
            continue
