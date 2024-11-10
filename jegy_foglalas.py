# JegyFoglalas osztály
class JegyFoglalas:
    def __init__(self, jarat, utas_nev):
        self.jarat = jarat
        self.utas_nev = utas_nev

    def foglalas_ara(self):
        return self.jarat.jegyar

    def __str__(self):
        return f"Foglalás - Utas: {self.utas_nev}, Járat: {self.jarat.jarat_info()}"
