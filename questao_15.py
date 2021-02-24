# Questão 15:

def menu():
    menu = False
    while menu != True:
        print('--'*20 +'MENU'+ '--'*20)
        menu = int(input('Digite a opção: \n\
    * [1 - ADIÇÃO]\n\
    * [2 - SUBTRAÇÃO]\n\
    * [3 - DIVISÃO]\n\
    * [4 - MULTIPLICAÇÃO]\n\
    * [0 - SAIR] : '))
    
        if menu == 1:
            num = float(input('Digite o número para elaboração da tabuada: '))
            tab = int(input('Digite a quantidade resultados desejados: '))
            adicao(x=num, y=tab)

        elif menu == 2:
            num = float(input('Digite o número para elaboração da tabuada: '))
            tab = int(input('Digite a quantidade resultados desejados: '))
            subtracao(x=num, y=tab)

        elif menu == 3:
            num = float(input('Digite o número para elaboração da tabuada: '))
            tab = int(input('Digite a quantidade resultados desejados: '))
            divisao(x=num, y=tab)

        elif menu == 4:
            num = float(input('Digite o número para elaboração da tabuada: '))
            tab = int(input('Digite a quantidade resultados desejados: '))
            multiplicacao(x=num, y=tab)

        elif menu == 0:
            sair()
        else:
            print('Dígito incorreto, tente novamente')

def adicao(x, y):
    for i in range(y+1):
        print(f'{x:.0f} + {i:.0f} = {x+i:.0f}')

def subtracao(x, y):
    for i in range(y+1):
        print(f'{x:.0f} - {i:.0f} = {x-i:.0f}')

def multiplicacao(x, y):
    for i in range(y+1):
        print(f'{x:.0f} * {i:.0f} = {x*i:.0f}')

def divisao(x, y):
    for i in range(1 ,y+1):
        print(f'{x:.2f} / {i:.2f} = {x/i:.2f}')


def sair():
    print('Sistema fechado')
    exit(0)

if __name__ == '__main__':
    menu()