
"""
Variavel boleano e operadores de comparacao
Sao variaveis que deriva das datas do tipo inteiro, e podem derivar 2 valores: True e False

Principais operadores: 
    Menor = '<' 
    Maior = '>' 
    Maior ou Igual = '>=' 
    Menor ou Igual = '<=' 
    Igual = '==' 
    Diferente = '!='
    
"""
#True = Verdadeiro 
#False = Falso

#Também conhecido como 1 e 0, onde 1 = True e 0 = False

True == 1 
False == 0

#True e false podem ser atribuidos a uma variavel tambem
x = True
y = False

#Programa de verificacao de idade, verificar se o individio tem mais de 18 anos e pode beber
idade = int(input('Quantos Anos voce tem?'))

#perguntas para retorno boleano
14 < 15 #True
14 > 15 #False

pode = idade >= 18
npode = idade < 18

print (pode)
print (npode)

"""
Atencao ao igual (=), ele não serve como sinal de igualdade e sim como sinal de atribuicao 
ou recebimento.
Para igual deve-se usar 2 iguais juntos
"""
18 == 18 #True
18 == 19 #False

"""
Para saber se um numero é diferente de outro, o sinal utilizado é o != e nao <>
""" 
18 != 18 #False
18 != 17 #True

"""
Também pode ser usada a funcao bool, que tem alguns requisitos
"""
#Qualquer numeros inteiro, retorna True, exemplo
x = bool (250)
#Qualquer valor que o python considere nao inteiro, retorna False, exemplo
#(), None, {}, '', "", 0 , 0.0
y, z, x = bool()