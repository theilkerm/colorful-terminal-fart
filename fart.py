import time
import random
from colorama import Fore, init

init()
metin = input("Yazılacak metni girin: ")

def type_text(text, spc="", slp=0.1):
    for char in text:
        # Rastgele bir renk seç
        color = random.choice([
            Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE,
            Fore.MAGENTA, Fore.CYAN, Fore.WHITE
        ])
        print(color + char, end=spc, flush=True)
        time.sleep(slp)
    print(Fore.RESET)

for i in range(1000):
    spc = i * " "
    slp = 0.1 / (i + 1)
    type_text(metin, spc, slp)
    time.sleep(0.1)
