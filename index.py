# tehdään alussa importit

from logger import logger
from summa import summa
from erotus import erotus

logger("aloitetaan") #muutos

x = int(input("luku1: "))
y = int(input("luku 2: "))
print(f"{summa(x, y)}")
print(f"{erotus(x, y)}")

logger("lopetetaan")
