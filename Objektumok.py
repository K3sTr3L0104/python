#a Kutya osztály létrehozása
class Kutya:
    nev: str
    fajta: str
    szulIdo: int

    def __init__(self, neve:str, fajtaja:str, szulIdo:int) -> None:
        self.nev = neve
        self.fajtaja = fajtaja
        self.szulIdo = szulIdo

    def ugat(self):
        print("Vau vau...")
#Kutya osztályú objektumon létrehozása (példányosítás) -> 1 konkrét kutya
enKutyam = Kutya("Bodri","Német-Juhász",2020)
print("A kutyám neve:",enKutyam.nev)
print("A kutyám kora:",2022-enKutyam.szulIdo)
print("A kutyám fajtája:", enKutyam.fajtaja)

teKutyad = Kutya("Villám","Pudli", 2020)
print("A te kutyád neve",teKutyad.nev,"a fajtája", teKutyad.fajtaja,"és a születési éve:", teKutyad.szulIdo)
#a Kutya osztály metódusának hívása
enKutyam.ugat()