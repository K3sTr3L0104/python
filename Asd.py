from operator import indexOf

class Eredmeny:
    nev: str
    rajtszam: int
    kategoria: str
    ido: str
    tavSzazalek: int

    def __init__(self, sor:str) -> None:
        adatok = sor.split(";")
        self.nev = adatok[0]
        self.rajtszam = int(adatok[1])
        self.kategoria = adatok[2]
        self.ido = adatok[3]
        self.tavSzazalek = int(adatok[4])

#5 Készítsen egy függvényt, amely megkapja a versenyző időeredményét, majd visszaadja az időt órában.
def idoOraban(ido):
    hours = list(map(int, ido.split(":")))
    secs = hours[2] + hours[1] * 60 + hours[0] * 3600
    return secs/3600


#Fájl megnyitása
file1 = open("ub2017egyeni.txt", "r")
file1.readline()
#Objektumlista létrehozása
osszesEredmeny = []
#objektum lista feltöltése
for sor in file1:
    egyEredmeny = Eredmeny(sor.strip())
    osszesEredmeny.append(egyEredmeny)
#lista hosszának kiíratása
print("A listában ", len(osszesEredmeny), " eredmény van.")
#hány női induló teljesítette a teljes távot
noiDb = 0
for egyAdat in osszesEredmeny:
    if egyAdat.kategoria == "Noi" and egyAdat.tavSzazalek == 100:
        noiDb = noiDb + 1

print(noiDb)
#2: Kérj be egy nevet, határozd meg, hogy indult-e, ha indult, mekkora távot teljesített
keresettNev = input("Kérem adja meg a keresett sportoló nevét:")
vanKeresett = False
for egyAdat in osszesEredmeny:
    if egyAdat.nev == keresettNev:
        vanKeresett == True
        print("szerepel")
        if egyAdat.tavSzazalek == 100:
            print(egyAdat.nev, "teljesítette a teljes távot")

if not vanKeresett:
    print("Nem indult")
        

#4-es feladat első sportoló idejét kiíratni:
ido = osszesEredmeny[0].ido.split(":")
oraban = (int(ido[0])*3600 + int(ido[1])*60 + int(ido[2])) / 3600
print(oraban)
#6 Határozza meg a teljes távot teljesítő, férfi sportolók átlagos idejét órában
ido = osszesEredmeny[0].ido
hours = list(map(int, ido.split(":")))
secs = hours[2] + hours[1] * 60 + hours[0] * 3600
print(round(secs/3600, 3))

for egyAdat in osszesEredmeny:
    print("Ezt az időt futotta:",idoOraban(egyAdat.ido))
    
    
count = 0
idohoz = 0
    
for egyAdat in osszesEredmeny:
    if egyAdat.kategoria == "Ferfi" and egyAdat.tavSzazalek == 100:
        count += 1
        idohoz += idoOraban(egyAdat.ido)
print(count)
print(idohoz/count)
#hány célba érkező versenyző van, akinél se az előtte levő se az utána levő nem ért be a célba
darab = 0
for i in range(1,len(osszesEredmeny)-1):
    if osszesEredmeny[i].tavSzazalek == 100 and osszesEredmeny[i-1].tavSzazalek < 100 and osszesEredmeny[i+1].tavSzazalek < 100:
        darab += 1
print(darab)