# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

def negafibonacci(k):
    fibonacci_list = [1,0,1]
    for i in range(k-1):
        fibonacci_list.append(fibonacci_list[-2]+fibonacci_list[-1])
        fibonacci_list.insert(0,fibonacci_list[1]-fibonacci_list[0])

    return fibonacci_list

number = int(input('Введите целое положительное число: '))
if(number<=0):
    print('Введено некорректное значение')
else:
    print(negafibonacci(number))
