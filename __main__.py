from enums import Stat

from rich import print
from rich.panel import Panel
from rich.traceback import install

from player import Player
from classes.assassino import Assassino
from classes.guerreiro import Guerreiro
from classes.mago import Mago
install()

CLASSES_DISPONIVEIS = {
    "1": (Guerreiro),
    "2": (Mago),
    "3": (Assassino),
}

def escolher_classe():
    print("\nEscolha sua classe:")
    for opcao, classe in CLASSES_DISPONIVEIS.items():
        print(f"  {opcao} - {classe.__name__}")
    while True:
        escolha = input("> ").strip()
        if escolha in CLASSES_DISPONIVEIS:
            return CLASSES_DISPONIVEIS[escolha]()
        print("Opção inválida! Tente novamente.")

def main():
    #nome = input("Nome do personagem: ").strip() or "Herói"
    
    #p1 = Player(nome, escolher_classe())
    p1 = Player("Tuneco", CLASSES_DISPONIVEIS["2"]())
    print(Panel(str(p1), title="Ficha do Personagem", expand=False))
    
if __name__ == "__main__":
    main()