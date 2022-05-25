#fájl megnyitása
file = open('orvosi_nobeldijak.txt', 'r', encoding='utf_8')
#lista létrehozása sorok számára
lista = []
#első sor beolvasása
file.readline()
#fájl sorainak bejárása
for sor in file:
    #listához hozzáfűzöm a listává szétdarabolt sort
    lista.append(sor.strip().split(";"))
print(lista[1][3])
#hány angol nobeldijas van?
hanyGb = 0
for sor in lista:
    if sor[3] == "GB":
        hanyGb += 1
print(hanyGb)
for sor in lista:
    if int(sor[0]) < 1905:
        print(sor[1])
for sor in lista:
    if sor[1][0] == "A":
        print(sor[1])
db = 0
for sor in lista:
    if sor[2][-1] == "-":
        szulEv = int(sor[2][1:4])
        print(sor[1], 2022-szulEv)
        db+=1
print(db)