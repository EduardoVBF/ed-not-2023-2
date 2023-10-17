from lib.stack import Stack
from data.nomes import nomes

# Criando uma nova pilha
p = Stack()

# inversão da ordem dos nomes

# Empilhamento
for nome in nomes:
    p.push(nome)

lista_inversa = []

# Desempilhamento
while not p.is_empty():
    lista_inversa.append(p.pop())

# Imprimir a lista inversa
print("Lista Invertida: ", lista_inversa)