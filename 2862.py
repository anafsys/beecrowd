c = int(input())

lista = []

for _ in range(c):
    c = int(input())
    if c <= 8000:
        lista.append("Inseto!")
    else:
        lista.append("Mais de 8000!")

for elemento in lista:
    print(elemento)

        

'''
while True:
    x,y = map(int, input().split(" "))
    
    if x > y:
        lista.append("Decrescente")
    if x < y:
        lista.append("Crescente")
    if x == y:
        break
'''
