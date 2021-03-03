# Questão 14:

val_cod = 0
cont = 0
cod = ""
while cod != 0:

    cod = int(input('Digite o código do Produto : '))
    if cod == 0:
        print(f'Total de items comprados {cont}')
        print(f'Valor das compras foram : {val_cod}')
        exit(1)
    cod_quant = int(input('Quantidade Comprada : '))
    if cod == 1:
        val = cod_quant * 0.5
        val_cod += val
        cont += cod_quant
    elif cod == 2:
        val = cod_quant * 1.0
        val_cod += val
        cont += cod_quant
    elif cod == 3:
        val = cod_quant * 4.0
        val_cod += val
        cont += cod_quant
    elif cod == 5:
        val = cod_quant * 7.0
        val_cod += val
        cont += cod_quant
    elif cod == 9:
        val = cod_quant * 8.0
        val_cod += val
        cont += cod_quant
    else :
        print('Código Inválido')

