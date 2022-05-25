# Írasd ki az összes sort
f = open("adatok.txt", "r")
for sor in f:
    print("Sor:",sor)

# Olvasd be a fájl első sorát, amely megadja, hogy összesen hány adatsor van.    
f.seek(0)
print("Sorok száma:",f.readline())

# Írasd ki egy sorokszama.txt fájlba a sorok számát. 
f.seek(0)
kiiratas = open("kiiratas.txt", "w")
kiiratas.write(f.readline())

# Írasd ki külön az adatsorokat és külön az összes sorok számát.
for sor in f:
    asd1 = sor.strip().split(";")
    print("Sorok száma a 2. sortól:", asd1)

# a sorokban levő 3 szám szorzatát írd ki. Csak az adatsorokkal dolgozz! 
f.seek(3)
for sor1 in f:
    asd = sor1.strip().split(";")
    print("Szorzat:", int(asd[0])*int(asd[1])*int(asd[2]))