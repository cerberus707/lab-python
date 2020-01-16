"""
Escreva um Programa que imprime dois numeros de sua escolha
e que depois imprime a soma, a subtração, a multiplicação,
a divisão normal e a divisão inteira,
e o resto da divisão do maior pelo menor
(coloque na mensagem a palavra resto ao invez do símbolo %)

EXEMPLO DE SAÍDA:
>>> 
x = 15 
y = 10
15 + 10 = 25
15 - 10 = 5
15 x 10 = 150
15 / 10 = 1.5
15 // 10 = 1
15 resto 10 = 5
>>> 
"""

x = 7
y = 9
soma = x + y
subt = y - x
mult = x * y
div_real = x / y
div_int = x // y 
div_rest = x % y

print ('meus numeros são', x, 'e', y)
print ('O resultado de', y, 'mais', x , 'é igual a', soma)
print ('O resultado de', y, 'menos', x , 'é igual a', subt)
print ('O resultado de', y, 'x', x , 'é igual a', mult)
print ('O resultado de', y, 'sobre', x , 'é igual ao valor real de', div_real)
print ('O resultado de', y, 'sobre', x , 'é igual ao inteiro de', div_int)
print ('O resultado de', y, 'sobre', x , 'é igual ao resto de', div_rest)