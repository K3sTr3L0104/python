def grading(goalcount: int):
    if goalcount <= 2:
        print("Gyenge")
    elif goalcount <= 5:
        print("Közepes")
    elif goalcount >= 6:
        print("Kiválló")

golokLista = []
golokOsszeg = 0
golokAtlaga = 0
file1 = open("golok.txt", "r", encoding="utf-8")


for i in file1:
    golokLista.append(int(i))
    golokOsszeg += int(i)

golokAtlaga = golokOsszeg / len(golokLista)

grading(golokOsszeg)