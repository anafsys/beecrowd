n = int(input())

total_presentes = 0

for _ in range(n):
    _, g, h = input().split(" ")
    h = int(h)

    if g == 'bonecos':
       total_presentes += h // 8
    elif g == 'arquitetos':
       total_presentes += h // 4
    elif g == 'musicos':
       total_presentes += h // 6
    elif g == 'desenhistas':
       total_presentes += h // 12

print(total_presentes)

''' 
n = int(input())

lista = []

for _ in range(n):
    e, g, h = input().split(" ")
    h = int(h)
   
    if g == 'bonecos':
       p = h // 8
       arred = round(p,1)
       lista.append(arred) 
    if g == 'arquitetos':
       p = h // 4
       arred = round(p,1)
       lista.append(arred)
    if g == 'musicos':
       p = h // 6
       arred = round(p,1)
       lista.append(arred)
    if g == 'desenhistas':
       p = h // 12
       arred = round(p,1)
       lista.append(arred)   

print(round(sum(lista)))
'''










