from rich import print
from rich.traceback import install

from classe import Classe as ClasseBase
from abc import ABC, abstractmethod
from enums import Stat

install()

class Player:
    """
    Representa um player base no sistema de RPG tático em turnos.

    O Player "possui" uma Classe (Mago, Guerreiro ou Assassino) via composição.
    Progressão (nível, XP, pontos de atributo) fica no Player; combate
    (vida, mana, vigor, ataques) fica na Classe — o Player apenas delega.

    Attributes:
        Inventario (list): Atributo de CLASSE — compartilhado entre
                           todos os Players instanciados.
    """

    Inventario = []

    def __init__(self, Nome: str, Classe: ClasseBase):
        self.Nome = Nome
        self.Classe = Classe
        self.Nivel = 1
        self.Xp = 0
        self.XpMax = 100
        self.Status = {s: 0 for s in Stat}
        self.Skills = {}
        self.Points = 3

    def __str__(self):
        status_formatado = "\n  ".join([f"{stat.value}: {val}" for stat, val in self.Status.items()])

        conteudo = f"Player: {self.Nome} ({self.Classe.NOME})"
        conteudo += f"\nNível: {self.Nivel} | XP: {self.Xp}/{self.XpMax} | Pontos livres: {self.Points}"
        conteudo += f"\n{self.Classe}"
        conteudo += f"\nStatus:\n  {status_formatado}"
        conteudo += f"\nInventário compartilhado: {Player.Inventario}"
        return conteudo

    def atacar(self, alvo):
        return self.Classe.atacar(alvo, **self._bonus_de_status())

    def ataque_especial(self, alvo):
        return self.Classe.ataque_especial(alvo, **self._bonus_de_status())

    def defender(self):
        return self.Classe.defender()

    def sofrer_dano(self, dano):
        return self.Classe.sofrer_dano(dano)

    def esta_vivo(self):
        return self.Classe.esta_vivo()

    def _bonus_de_status(self):
        """
        Converte os Status do Player nos bônus que cada Classe usa:
        Guerreiro escala com FOR, Mago com INT, Assassino com DES.
        """
        return {
            "forca": self.Status[Stat.FOR],
            "inteligencia": self.Status[Stat.INT],
            "destreza": self.Status[Stat.DES],
        }

    def ganhar_xp(self, quantidade):
        self.Xp += quantidade
        resultado = f"{self.Nome} ganhou {quantidade} XP."
        while self.Xp >= self.XpMax:
            self.Xp -= self.XpMax
            resultado += " " + self.subir_nivel()
        return resultado

    def subir_nivel(self):
        self.Nivel += 1
        self.Points += 3
        self.XpMax = int(self.XpMax * 1.25)
        return f"{self.Nome} subiu para o nível {self.Nivel}!"

    def alocar_pontos(self, stat: Stat, QtdPontos: int = 1):
        if self.Points < QtdPontos:
            return "Você não tem pontos para aplicar!"

        if stat in self.Status:
            self.Points -= QtdPontos
            self.Status[stat] += QtdPontos
            print(f"{QtdPontos} Pontos alocados em: {stat.value}" if QtdPontos > 1 else f"1 Ponto alocado em: {stat.value}")
        else:
            print("Atributo inválido!")

    def adicionar_item(self, item):
        Player.Inventario.append(item)
        return f"{item} adicionado ao inventário compartilhado."

    def equipar_item(self, item):
        pass

    def desequipar_item(self, slot):
        pass

    def craftar_item(self, material=None):
        if material is None:
            material = []
        pass