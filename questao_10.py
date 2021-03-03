# Questão 10:

val_dep = float(input("Valor depositado: "))
taxa = float(input("Taxa de juros: "))

mes = 1
saldo = val_dep

while mes <= 12:
    saldo = saldo + (saldo * (taxa / 100))
    print(f"Mês {mes}: de R${saldo:5.2f}.")
    mes = mes + 1
print(f"O juros em seu total foram de: R${saldo - val_dep:8.2f}")