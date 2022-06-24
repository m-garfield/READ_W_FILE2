# получаем список файлов в каталог
import os
dec_files = {}
for file in os.listdir():
    if file.endswith(".txt"):
        with open(file, "r", encoding="utf-8") as file_txt:
            list_data_file = []
            data_file = file_txt.read().split("\n")
            tuple_file = [(len(data_file)),(data_file)]
            dec_files[file] = tuple_file
sorted_files = sorted(dec_files.values())
for write_files_data in sorted_files:
    for write_file_line in write_files_data[1]:
        with open(("4.txt"),"a+", encoding="utf-8") as new_files:
            new_files.write(write_file_line + "\n")




    # with open(("4.txt"),"a+", encoding="utf-8") as new_files:
    #     new_files.write((write_files_data[1][0]) + "\n")

# print(sorted_files)
# в цикле читаем файлы и формируем словарь где ключь имя файла значение -кортеж где указано количество строк и данные файла



# сортируем словарь и записываем новый файл
