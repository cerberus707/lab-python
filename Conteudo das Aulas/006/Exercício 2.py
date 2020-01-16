"""
Organize os numeros 2,3,4,5,10,12 para obter a saída 18
em uma única operação:
x = 12*3
x = x + 4
x = x//10
x = x*5
x = x - 2
print(x)
"""

x = 12*3 #36 
x = x + 4 #40 
x = x//10 #4
x = x*5 #20
x = x - 2 #18
print(x)

x = ((12 * 3 + 4) // 10 * 5) -2 

print(x)