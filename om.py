#üres lista létrehozása
lista = []
#fájl megnyitása
f1 = open("ub2017egyeni.txt", "r", encoding="utf_8")
#első sor kiíratás
f1.readline()
#2d listába olvassuk a fájlt
for sor in f1:
    lista.append(sor.strip().split(";"))
print(lista)
#1 Van-e Zsolt keresztnevű induló
for sor in lista:
    if "Zsolt" in sor[0]:
        print(sor[0])
#2 hány női induló volt
noi = 0
for sor in lista:
    if sor[2] == "Noi":
        noi += 1
print("Ennyi női induló volt:", noi)
#3 átlagosan hány százalékát futották le a távnak
atlag = 0
szam = 0
for sor in lista:
    atlag+=int(sor[4])
    szam+= 1
print("Átlagosan ennyi százalékba futották le:", atlag/szam)
#4 hány férfi futotta le 25 óránál kevesebb idő alatt a teljes távot?
ido = []
count = 0
for sor in lista:
    ido = sor[3].split(":")
    if int(ido[0]) < 25 and sor[2] == "Ferfi" and int(sor[4]) == 100:
        count+= 1
print(count, "25 óránál kevesebb idő alatt teljesítette férfiként a teljes távot.")