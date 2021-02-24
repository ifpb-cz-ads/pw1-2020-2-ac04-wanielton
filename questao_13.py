# Questão 13:

quant_num = ''
num_qtn = 0
soma = 0

while quant_num != 0:

    def sair():
        if quant_num == 0:
            print('*'*50)
            media = (soma/num_qtn-1)
            print(f' A Média é aritimética é : {media}')
            print('Saindo do programa...')
            exit(1)

    print('Digite um número Inteiro ou digite 0 para sair] :')
    quant_num = int(input())
    soma += quant_num
    if quant_num == 0:
        sair()
    num_qtn += 1
    print(f' A quantidade de números digitados foram : {int(num_qtn)}')
    print(f' A Soma dos números digitados é : {int(soma)}')