from classe import Classe

class Mago(Classe):
    """Dano mágico à distância: pouca vida e defesa, dano baseado em Inteligência."""

    NOME = "Mago"

    def __init__(self):
        super().__init__(max_vida=90, max_vigor=8, max_mana=12, defesa=6)

    def atacar(self, alvo, inteligencia=0, **kwargs):
        custo = 1
        if self.Mana < custo:
            return "Mana insuficiente para conjurar Bola de Fogo!"
        self.Mana -= custo
        dano = 10 + inteligencia * 1.2
        return alvo.sofrer_dano(dano)

    def ataque_especial(self, alvo, inteligencia=0, **kwargs):
        custo = 3
        if self.Mana < custo:
            return "Mana insuficiente para conjurar Bola de Fogo!"
        self.Mana -= custo
        dano = 35 + inteligencia * 2.0
        return f"BOLA DE FOGO! {alvo.sofrer_dano(dano)}"
