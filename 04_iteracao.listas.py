#lista de frutas
frutas = ["Laranja", "Maçã", "Uva", "Pera", "Mamão", "Abacate", "Amora"]

#Para percorrer uma lista e exibir apenas seus elementos,
#usamos a estrutura FOR..IN

for f in frutas:
    print(f)

print('-' * 30)

#Imprimindo uma lista de trás para frente: reversed()
for x in reversed(frutas):
    print(x)

print('-' * 30)

# No entanto, frequentemente precisamos exibir, além do
# valor do elemento, também sua posição. Nesse caso devemos
# usar a estrutura FOR...IN combinada com as funções range() e len()
for pos in range(len(frutas)):
  # print(frutas[pos], ":", pos)
  # print("A fruta", frutas[pos], "está na posição", pos, ".")
  print(f"A fruta {frutas[pos]} está na posição {pos}.")

print('-' * 30)

# Algumas vezes é necessário percorrer a lista de trás para a frente,
# mas tendo acesso também à posição dos elementos. Para isso,
# usamos a estrutura FOR...IN, range() com três parâmetros e len().
for i in range(len(frutas) -1, -1, -1):
    print(f"A fruta {frutas[i]} está na posição {i}.")