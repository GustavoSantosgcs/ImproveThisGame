from heroi import Heroi
from itens import PocaoVida, PocaoMana
from utils import Utils

class Guerreiro(Heroi):
    """
    Arquetipo: Guerreiro
      - Vida: 130
      - Mana: 60
      - Habilidade especial: marretadaBruta()
      - Bônus de defesa: reduz 15% do dano recebido
    """
    MAX_VIDA = 130
    MAX_MANA = 60
    CUSTO_MARRETADA = 15
    DANO_MARRETADA = 45
    BONUS_DEFESA = 0.15  # 15% de redução


    def __init__(self, nome: str, idade: int):
        """
        Cria um Guerreiro com vida alta e mana baixa.
        """
        super().__init__(nome, idade, vida=Guerreiro.MAX_VIDA, mana=Guerreiro.MAX_MANA)

        # Kit inicial de itens
        self.addItem("Poção de Vida", 3)
        self.addItem("Poção de Mana", 1)


    def descricao(self):
        """
        Descrição do Guerreiro, incluindo kit inicial de itens.
        """
        pocao_vida = self.inventario.get("Poção de Vida", 0)
        pocao_mana = self.inventario.get("Poção de Mana", 0)
        return (
            "Guerreiro: tanque resistente com bônus de defesa.\\n"
            f"Vida: {self.vida}/{Guerreiro.MAX_VIDA} | Mana: {self.mana}/{Guerreiro.MAX_MANA}\\n"
            f"Itens iniciais: Poção de Vida x{pocao_vida}, Poção de Mana x{pocao_mana}\\n"
            "Ataque especial: Marretada Bruta (dano 45, custo 15 de mana)."
        )


    def marretadaBruta(self, alvo):
        """
        Executa golpe forte:
         - consome CUSTO_MARRETADA de mana
         - causa DANO_MARRETADA de dano
        """
        console = Utils.console
        if self.mana < Guerreiro.CUSTO_MARRETADA:
            console.print(
                f"[red]{self.nome} não tem mana suficiente ({self.mana}/{Guerreiro.CUSTO_MARRETADA})![/red]"
            )
            return

        self.mana -= Guerreiro.CUSTO_MARRETADA
        dano = Guerreiro.DANO_MARRETADA
        alvo.receberDano(dano)

        console.print(
            f"[yellow]{self.nome} desferiu Marretada Bruta em {alvo.nome}, causando {dano} de dano![/yellow]"
        )
        console.print(f"Mana restante: {self.mana}/{Guerreiro.MAX_MANA}")


    def receberDano(self, dano: int):
        """
        Recebe dano aplicando o bônus de defesa.
        """
        console = Utils.console
        dano_reduzido = int(dano * (1 - Guerreiro.BONUS_DEFESA))
        self.vida = max(self.vida - dano_reduzido, 0)
        console.print(
            f"[red]{self.nome} recebeu {dano_reduzido} de dano após defesa ({int(Guerreiro.BONUS_DEFESA*100)}%)[/red]"
        )
        return self.vida


    def ataqueEspecial(self, alvo):
        """
        Override do Heroi: executa marretadaBruta.
        """
        self.marretadaBruta(alvo)


    def __str__(self):
        base = super().__str__()
        return base + f" | Defesa bônus: {int(Guerreiro.BONUS_DEFESA*100)}%"
