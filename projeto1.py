# Fatorial de um número
'''
# Crie um programa que recebe um número e imprime seu fatorial.

# Método 5Qs para montar um algoritmo:
1. Quais são os dados de entrada necessários?
- numero
2. O que devo fazer com estes dados?
- calcular o fatorial e exibir na tela o resultado
3. Quais são as restrições deste problema?
- número positivo e inteiro
4. Qual é o resultado esperado?
- resultado do fatorial
5. Qual é sequência de passos a ser feitas para chegar ao resultado esperado?
-elaborar pseudocódigo
#Pseudogódigo
input numero
if numero < 0
if numero = inteiro
fatorial = 1
loop de 1 a numero
fatorial = fatorial * numero
print fatorial
'''

numero = int(input('Digite um número'))
if numero > 0:
  fatorial = 1
  for item in range (1,numero +1):
    fatorial = fatorial * item
  print(fatorial)
          