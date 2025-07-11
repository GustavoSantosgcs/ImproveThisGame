from heroi import Heroi


class Ninja(Heroi):
    """
    Arquetipo: Ninja
      - Vida: 75
      - Mana: 100
      - Habilidade especial: ataque_sombrio()
      - Bônus: chance de esquiva passiva
    """

    MAX_VIDA = 75
    MAX_MANA = 100
    CUSTO_ATAQUE_SOMBRIO = 25
    DANO_ATAQUE_SOMBRIO = 60
    CHANCE_ESQUIVA = 0.2  # 20% de chance de evitar um ataque inimigo


    def __init__(self, nome: str, idade: int):
        """
        Cria um Ninja com vida e mana padrão do arquetipo.
        """
        super().__init__(nome, idade, vida=Ninja.MAX_VIDA, mana=Ninja.MAX_MANA)


    def ataqueSombrio(self, alvo):
        """
        Executa um ataque sombrio:
         - consome CUSTO_ATAQUE_SOMBRIO de mana
         - causa DANO_ATAQUE_SOMBRIO de dano
        """
        if self.mana < Ninja.CUSTO_ATAQUE_SOMBRIO:
            print(f"{self.nome} não tem mana suficiente ({self.mana}/{Ninja.CUSTO_ATAQUE_SOMBRIO}) para Ataque Sombrio.")
            return

        self.mana -= Ninja.CUSTO_ATAQUE_SOMBRIO
        alvo.vida = max(alvo.vida - Ninja.DANO_ATAQUE_SOMBRIO, 0)

        print(f"{self.nome} realizou Ataque Sombrio em {alvo.nome}, causando {Ninja.DANO_ATAQUE_SOMBRIO} de dano!")
        print(f"Mana restante: {self.mana}/{Ninja.MAX_MANA}")


    def tentarEsquivar(self):
        """
        Retorna True se o ninja conseguir esquivar de um ataque.
        """
        from random import random
        return random() < Ninja.CHANCE_ESQUIVA


    def receberAtaque(self, dano: int):
        """
        Recebe dano, mas pode tentar esquivar.
        """
        if self.tentarEsquivar():
            print(f"{self.nome} esquivou do ataque e não recebeu dano!")
        else:
            self.vida = max(self.vida - dano, 0)
            print(f"{self.nome} foi atingido e perdeu {dano} de vida. Vida atual: {self.vida}")


    def ataqueEspecial(self, alvo):
        return self.ataqueSombrio(alvo)