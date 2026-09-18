from abc import ABC, abstractmethod

class Classe(ABC):
    """
    Representa uma classe de combate no sistema de RPG tático em turnos.

    A Classe guarda os atributos de combate (Vida, Mana, Vigor, Defesa) e
    define o comportamento de ataque do personagem. O Player "possui" uma
    Classe (composição) e repassa as ações de combate para ela.

    Attributes:
        Vida (float): Pontos de vida atuais do personagem.
        MaxVida (float): Pontos de vida máximos.
        Vigor (float): Energia atual para habilidades físicas.
        MaxVigor (float): Vigor máximo.
        Mana (float): Energia atual para habilidades mágicas.
        MaxMana (float): Mana máxima.
        Defesa (float): Redução de dano recebido.
        Defendendo (bool): True se estiver em postura defensiva neste turno.
    """

    NOME = "Classe Base"

    def __init__(self, max_vida=100, max_vigor=10, max_mana=50, defesa=10):
        self.Vida = max_vida
        self.MaxVida = max_vida
        self.Vigor = max_vigor
        self.MaxVigor = max_vigor
        self.Mana = max_mana
        self.MaxMana = max_mana
        self.Defesa = defesa
        self.Defendendo = False

    def __str__(self):
        return (
            f"Classe: {self.NOME}\n"
            f"  Vida: {self.Vida:.0f}/{self.MaxVida:.0f}\n"
            f"  Mana: {self.Mana:.0f}/{self.MaxMana:.0f}\n"
            f"  Vigor: {self.Vigor:.0f}/{self.MaxVigor:.0f}\n"
            f"  Defesa: {self.Defesa:.0f}"
        )

    @abstractmethod
    def atacar(self, alvo, **atributos):
        """
        Ataque básico da classe.

        Args:
            alvo: Objeto com método sofrer_dano(dano).
            **atributos: Bônus derivados dos Status do Player
                         (ex: forca=5, inteligencia=3, destreza=2).
        """
        pass

    @abstractmethod
    def ataque_especial(self, alvo, **atributos):
        """
        Ataque especial da classe. Consome Mana ou Vigor.

        Args:
            alvo: Objeto com método sofrer_dano(dano).
            **atributos: Bônus derivados dos Status do Player.
        """
        pass

    def defender(self):
        self.Defendendo = True
        return "Postura defensiva ativa neste turno (reduz o dano recebido)."

    def sofrer_dano(self, dano):
        if not self.esta_vivo():
            return "O personagem já está derrotado."

        if dano < 0:
            return "O dano sofrido não pode ser negativo."

        # Defendendo reduz mais dano; a postura só dura um turno
        reducao = self.Defesa * 0.5 if self.Defendendo else self.Defesa * 0.2
        dano_real = max(1.0, dano - reducao)
        self.Vida = max(0.0, self.Vida - dano_real)
        self.Defendendo = False

        if self.Vida <= 0:
            return f"Dano recebido: {dano_real:.1f}. O personagem foi derrotado!"
        return f"Dano recebido: {dano_real:.1f}. Vida restante: {self.Vida:.1f}"

    def esta_vivo(self):
        return self.Vida > 0
