import os
import shutil


def searh(source_folder, destination_folder):
#   Проверяем существует ли исходная папка
    if not os.path.exists(source_folder):
       return (f'Путь {source_folder} не найден')

    all_files = []

    #Получаем список всех файлов в папке
    for path in os.listdir(source_folder):
        # Формируем путь до файла
        path_file = source_folder + '/' + path
        # проверяем является ли путь папкой
        if os.path.isdir(path_file):
            # спускаемся на уровень ниже
            searh(path_file, destination_folder_path)
            all_files.append(path_file)
        else:
            all_files.append(path_file)

    for file in all_files:
        if os.path.isfile(file):
            try:
                shutil.move(file, destination_folder)
                print(f"Файл {file} успешно перемещен")
            except Exception as e:
                pass
                print(f"Ошибка перемещения файла {type(e)}")

source_folder_path = "D:/Загрузка/FileZilla/uploads"
destination_folder_path = "D:/Загрузка/FileZilla/all_files"

searh(source_folder_path, destination_folder_path)
