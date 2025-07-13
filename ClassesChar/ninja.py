from heroi import Heroi


class Ninja(Heroi):
    """
    Arquetipo: Ninja
      - Vida: 80
      - Mana: 100
      - Habilidade especial: ataqueSombrio()
      - Bônus: chance de esquiva passiva
    """
    MAX_VIDA: int = 80
    MAX_MANA: int = 100
    CUSTO_ATAQUE_SOMBRIO: int = 30
    DANO_ATAQUE_SOMBRIO: int = 55
    CHANCE_ESQUIVA: float = 0.2  # 20% de chance de evitar um ataque inimigo

    def __init__(self, nome: str, idade: int):
        """
        Cria um Ninja com vida e mana padrão do arquetipo.

        Parâmetros:
            nome: nome do ninja
            idade: idade em anos
        """
        super().__init__(nome, idade, vida=Ninja.MAX_VIDA, mana=Ninja.MAX_MANA)
        # Kit inicial de itens
        self.addItem("Poção de Vida", 1)
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

        Parâmetros:
            alvo: instância de Personagem a receber o dano
        """
        if self.mana < Ninja.CUSTO_ATAQUE_SOMBRIO:
            print(f"{self.nome} não tem mana suficiente ({self.mana}/{Ninja.CUSTO_ATAQUE_SOMBRIO}) para Ataque Sombrio.")
            return

        self.mana -= Ninja.CUSTO_ATAQUE_SOMBRIO
        alvo.receberDano(Ninja.DANO_ATAQUE_SOMBRIO)

        print(
            f"{self.nome} realizou Ataque Sombrio em {alvo.nome}, causando {Ninja.DANO_ATAQUE_SOMBRIO} de dano!"
        )
        print(f"Mana restante: {self.mana}/{Ninja.MAX_MANA}")


    def tentarEsquivar(self):
        """
        Retorna True se o ninja conseguir esquivar de um ataque.
        """
        from random import random
        return random() < Ninja.CHANCE_ESQUIVA


    def receberDano(self, dano: int) -> int:
        """
        Recebe dano, mas pode tentar esquivar.

        Parâmetros:
            dano: valor bruto de dano recebido

        Retorna:
            vida atualizada
        """
        if self.tentarEsquivar():
            print(f"{self.nome} esquivou do ataque e não recebeu dano!")
        else:
            self.vida = max(self.vida - dano, 0)
            print(f"{self.nome} foi atingido e perdeu {dano} de vida. Vida atual: {self.vida}")
        return self.vida


    def ataqueEspecial(self, alvo) -> None:
        """
        Chama o ataque sombrio como especial.

        Parâmetros:
            alvo: instância de Personagem a receber o dano
        """
        self.ataqueSombrio(alvo)
