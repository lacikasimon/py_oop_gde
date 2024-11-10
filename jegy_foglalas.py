# JegyFoglalas osztály
class JegyFoglalas:
    def __init__(self, jarat, utas_nev, idopont, repules_datuma):
        self.jarat = jarat
        self.utas_nev = utas_nev
        self.idopont = idopont
        self.repules_datuma = repules_datuma

    def foglalas_ara(self):
        return self.jarat.jegyar

    def __str__(self):
        return f"Foglalás - Utas: {self.utas_nev}, Járat: {self.jarat.jarat_info()}, Időpont: {self.idopont}, Repülés dátuma: {self.repules_datuma}"
