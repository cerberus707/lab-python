"""
Fa�a um Programa para uma loja de tintas.

O programa dever� pedir o tamanho em metros quadrados da �rea a ser pintada.
Considere que a cobertura da tinta � de 1 litro para cada 6 metros quadrados
e que a tinta � vendida em latas de 18 litros, que custam R$ 80,00 ou
em gal�es de 4 litros, que custam R$ 25,00.

Informe ao usu�rio as quantidades de tinta a serem compradas e os respectivos
pre�os em 3 situa��es:
    comprar apenas latas de 18 litros;
    comprar apenas galões de 4 litros;
    misturar latas e galões, de forma que o pre�o seja o menor.

Acrescente 10% de folga e sempre arredonde os valores para cima, isto �,
considere latas cheias
    int()
    //
    %
    if
"""



area = int(input('Qual o tamanho da �rea?'))
litros = area//6 #Onde 6 � o minimo para pintar uma area, ou seja,  6*18  � a area total
lata = litros//18 #Onde 18 � o total da lata
galao = litros //4


if area % 6 > 0:
    area = area + 1
else:
    area    


if litros % 18 > 0:
    litros = litros + 1
else:
    litros

    
print ('voce vai precisar de', litros, 'Litros(s) de tinta, ', 'Ou', galao, 'Gal�es')
print ('voce vai gastar R$', ((lata*80) * 0.10 + (lata*80)), 'Em Latas', 'Ou R$', ((galao*25)*0.10 + (galao*25)), 'Em Gal�es')
print('Voce pagar� R$', 80//18, 'Por Litro da Lata e R$', 25//4, 'Por Litro do Gal�o')

