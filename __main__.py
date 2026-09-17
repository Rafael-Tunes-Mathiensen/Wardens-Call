from rich import print
from rich.traceback import install
from rich.panel import Panel
from rich.table import Table

from player import Player

install()

p1 = Player("Rafael", 1, 100, 100, 10)
print(p1)