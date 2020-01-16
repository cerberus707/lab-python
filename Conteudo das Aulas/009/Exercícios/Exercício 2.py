"""
Faça um Programa para uma loja de tintas.

O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados
e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou
em galões de 4 litros, que custam R$ 25,00.

Informe ao usuário as quantidades de tinta a serem compradas e os respectivos
preços em 3 situações:
    comprar apenas latas de 18 litros;
    comprar apenas galÃµes de 4 litros;
    misturar latas e galÃµes, de forma que o preço seja o menor.

Acrescente 10% de folga e sempre arredonde os valores para cima, isto é,
considere latas cheias
    int()
    //
    %
    if
"""



area = int(input('Qual o tamanho da área?'))
litros = area//6 #Onde 6 é o minimo para pintar uma area, ou seja,  6*18  é a area total
lata = litros//18 #Onde 18 é o total da lata
galao = litros //4


if area % 6 > 0:
    area = area + 1
else:
    area    


if litros % 18 > 0:
    litros = litros + 1
else:
    litros

    
print ('voce vai precisar de', litros, 'Litros(s) de tinta, ', 'Ou', galao, 'Galões')
print ('voce vai gastar R$', ((lata*80) * 0.10 + (lata*80)), 'Em Latas', 'Ou R$', ((galao*25)*0.10 + (galao*25)), 'Em Galões')
print('Voce pagará R$', 80//18, 'Por Litro da Lata e R$', 25//4, 'Por Litro do Galão')

