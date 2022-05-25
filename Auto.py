class Auto:
    marka = str
    evjarat: int
    szin: str
    hengerurtartalom: int

    def __init__(self, markaja:str, evjarata:int, szine:str, hengerurtartalma:int) -> None:
        self.marka = markaja
        self.evjarat = evjarata
        self.szin = szine
        self.hengerurtartalom = hengerurtartalma 
    def dudal(self):
        print("Piiiiiiiiiip")
Autom = Auto("Audi", 1996, "kék", 1300)
print("Az autóm márkája:", Autom.marka,)
print("Az autóm évjárata:", Autom.evjarat)
print("Az autóm színe:", Autom.szin)
print("Az autóm hengerűrtartalma:", Autom.hengerurtartalom)
Autom.dudal()