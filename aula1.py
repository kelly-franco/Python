
# Usando variáveis em um programa real
# Problema 1 - Valor por Hora
# Escreva um programa que retorna o valor hora de um funcionário com base no seu salário mensal e horas trabalhadas por mês.
'''
input salario_mensal
input horas_trabalhadas_por_mes
valor_hora = salario_mensal / horas_trabalhadas_por_mes
print valor_hora
'''
salario_mensal = input ('Qual é o seu salário mensal?')
horas_trabalhadas_por_mes = input('Quantas horas você trabalha por mês?')
valor_hora = int(salario_mensal) / int(horas_trabalhadas_por_mes)
print (valor_hora)



