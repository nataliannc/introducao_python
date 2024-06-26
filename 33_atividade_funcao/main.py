"""
Crie um programa que o usuário possa escolher se deseja saber a área de um círculo, de um triângulo ou de um trapézio.
"""

import os

def exibir_menu():
    print("Digite 1 para calcular a área de um círculo.")
    print("Digite 2 para calcular a área de um triângulo.")
    print("Digite 3 para calcular a área de um trapézio.")
    print("Digite 4 para sair do programa")

def calcular_circulo(raio):
    circulo = (raio**2) * 3.14
    return circulo

def calcular_triangulo(base_triangulo, altura_triangulo):
    triangulo = (base_triangulo * altura_triangulo)/2
    return triangulo

def calcular_trapezio(base1, base2, altura_trapezio):
    trapezio = (base1 + base2) * altura_trapezio/2
    return trapezio


while True:
    exibir_menu()
    opcao = input("Digite o número da área que você deseja calcular:")

    os.system('cls')

    if opcao == "1":
        raio = int(input('Informe a base do círculo:'))
        print(f'A área do círculo é {calcular_circulo(raio)}')
    elif opcao == "2":
        base_triangulo = int(input("Informe o valor da base do triângulo:"))
        altura_triangulo = int(input("Informe o valor da altura do triângulo:"))
        print(f'A área do triângulo é {calcular_triangulo(base_triangulo, altura_triangulo)}')
    elif opcao == "3":
        base1 = int(input("Informe o valor da primeira base do trapézio:"))
        base2 = int(input("Informe o valor da segunda base do trapézio:"))
        altura_trapezio = int(input("Informe o valor da altura do trapézio:"))
        print(f'A área do trapézio é {calcular_trapezio(base1, base2, altura_trapezio)}')
    elif opcao == "4":
        print("Você saiu do programa. Volte sempre!")
        break
    else:
        print("Opção invalida!")