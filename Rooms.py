type_figure = str(input())
if type_figure == 'треугольник':
    a = int(input())
    b = int(input())
    c = int(input())
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print(s)
elif type_figure == 'прямоугольник':
    a = int(input())
    b = int(input())
    s = a * b
    print(s)
else:
    a = int(input())
    s = 3.14 * a ** 2
    print(s)
