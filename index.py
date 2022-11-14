# tehdään alussa importit

from logger import logger
from summa import summa
from erotus import erotus

logger("aloitetaan")

x = int(input("luku1: "))
y = int(input("luku 2: "))
print(f"Lukujen summa on {summa(x, y)}")
print(f"Lukujen erotus on {erotus(x, y)}")

logger("lopetetaan ohjelma")
print("goodbye!") #tämä on kommentti
