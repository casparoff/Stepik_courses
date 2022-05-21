tk_number = int(input())
a = tk_number % 10
b = (tk_number % 100) // 10
c = (tk_number % 1000) // 100
d = (tk_number % 10000) // 1000
e = (tk_number % 100000) // 10000
f = (tk_number % 1000000) // 100000
if a + b + c == d + e + f:
    print('Счастливый')
else:
    print('Обычный')
