# Questão 08:

num1 = int(input('Digite o primeiro número (Dividendo): '))
num2 = int(input('Digite o segundo número (Divisor): '))

quociente = 0
x = num1
while x >= num2:
    x = x - num2
    quociente = quociente + 1

resto = x

print('O resultado inteiro é:', quociente)
print('O resto é:', resto)
