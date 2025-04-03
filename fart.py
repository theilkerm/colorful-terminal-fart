import time
import random
from enum import Enum
import argparse

class Color(Enum):
    BLACK           = 30
    RED             = 31
    GREEN           = 32
    YELLOW          = 33
    BLUE            = 34
    MAGENTA         = 35
    CYAN            = 36
    WHITE           = 37
    RESET           = 39

    def __str__(self):
        return f"\033[{self.value}m"

parser = argparse.ArgumentParser(
        prog="colorful-terminal-fart",
        description="just watch the chars",
        epilog="https://github.com/theilkerm/colorful-terminal-fart - CC0"
        )

parser.add_argument('-i', '--interactive', help="get the text interactively (default)",
        action='store_true')
parser.add_argument('-t', '--text', help="text to be written")
parser.add_argument('-c', '--count', help="loop count (default 1000)", type=int, default=1000)

args = parser.parse_args()

if args.text is None:
    metin = input("Yazılacak metni girin: ")
else:
    metin = args.text

def type_text(text, spc="", slp=0.1):
    for char in text:
        # Rastgele bir renk seç
        color = random.choice([
            Color.RED, Color.GREEN, Color.YELLOW, Color.BLUE,
            Color.MAGENTA, Color.CYAN, Color.WHITE
        ])
        print(str(color) + char, end=spc, flush=True)
        time.sleep(slp)
    print(Color.RESET)

for i in range(args.count):
    spc = i * " "
    slp = 0.1 / (i + 1)
    type_text(metin, spc, slp)
    time.sleep(0.1)
