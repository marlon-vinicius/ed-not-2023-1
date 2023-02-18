# range(): função que gera uma faixa de números
# É muita usada em associação com listas

# range() com 1 parametro: gera uma faixa que vai
# de 0(zero) até o valor do parâmetro -1
for x in range(10):
    print(x)

print("-" * 80)

# range() com 2 parâmetros: gera uma lista começando pelo 
# primeiro parâmetro (inclusive)até o segundo argumento
# (exclusive, NÃO ENTRA)
for y in range(5,12):
    print(y)

# range com 3 parâmetros:
# 1º: Limite inferior (inclusive)
# 2º: Limite superior (exclusive)
# 3º: passo (de quanto em quanto a lista vai saltar; PODE SER NEGATIVO)
for z in range(0, 22, 3):   #De 0 a 21 santando de 3 em 3
    print (z)

print("-" * 80)

# range() com passo negativo
for k in range(10, 0 , -1):   #Contagem regresiva de 10 até 1
    print(k)