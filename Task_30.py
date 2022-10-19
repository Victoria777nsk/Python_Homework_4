# 30. Есть два файла: в одном хранятся ФИО пользователей сайта (users.txt), а в другом — данные об их хобби (hobby.txt). 
# Известно, что при хранении данных используется принцип: одна строка — один пользователь. 
# Написать код, загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО, значения — данные о хобби.
# Сохранить словарь в файл users_hobby.txt. 

list_users = []
with open ('users.txt', 'r', encoding = 'utf8') as list1:
    for line in list1:
        list_users.append(line.replace('\n', ''))
print(f'ФИО: {list_users}')                                # Создаем и выводим список с данными о пользователях.

list_hobbies = []
with open ('hobby.txt', 'r', encoding = 'utf8') as list2:
    for line in list2:
        list_hobbies.append(line.replace('\n', ''))
print(f'Хобби: {list_hobbies}')                            # Создаем и выводим список с данными о хобби.

my_dict = dict(zip(list_users, list_hobbies))
print(f'Словарь: {my_dict}')                               # Объединяем элементы из двух списков и создаем из них словарь.
 

geeky_file = open('users_hobby.txt', 'wt', encoding = 'utf8') # Сохраняем словарь в файл users_hobby.txt.
geeky_file.write(str(my_dict))
geeky_file.close()