from random import seed


f = open("haromszogek.txt", "r")
for sor in f:
    print(sor)
lista = []
f.seek(0)
lista.append(f.readline())
print(lista)