from classe import Classe

class Guerreiro(Classe):
    """Tanque corpo a corpo: muita vida e defesa, dano baseado em Força."""

    NOME = "Guerreiro"

    def __init__(self):
        super().__init__(max_vida=150, max_vigor=12, max_mana=10, defesa=15)

    def atacar(self, alvo, forca=0, **kwargs):
        dano = 15 + forca * 1.5
        return alvo.sofrer_dano(dano)

    def ataque_especial(self, alvo, forca=0, **kwargs):
        custo = 5
        if self.Vigor < custo:
            return "Vigor insuficiente para usar Golpe Esmagador!"
        self.Vigor -= custo
        dano = 30 + forca * 2.0
        return f"GOLPE ESMAGADOR! {alvo.sofrer_dano(dano)}"
