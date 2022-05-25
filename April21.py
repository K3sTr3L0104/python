class Meccs:
    fordulo: int
    hazaiGol: int
    vendegGol: int
    hazaiFelidoGol: int
    vendegFelidoGol: int
    hazaiCsapat: str
    vendegCsapat: str


    def __init__(self, sor: str) -> None:
        adatok = sor.strip().split(" ")
        self.fordulo = int(adatok[0])
        self.hazaiGol = int(adatok[1])
        self.vendegGol = int(adatok[2])
        self.hazaiFelidoGol = int(adatok[3])
        self.vendegFelidoGol = int(adatok[4])
        self.hazaiCsapat = adatok[5]
        self.vendegCsapat = adatok[6]
fajl = open("meccs.txt", "r")
fajl.readline()
meccsekObjList: list[Meccs] = []
for i in fajl:
    meccsekObjList.append(Meccs(i))
#Hány mérkőzés van az adatszerkezetünkben?
print(len(meccsekObjList), "mérkőzés volt.")
bekeres = int(input("Adja meg egy forduló számát 1-20 között:"))
for i in meccsekObjList:
    if i.fordulo == bekeres:
        print(i.hazaiCsapat,"-",i.vendegCsapat,":", i.hazaiGol,"-", i.vendegGol, "(",i.hazaiFelidoGol,"-",i.vendegFelidoGol,")")
#csapatnév bekérése
bekeres1 = input("Adj meg egy csapatnevet:")
ertek = False
for i in meccsekObjList:
    if i.hazaiCsapat  == bekeres1 or i.vendegCsapat == bekeres1:
        ertek = True
    else: ertek = False
if (ertek):
    print("Van")
else: print("Nincs")
#Határozza meg, hogy a bajnokság során mely csapatoknak sikerült megfordítaniuk az állást
#Ez azt jekenti, hogy a csapat az első félidőben vesztésre állt ugyan, de sikerült a mérkőzést megfordítani.
#A képernyőn soronként tüntesse fel a forduló számát és a győztes csapat nevét.
for i in meccsekObjList:
    if i.hazaiFelidoGol > i.vendegFelidoGol and i.hazaiGol < i.vendegGol:
        print("Fordítottak")
    if i.hazaiFelidoGol < i.vendegFelidoGol and i.hazaiGol > i.vendegGol:
        print("Fordítottak")
osszeg = 0
for i in meccsekObjList:
    if i.vendegCsapat == "Nyulak":
        osszeg = osszeg + i.vendegGol
print(osszeg)