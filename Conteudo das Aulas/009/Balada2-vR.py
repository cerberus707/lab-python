"""
Estruturas de decisao: IF e Else (se nao ou caso contrario)
':' no python, substitui o then
a condicao if so depende de resposta True ou Fale, exeplo case 2
"""

#Case 1
idade = int(input('Quantos Anos voce tem?'))
resp = idade >= 18


if resp == True: 
    print('Voce pode beber a vontade')

if resp == False:
    print ('Voce so pode beber refrigerante')
    
print (resp) 


#Case 2
idade = int(input('Quantos Anos voce tem?'))
resp = idade >= 18

if resp: 
    print('Voce pode beber a vontade')

if resp != True:
    print ('Voce so pode beber refrigerante')
    
print (resp) 

#Case 3
idade = int(input('Quantos Anos voce tem?'))
if idade >= 18: 
    print('Voce pode beber a vontade')

if idade < 18:
    print ('Voce so pode beber refrigerante')
    


#Case 4
idade = int(input('Quantos Anos voce tem?'))
if idade >= 18: 
    print('Voce pode beber a vontade')
    if idade >= 21:
        print ('Voce é cliente VIP')

if idade < 18:
    print ('Voce so pode beber refrigerante')


#Adocao do ELSE    
#Case 1
idade = int(input('Quantos Anos voce tem?'))
if idade >= 18: 
    print('Voce pode beber a vontade')
    if idade >= 21:
        print ('Voce é cliente VIP')

else:
    print ('Voce so pode beber refrigerante')


#Case 2
if 1 > 1: 
    Print('Sim')
else:
    print('nao')