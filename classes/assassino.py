from player import Player

from rich import print
from rich.traceback import install

install()

class Assasino(Player):
    def __init__(self, Nome, Nivel=1, MaxVida=110, MaxVigor=8, Defesa=8):
        super().__init__(Nome, Nivel, MaxVida, MaxVigor, Defesa)
    
    def atacar(self, alvo):
        print(f"O jogador {self.Nome} chegou na espreita e atacou o inimigo!")
        return alvo.sofrer_dano(12.5)
    