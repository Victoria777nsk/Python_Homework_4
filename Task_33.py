# 33. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k.
# Пример: k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0

from random import randint

k = int(input('Введите натуральную степень k: '))

polynomial = []
for i in range(1, k + 2):
    polynomial.append(randint(1, 10))   # Формируем случайный список коэффициентов от 1 до 9.

result = []
for i in range(len(polynomial)):
    if k == 1:
        result.append(f'{polynomial[i]}*x')
    elif k == 0:
        result.append(f'{polynomial[i]}')
    else:
        result.append(f'{polynomial[i]}*x^{k}')
    signs = randint(0, 1)
    if signs == 1:
        result.append('+')
    elif signs == 0:
        result.append('-')
    k -= 1

result.pop(-1)                   # Удаляем из последовательности последний лишний знак перед "=".
result.append('= 0')
print(result)

record = open('data.txt', 'w')   # Записываем полученный многочлен в текстовый файл data.txt.
record.write(''.join(result))
record.close()