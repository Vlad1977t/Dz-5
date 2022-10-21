print("Введите число")
tislo = int(input())
print("Введите систему счисления - 2 или 8 - ую")
sistema = int(input())


if sistema == 2:
    a = ''#cистема счисления
    while tislo > 0:
        a = str(tislo % 2) + a
        tislo = tislo // 2
    print(a)
if sistema == 8:
    c = ''  # cистема счисления
    while tislo > 0:
        c = str(tislo % 8) + c
        tislo = tislo // 8
    print(c)


