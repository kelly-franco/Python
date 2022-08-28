#Projeto 3 - Medidor de velocidade
#Analise criticamente o problema e descubra:
'''
Levando em consideração a velocidade máxima permitida de 80km em uma determinada rua. Crie um programa que recebe do usuário um valor que representa a velocidade e com base nessa velocidade diga se ele tomou um multa leve, grave ou gravíssima. Levando em consideração que se a pessoa estiver abaixo da velocidade máxima seu programa deve exibir "não houve multa", caso esteja até 10km acima, deve exibir: "levou multa leve", caso esteja entre 11 a 20km acima da velocidade máxima, exibir: "levou multa grave", e caso esteja acima de 20km acima da velocidade máxima, exiba: "levou multa gravíssima".

Tente explicar este problema para você mesmo em voz alta e
peça mais informações/investigue mais até você
compreender completamente o problema.)

1. Quais são os dados de entrada necessários?
- velocidade
2. O que devo fazer com estes dados?
- comparar a velocidade que a pessoa passou e a permitida e informar o estatus, se a pessoa estiver abaixo da velocidade máxima seu programa deve exibir "não houve multa", caso esteja até 10km acima, deve exibir: "levou multa leve", caso esteja entre 11 a 20km acima da velocidade máxima, exibir: "levou multa grave", e caso esteja acima de 20km acima da velocidade máxima, exiba: "levou multa gravíssima".
3. Quais são as restrições deste problema?
4. Qual é o resultado esperado?
- o resultado esperado e exibir na tela o nivel da multa que a pessoa levou "se a pessoa estiver abaixo da velocidade máxima seu programa deve exibir "não houve multa", caso esteja até 10km acima, deve exibir: "levou multa leve", caso esteja entre 11 a 20km acima da velocidade máxima, exibir: "levou multa grave", e caso esteja acima de 20km acima da velocidade máxima, exiba: "levou multa gravíssima"
5. Qual é sequência de passos a ser feitas para chegar ao resultado esperado?(faça essa parte em pseudocódigo)
input velocidade
velocidade_maxima = 80
if velocidade <= velocidade_maxima
print 'não levou multa'
if velocidade > velocidade_maxima <= velocidade_maxima + 10:
print 'levou multa leve'
if velocidade > velocidade_maxima + 11 <= velocidade_maxima + 20:
print 'levou multa grave'
if velocidade > velocidade_maxima + 20:
print 'levou multa gravissima!'
'''
velocidade = int(input('Digite sua velocidade: '))
velocidade_maxima = 80
if velocidade <= velocidade_maxima:
  print('Não levou multa')
elif velocidade > velocidade_maxima and velocidade <= velocidade_maxima + 10:
  print('Levou multa leve')
elif velocidade >= velocidade_maxima + 11 and velocidade <= velocidade_maxima + 20:
  print('Levou multa grave')
elif velocidade > velocidade_maxima + 20:
  print('Levou multa gravíssima')