"""
Faça um programa para uma loja de tintas.

O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados
e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.

Informe ao usuário a quantidades de latas de tinta
a serem compradas e o preço total.
"""
area = int(input("Digite a �rea a ser pintada: "))

litros = area//3 #Tranformando o valor dos litros em numero inteiro
if area % 3 > 0: #So pra identificar se o valor da area divido por 3 tem resto, se tiver, adicio-se 1 litro
    litros = litros + 1

latas = litros//18#Tranformando o valor dos litros em numero inteiro
if litros % 18 > 0:#So pra identificar se o valor da area divido por 18 tem resto, se tiver, adicio-se 1 litro
    latas = latas + 1

print("Voce precisara de", latas, "latas.")
print("Voce vai pagar R$", latas*80)
