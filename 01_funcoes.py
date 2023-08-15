# Função que calcula o IMC de uma pessoa
def calc_imc(peso, altura):
    return peso / altura ** 2

# p = 85
# a = 1.72
# imc = calc_imc(p, a)

# print(imc)

print(calc_imc(85, 1.72))

###########################

from math import pi

"""
Função que calcula a área de um figura geométrica plana
"""
def calc_area(base, altura, tipo):
    ## resultado = None (Opção de anular qualquer forma inválida sem ser pelo ultimo else)
 
    if tipo == "R": #Retângulo 
        resultado = base * altura
    elif tipo == 'T': #Triângulo
        resultado = (base * altura)/2
    elif tipo == 'E': #Elipse
        resultado = (base/2) * (altura/2) * pi
    else: #Forma desconhecida
        resultado = None

    return resultado

print ("Retangulo 5x4: ", calc_area(5, 4, "R"))
print ("Triangulo 7x3: ", calc_area(7, 3, "T"))
print ("Elipse 12x8: ", calc_area(12, 8, "E"))
print ("Desconhecido 5x7: ", calc_area(5, 7, "X"))