n = int(input("Введите любое целое число: "))
m = -1
while n > 0:
    d = n % 10
    if d > m:
        m = d
    n = n // 10
print(m)