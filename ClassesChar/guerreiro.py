from heroi import Heroi


class Guerreiro(Heroi):
    """
    Arquetipo: Guerreiro
      - Vida: 120
      - Mana: 50
      - Habilidade especial: MarretadaBruta()
      - Bônus de defesa: reduz 10% do dano recebido
    """

    MAX_VIDA = 120
    MAX_MANA = 50
    CUSTO_MARRETADA = 15
    DANO_MARRETADA = 45
    BONUS_DEFESA = 0.1  # 10% de redução


    def __init__(self, nome: str, idade: int):
        """
        Cria um Guerreiro com vida alta e mana baixa.
        """
        super().__init__(nome, idade, vida=Guerreiro.MAX_VIDA, mana=Guerreiro.MAX_MANA)


    def marretadaBruta(self, alvo):
        """
        Golpe forte:
         - consome CUSTO_MARRETADA de mana
         - causa DANO_MARRETADA de dano
        """
        if self.mana < Guerreiro.CUSTO_MARRETADA:
            print(f"{self.nome} não tem mana suficiente ({self.mana}/{Guerreiro.CUSTO_MARRETADA}) para Golpe Forte.")
            return

        self.mana -= Guerreiro.CUSTO_MARRETADA
        alvo.vida = max(alvo.vida - Guerreiro.DANO_MARRETADA, 0)
        print(f"{self.nome} desferiu Golpe Forte em {alvo.nome}, causando {Guerreiro.DANO_MARRETADA} de dano!")
        print(f"Mana restante: {self.mana}/{Guerreiro.MAX_MANA}")


    def receberAtaque(self, dano: int):
        """
        Recebe dano aplicando o bônus de defesa.
        """
        dano_reduzido = int(dano * (1 - Guerreiro.BONUS_DEFESA))
        self.vida = max(self.vida - dano_reduzido, 0)
        print(f"{self.nome} recebeu {dano_reduzido} de dano após defesa. Vida atual: {self.vida}")

   
    def ataqueEspecial(self, alvo):
        return self.marretadaBruta(alvo)