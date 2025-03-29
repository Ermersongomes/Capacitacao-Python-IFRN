'''
10. Desenvolva um algoritmo em Python que armazene o valor do salário mínimo e o valor do seu salário. Ao final, o programa deverá imprimir quantos salários mínimos ele ganha.
'''

salario_minimo = float(input("Digite o valor do salário mínimo atual: "))
meu_salario = float(input("Digite o valor do seu salário: "))
qtd_salario = meu_salario // salario_minimo

print("Você receber o equivalante a", qtd_salario, "salários mínimos.")