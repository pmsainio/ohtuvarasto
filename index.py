# tehdään alussa importit

from logger import logger
from summa import summa
from erotus import erotus

logger("aloitetaan") #muutos

x = int(input("luku1: "))
y = int(input("luku 2: "))
print(f"Lukujen summa on {x}+{y}={summa(x, y)}")
print(f"Lukujen erotus on {x}-{y}={erotus(x, y)}")

logger("lopetetaan ohjelma")
print("goodbye!") #tämä on kommentti
