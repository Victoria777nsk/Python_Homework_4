# 32. Задайте последовательность чисел. Напишите программу, которая выведет 
# список неповторяющихся элементов исходной последовательности.

numbers = list(map(int, input('Введите числа через пробел: ').split()))
found = set()
found_again = set()

for number in numbers:
    if number in found_again:
        continue
    if number in found:
        found.remove(number)
        found_again.add(number)
    else:
        found.add(number)

print(f'Элементы, не имеющие повторений: {list(found)}')