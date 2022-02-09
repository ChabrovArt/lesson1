n = int(input("Введите любое число от 1 до 9: "))
temp = str(n)
t1 = temp + temp
t2 = temp + temp + temp
comp = n + int(t1) + int(t2)
print("Результат равен:", n, '+', t1, '+', t2, '=', comp)
