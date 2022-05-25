# OSZTÁLY:

from xmlrpc.client import Boolean


class Haromszog:
    a: int
    b: int
    c: int
    
    
    # konstruktor
    def __init__(self, sorom) -> None:
        self.a = int(sorom[0])
        self.b = int(sorom[1])
        self.c = int(sorom[2])    
        
    # osztály metódusa: szöveggel visszatérve megmondja, hogy a számok háromszöget alkotnak-e    
    def haromszoge(self) -> str:
        if self.a<self.b+self.c and self.b<self.a+self.c and self.c<self.a+self.b:
            return "Háromszöget alkotnak"
        else:
            return "Nem alkotnak háromszöget."
    def derekszogue(self)-> bool:
        return (self.a*self.a)+(self.b*self.b) == (self.c*self.c)
    
    def vanekilenc(self, bekert)-> bool:
        return self.a == bekert or self.b == bekert or self.c == bekert

    
    # osztály metódusa: egész számként visszaadja a háromszög kerületét
    def kerulet(self)-> int:
        return self.a + self.b + self.c
#fájl megnyitása
file = open("haromszog.txt", "r", encoding="utf_8")
file.readline()
#2D lista létrehozása
lista = []
for i in file:
    lista.append(i.strip().split("*"))
print(lista)
for sor in lista:
    egyHaromszog = Haromszog(sor)
    print(egyHaromszog.haromszoge(),"kerülete:", egyHaromszog.kerulet())
#Kérj be a felhasználótól 3 számot (megfelelő adatszerkezetben), majd írd ki neki, hogy háromszöget alkotnak-e!
szam1 = int(input("Add meg egy háromszög oldalát:"))
szam2 = int(input("Add meg a háromszög másik oldalát:"))
szam3 = int(input("Add meg a háromszög harmadik oldalát:"))
lista2 = []
lista2.append(szam1)
lista2.append(szam2)
lista2.append(szam3)
print(lista2)
egyHaromszog = Haromszog(lista2)
print(egyHaromszog.haromszoge())
print(egyHaromszog.derekszogue())
#írj egy új osztály metódust, amelyik logikai értékként megadja, hogy szerepel-e benne egy paraméterként megadott szám (ezt a felhasználótól kérd be)!
bekert = int(input("Adj meg egy számot:"))
print(egyHaromszog.vanekilenc(bekert))
