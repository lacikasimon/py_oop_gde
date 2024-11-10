from abc import ABC, abstractmethod

# Járat (absztrakt osztály)
class Jarat(ABC):
    def __init__(self, jaratszam, celallomas, jegyar):
        self.jaratszam = jaratszam
        self.celallomas = celallomas
        self.jegyar = jegyar

    @abstractmethod
    def jarat_info(self):
        pass

# BelföldiJarat osztály
class BelfoldiJarat(Jarat):
    def jarat_info(self):
        return f"Belföldi Járat - Szám: {self.jaratszam}, Cél: {self.celallomas}, Ár: {self.jegyar}"

# NemzetkoziJarat osztály
class NemzetkoziJarat(Jarat):
    def jarat_info(self):
        return f"Nemzetközi Járat - Szám: {self.jaratszam}, Cél: {self.celallomas}, Ár: {self.jegyar}"
