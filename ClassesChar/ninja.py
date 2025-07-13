from heroi import Heroi
from itens import PocaoVida, PocaoMana
from utils import Utils
from random import random

class Ninja(Heroi):
    """
    Arquetipo: Ninja
      - Vida: 80
      - Mana: 100
      - Habilidade especial: ataqueSombrio()
      - Bônus: chance de esquiva passiva
    """
    MAX_VIDA = 80
    MAX_MANA = 100
    CUSTO_ATAQUE_SOMBRIO = 30
    DANO_ATAQUE_SOMBRIO = 55
    CHANCE_ESQUIVA = 0.2  # 20% de chance de evitar um ataque inimigo

    def __init__(self, nome: str, idade: int):
        """
        Cria um Ninja com vida e mana padrão do arquetipo.
        """
        super().__init__(nome, idade, vida=Ninja.MAX_VIDA, mana=Ninja.MAX_MANA)
        # Kit inicial de itens
        self.addItem("Poção de Vida", 3)
        self.addItem("Poção de Mana", 2)


    def descricao(self):
        """
        Descrição do Ninja, incluindo kit inicial de itens.
        """
        pocao_vida = self.inventario.get("Poção de Vida", 0)
        pocao_mana = self.inventario.get("Poção de Mana", 0)
        return (
            "Ninja: arquetipo furtivo com alta chance de esquiva.\n"
            f"Vida: {self.vida}/{Ninja.MAX_VIDA} | Mana: {self.mana}/{Ninja.MAX_MANA}\n"
            f"Chance de esquiva: {int(Ninja.CHANCE_ESQUIVA * 100)}%\n"
            f"Itens iniciais: Poção de Vida x{pocao_vida}, Poção de Mana x{pocao_mana}\n"
            "Ataque especial: Ataque Sombrio (dano 55, custo 30 de mana)."
        )

    def ataqueSombrio(self, alvo):
        """
        Executa um ataque sombrio:
         - consome CUSTO_ATAQUE_SOMBRIO de mana
         - causa DANO_ATAQUE_SOMBRIO de dano
        """
        console = Utils.console
        if self.mana < Ninja.CUSTO_ATAQUE_SOMBRIO:
            console.print(
                f"[red]{self.nome} não tem mana suficiente ({self.mana}/{Ninja.CUSTO_ATAQUE_SOMBRIO})![/red]"
            )
            return

        self.mana -= Ninja.CUSTO_ATAQUE_SOMBRIO
        dano = Ninja.DANO_ATAQUE_SOMBRIO
        alvo.receberDano(dano)

        console.print(
            f"[magenta]{self.nome} realizou Ataque Sombrio em {alvo.nome}, causando {dano} de dano![/magenta]"
        )
        console.print(f"Mana restante: {self.mana}/{Ninja.MAX_MANA}")


    def tentarEsquivar(self):
        """
        Retorna True se o ninja conseguir esquivar de um ataque.
        """
        return random() < Ninja.CHANCE_ESQUIVA


    def receberDano(self, dano: int):
        """
        Recebe dano, mas pode tentar esquivar.
        """
        console = Utils.console
        if self.tentarEsquivar():
            console.print(f"[cyan]{self.nome} esquivou do ataque![/cyan]")
        else:
            self.vida = max(self.vida - dano, 0)
            console.print(f"[red]{self.nome} recebeu {dano} de dano. Vida atual: {self.vida}[/red]")
        return self.vida


    def ataqueEspecial(self, alvo):
        """
        Override do Heroi: executa ataqueSombrio.
        """
        self.ataqueSombrio(alvo)

