# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

def dec_to_binar(num, d_list):
    d_list.append(num % 2)
    if (num//2 <= 0):
        return num % 2
    return dec_to_binar(num//2, d_list)


number = int(input('Введите целое число: '))
digit_list = []
dec_to_binar(number, digit_list)
digit_list.reverse()
print(f'{number} ->', end =' ')
print(*digit_list, sep='')
