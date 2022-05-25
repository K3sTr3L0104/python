#Feladat: Írasd ki azokat a sorokat, melyeknek nincs 3-mal osztható száma
from tokenize import String
from xmlrpc.client import boolean


file = open("haromszogek.txt", "r")
szamok = []
def oszthato(a: int, b: int, c: int):
    if int(a)%3 != 0 and int(b)%3 != 0 and int(c)%3 != 0:
        print(a,b,c)

f = open("forras2.txt", "r")
for sorok in file:
    szamok = sorok.strip().split(" ")
    oszthato(int(szamok[0]),int(szamok[1]),int(szamok[2]))
#Feladat: írasd ki, hogy melyik sor nem osztható 3-mal
def nincsOszthato(egysor: String) -> boolean:
    szamok = egysor.strip().split(";")
    for i in range(len(szamok)):
        if int(szamok[i])%3 == 0:
            return False
    return True

for sor in f:
    if nincsOszthato(sor):
        print(sor)