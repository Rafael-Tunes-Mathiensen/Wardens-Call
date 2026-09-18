from classe import Classe

class Assassino(Classe):
    """Dano físico rápido: muito vigor, dano baseado em Destreza."""

    NOME = "Assassino"

    def __init__(self):
        super().__init__(max_vida=110, max_vigor=14, max_mana=20, defesa=8)

    def atacar(self, alvo, destreza=0, **kwargs):
        dano = 12 + destreza * 1.5
        return alvo.sofrer_dano(dano)

    def ataque_especial(self, alvo, destreza=0, **kwargs):
        custo = 6
        if self.Vigor < custo:
            return "Vigor insuficiente para usar Golpe Sombrio!"
        self.Vigor -= custo
        dano = 22 + destreza * 2.5
        return f"GOLPE SOMBRIO atacando pelas sombras! {alvo.sofrer_dano(dano)}"
