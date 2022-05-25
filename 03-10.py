#Írj egy logikai értéket visszatérő Python függvényt, amely paraméterként kap három számot, és eldönti, hogy az összes paraméter pozitív-e!

def isPositive(x: int, y: int, z: int) -> bool:
    return x > 0 and y > 0 and z > 0

a = int(input("Kérem adja meg az első számot: "))
b = int(input("Kérem adja meg a második számot: "))
c = int(input("Kérem adja meg a harmadik számot: "))

if isPositive(a,b,c):
    print("A függvény bemeneti paramétere.")
else:
    print("Függvény név, aktuális paraméter(ek) és értéktípusa(ik), visszatérési érték típusa.")