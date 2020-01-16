"""
Comparacoes Multiplas
False sempre terá prioridade sobre o True
IMPORTANTE
1. Comparacao fora do parenteses são encadeadas
2. Compoaracoes dentro do paratese sao distintas e podem ser comparadas entre si
"""

#Exemplo 1 para comparacoes multiplas

    1<2<3<4 #Resultado - True
    1<2<3<4<3 #Resultado - False

#Exemplo 2 para comparacoes multiplas
    a = 3
    1 < a
    
    1 < a < 5 """Este caso todas as condicoes sao verdadeiras, então é true"""
    
    1 < a < 2 """Este caso um das condicoes é falso, então é falso"""

    1 > a < 5 """Este caso um das condicoes é falso, então é falso"""

#Exemplo 2 para comparacões multiplas, importante.

(1 < 2) < 2 """Comparacoes distitas, aquio resultado é True, por que, true =1 e 1 é menor que 2"""

"""Bom exeplo para demostrar como o boleano se comporta
   Quando fechamos o parentes, ele passa a ser comparado com o valor de fora.
"""
True = 1 < 3 > False = 0
(1 < 2) < 3 > (2 > 3)
    
#Case 1
idade = int(input('Digite Sua Idade:'))

if idade >= 18:
    if idade < 70:
        print('Voce pode receber o beneficio')
    else: 
        print('Voce nao pode receber o beneficio')
else:
    print('Voce nao pode receber o beneficio')
    

#Case 2
idade = int(input('Digite Sua Idade:'))

if 18 <= idade  < 70: #A partir de 70 anos voce é considerado idoso
        print('Voce pode receber o beneficio')
else: 
        print('Voce nao pode receber o beneficio')
