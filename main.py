a = int(input())                         #ввод числа которое возводится в степень
b = int(input())                         #ввод степени в которую будет возводится заданое число
def fucl():                              #создание функции fucl
    b1 = 1                               #переменной которой будет присвоен результат вычислений
    for i in range(b):                  
        b1 = b1 * a
    return(b1)                           #возращение результата
print(fucl())                            #вызов функции fucl 
