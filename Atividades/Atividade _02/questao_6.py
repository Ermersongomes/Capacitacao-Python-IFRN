'''
6. Desenvolva um algoritmo em Python que armazene o seu peso em uma variável, e a sua altura em outra variável. O programa deve realizar o cálculo do IMC deste usuário através da seguinte fórmula: IMC = peso/altura2. Ao final, o valor do IMC deve ser impresso.

'''

peso = float(input("Digite seu peso: "))
altura = float(input("Digitte sua altura: "))

imc = peso // (altura * 2)

print('seu imc é ', imc )