class Eredmeny:
    nev: str
    rajtszam: int
    kategoria: str
    ido: str
    tavSzazalek: int
    def __init__(self, sor: str) -> None:
        adatok = sor.split(";")
        self.nev = adatok[0]
        self.rajtszam = int(adatok[1])
        self.kategoria = adatok[2]
        self.ido = adatok[3]
        self.tavSzazalek = int(adatok[4])

szamlalo = 0   
file = open("ub2017egyeni.txt", "r")
file.readline()
minSzazalek = 100
for i in file:
    #print(i)
    egyAdat = Eredmeny(i)
    print("Neve:",egyAdat.nev, "Ideje:", egyAdat.ido)
    if egyAdat.kategoria == "Noi":
        szamlalo += 1
    if egyAdat.tavSzazalek < minSzazalek:
        minSzazalek = egyAdat.tavSzazalek
print(minSzazalek)
print(szamlalo)
