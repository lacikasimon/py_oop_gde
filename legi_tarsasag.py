# Légitársaság osztály
class LegiTarsasag:
    def __init__(self, nev):
        self.nev = nev
        self.jaratok = []

    def jarat_hozzaadasa(self, jarat):
        # print(f"[DEBUG] Járat hozzáadása: {jarat.jarat_info()}")
        self.jaratok.append(jarat)

    def listaz_jaratok(self):
        print("Elérhető járatok:")
        for jarat in self.jaratok:
            print(jarat.jaratszam)

    def __str__(self):
        return f"Légitársaság: {self.nev}, Járatok száma: {len(self.jaratok)}"
