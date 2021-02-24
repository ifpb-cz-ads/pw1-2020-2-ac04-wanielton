# Questão 16:

num = int(input("Digite um número: "))
prim = True

if num % 2 != 0:
    x = 3

    while x <= num:
        if x % 2 != 0:
            if num != x and num % x == 0:
                prim = False
        x += 1
else:
    prim = False

if prim:
    print('É primo')
else:
    print("Não é primo')