from rich import print
from rich.traceback import install
install()

class Jogador():
    """
    Representa um jogador base no sistema de RPG tático em turnos.

    Esta classe serve como classe mãe (superclasse) para as especializações
    de combate (como Guerreiro, Assassino e Mago), gerenciando os atributos
    vitais, inventário e ações fundamentais do personagem.

    Attributes:
        Nome (str): Nome do personagem escolhido pelo jogador.
        Nivel (float/int): Nível atual de progressão do personagem. Padrão é 1.
        Vida (float): Pontos de vida atuais/máximos do personagem. Padrão é 100.
        Dano (float): Valor base de dano físico ou mágico. Padrão é 10.
        Defesa (float): Redução de dano contra ataques recebidos. Padrão é 10.
        Vigor (float): Energia disponível para ações especiais. Padrão é 100.
        Inventario (list): Lista de itens e materiais coletados ou craftados.
    """
    
    def __init__(self, Nome, Nivel=1, MaxVida=100, MaxVigor=10, Dano=10, Defesa=10, Inventario=None):
        self.Nome = Nome
        self.Nivel = Nivel
        self.Vida = MaxVida
        self.MaxVida = MaxVida
        self.Vigor = MaxVigor   
        self.MaxVigor = MaxVigor
        self.Dano = Dano
        self.Defesa = Defesa
        self.Defendendo = False
        self.Inventario = Inventario if Inventario is not None else []
    
    def __str__(self):
        conteudo = f"Player: {self.Nome}"   
        conteudo += f"\nNivel: {self.Nivel}"
        conteudo += f"\nVida: {self.Vida}"
        conteudo += f"\nVigor: {self.Vigor}"
        conteudo += f"\nDano: {self.Dano}"
        conteudo += f"\nDefesa: {self.Defesa}"
        
        conteudo += f"\nInventário: {self.Inventario}"
        return conteudo

    def atacar(self, alvo):
        if not alvo:
            return f"Antes de atacar escolha um inimigo válido"
        
    def ataque_especial(self, alvo):
        if not alvo:
            return f"Antes de atacar escolha um inimigo válido"
    
    def defender(self):
        """
        Coloca o jogador em postura defensiva, aumentando a proteção no turno.
        """
        self.Defendendo = True
        return f"{self.Nome} assumiu postura defensiva! Sua defesa está ativa neste turno."
    
    def sofrer_dano(self, dano):
        if not self.esta_vivo():
            return f"O player:{self.Nome} já está derrotado"
        
        if dano < 0:
            return f"O dano sofrido não pode ser negativo"
            
        self.Vida -= dano
        return f"{self.Nome} sofreu {dano} de dano"
        
    def equipar_item(self, item):
        pass
    
    def desequipar_item(self, slot):
        pass
    
    def craftar_item(self, material=[]):
        pass
    
    def esta_vivo(self):
        return self.Vida > 0

p1 = Jogador("Rafael", 1, 100, 100, 10, 10, None)
print(p1)