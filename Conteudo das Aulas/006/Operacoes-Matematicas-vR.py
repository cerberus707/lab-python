#Trabalhando com operadores matematicos.
#Atecao a prioridade dos sinais:
  #1.Potecia
  #2.Divisao/multiplicao
  #3.adicao/Subtracao
#Adicao, usa os mesmos criterios matematicos, por exemplo

#Adicao
x = 10
y = 10
soma = x + y - 1 + 1

#(-)Subtracao
#É possivel intercalar variavel com o proprio valor(nao variavel)
sub = x - y
sub2 = 2-1
sub3 = x - 9

#Multiplicacao
mult = x * sub3
mult2 = 5 * 8
mult3 = y * 9

#Divisão (retorna numero real da divisão)
divi = 10 / 3 #(3,333333333333335)
#Divisão (retorna numero inteiro da divisão)
divi_inteiro = 10//3 #(3)
#Divisão (retorna o resto da divisão)
divi_resto = 10%3 #(1)

#Potenciacao
pot = 10**2
pot2 = 10**3

#pela priodade, o numero que virá ser o 11 e nao o 3 como esperado
ordem_oper_err = 10 + 5*3/15 
#pela priodade, de sinais, o valor correto sera o 3
ordem_oper_corr = (10+5) * 3 / 15