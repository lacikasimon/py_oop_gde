from legi_tarsasag import LegiTarsasag
from jarat import BelfoldiJarat, NemzetkoziJarat
from jegy_foglalas import JegyFoglalas
from datetime import datetime

# Fő funkciók
class FoglalasiRendszer:
    def __init__(self):
        # print("[DEBUG] FoglalasiRendszer inicializálása...")
        self.foglalasok = []
        self.legi_tarsasag = LegiTarsasag("Példa Légitársaság")
        self.alap_adatok_betoltese()

    def alap_adatok_betoltese(self):
        # print("[DEBUG] Alap adatok betöltése...")
        jarat1 = BelfoldiJarat("B123", "Budapest", 10000)
        jarat2 = NemzetkoziJarat("N456", "London", 50000)
        jarat3 = NemzetkoziJarat("N789", "New York", 80000)

        self.legi_tarsasag.jarat_hozzaadasa(jarat1)
        self.legi_tarsasag.jarat_hozzaadasa(jarat2)
        self.legi_tarsasag.jarat_hozzaadasa(jarat3)

        self.foglalasok.append(JegyFoglalas(jarat1, "Kiss János", datetime.now(), "2024-12-01"))
        self.foglalasok.append(JegyFoglalas(jarat2, "Nagy Anna", datetime.now(), "2024-12-05"))
        self.foglalasok.append(JegyFoglalas(jarat3, "Szabó Péter", datetime.now(), "2024-12-10"))
        # print("[DEBUG] Alap adatok betöltése kész.")

    def jegy_foglalasa(self, jaratszam, utas_nev, repules_datuma):
        # print(f"[DEBUG] Jegy foglalása - Járatszám: {jaratszam}, Utas név: {utas_nev}, Repülés dátuma: {repules_datuma}")
        jarat = self.jarat_keresese(jaratszam)
        if jarat:
            try:
                foglalas_idopont = datetime.now()
                repules_date = datetime.strptime(repules_datuma, "%Y-%m-%d")
                if repules_date <= foglalas_idopont:
                    print("Hiba: A repülés dátuma jövőbeni dátum kell, hogy legyen.")
                    return
                uj_foglalas = JegyFoglalas(jarat, utas_nev, foglalas_idopont, repules_datuma)
                self.foglalasok.append(uj_foglalas)
                print(f"Foglalás sikeres. Foglalás ára: {uj_foglalas.foglalas_ara()} Ft, Repülés dátuma: {repules_datuma}")
            except ValueError:
                print("Hiba: A dátum formátuma hibás. A helyes formátum: ÉÉÉÉ-HH-NN (pl.: 2024-12-15)")
        else:
            print("Nincs ilyen járat a rendszerben.")
        # print("[DEBUG] Jegy foglalása vége.")

    def foglalas_lemondasa(self, utas_nev):
        # print(f"[DEBUG] Foglalás lemondása - Utas név: {utas_nev}")
        for foglalas in self.foglalasok:
            if foglalas.utas_nev == utas_nev:
                self.foglalasok.remove(foglalas)
                print("Foglalás sikeresen lemondva.")
                # print("[DEBUG] Foglalás sikeresen lemondva.")
                return
        print("Nem található ilyen nevű foglalás.")
        # print("[DEBUG] Foglalás lemondása vége.")

    def foglalasok_listazasa(self):
        # print("[DEBUG] Foglalások listázása...")
        if not self.foglalasok:
            print("Nincs aktív foglalás.")
        for foglalas in self.foglalasok:
            print(f"Utas: {foglalas.utas_nev}, Járat: {foglalas.jarat.jarat_info()}, Foglalás időpontja: {foglalas.idopont}, Repülés dátuma: {foglalas.repules_datuma}")
        # print("[DEBUG] Foglalások listázása vége.")

    def jarat_keresese(self, jaratszam):
        # print(f"[DEBUG] Járat keresése - Járatszám: {jaratszam}")
        for jarat in self.legi_tarsasag.jaratok:
            if jarat.jaratszam == jaratszam:
                # print(f"[DEBUG] Járat megtalálva: {jarat.jaratszam}")
                return jarat
        # print("[DEBUG] Járat nem található.")
        return None

# Futtatható rész
if __name__ == "__main__":
    # print("[DEBUG] Repülőjegy Foglalási Rendszer indítása...")
    rendszer = FoglalasiRendszer()
    while True:
        print("\n--- Repülőjegy Foglalási Rendszer ---")
        print("1. Jegy foglalása")
        print("2. Foglalás lemondása")
        print("3. Foglalások listázása")
        print("4. Elérhető járatok listázása")
        print("5. Kilépés")
        valasztas = input("Választás: ")

        if valasztas == "1":
            rendszer.legi_tarsasag.listaz_jaratok()
            jaratszam = input("Járatszám: ")
            utas_nev = input("Utazó neve: ")
            repules_datuma = input("Repülés dátuma (formátum: ÉÉÉÉ-HH-NN, pl.: 2024-12-15): ")
            # print("[DEBUG] Jegy foglalása indítása...")
            rendszer.jegy_foglalasa(jaratszam, utas_nev, repules_datuma)
        elif valasztas == "2":
            utas_nev = input("Utazó neve: ")
            # print("[DEBUG] Foglalás lemondása indítása...")
            rendszer.foglalas_lemondasa(utas_nev)
        elif valasztas == "3":
            # print("[DEBUG] Foglalások listázása indítása...")
            rendszer.foglalasok_listazasa()
        elif valasztas == "4":
            # print("[DEBUG] Elérhető járatok listázása indítása...")
            rendszer.legi_tarsasag.listaz_jaratok()
        elif valasztas == "5":
            print("Kilépés...")
            # print("[DEBUG] Program kilépés...")
            break
        else:
            print("Érvénytelen választás.")
            # print("[DEBUG] Érvénytelen választás történt.")
