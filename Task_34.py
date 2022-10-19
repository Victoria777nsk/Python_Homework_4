# 34. *Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
# 2x² + 4x + 5 = 0 и x² + 5x + 3 = 0 => 3x² + 9x + 8 = 0

file_1 = open('Task_34_File_1.txt', 'r')
file_2 = open('Task_34_File_2.txt', 'r')
new_file = open('Task_34_Sum.txt', 'w')  # Создаем новый текстовый файл для вывода суммы многочленов.

file1 = file_1.readline()
file2 = file_2.readline()

for i in range(len(file1)):
    if file1[i-1] != '^':
        if file1[i].isnumeric():   # Проверяем, является ли элемент числом.
            new_file.write(str(int(file1[i]) + int(file2[i])))
        else:
            new_file.write(str(file1[i]))
    else:
        new_file.write(str(file1[i]))

file_1.close
file_2.close
new_file.close