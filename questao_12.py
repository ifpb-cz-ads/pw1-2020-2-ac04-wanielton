# Questão 12:

val_div = float(input("Dívida: "))
taxa = float(input("Juros (Ex.: 3 para 3%): "))
val_men_pag = float(input("Pagamento mensal:"))

mes = 1
saldo = val_div
juros_pago = 0

while saldo > val_men_pag:
    juros = saldo * taxa / 100
    saldo = saldo + juros - val_men_pag
    juros_pago = juros_pago + juros
    print(f"A dívida no mês {mes} é de R${saldo:6.2f}.")
    mes = mes + 1
    
print(f"Para pagar uma dívida de R${val_div:8.2f}, a {taxa:5.2f} % de juros,")
print(f"Serão necessários {mes - 1} meses, pagando um total de R${juros_pago:8.2f} de juros.")
