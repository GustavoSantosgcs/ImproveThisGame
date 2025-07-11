from heroi import Heroi


class Mago(Heroi):
    """
    Arquetipo: Mago
      - Vida: 70
      - Mana: 150
      - Habilidade especial: bolaDeFogo()
    """

    # Valores máximos e parâmetros de spell
    MAX_VIDA = 70
    MAX_MANA = 150
    CUSTO_BOLA_DE_FOGO = 30
    DANO_BOLA_DE_FOGO = 50


    def __init__(self, nome: str, idade: int):
        """
        Cria um Mago com vida e mana padrão definidos por arquetipo.
        """
        super().__init__(nome, idade, vida=Mago.MAX_VIDA, mana=Mago.MAX_MANA)


    def bolaDeFogo(self, alvo):
        """
        Lança uma bola de fogo no alvo (alvo):
         - consome CUSTO_BOLA_DE_FOGO de mana
         - causa DANO_BOLA_DE_FOGO de dano
        """
        if self.mana < Mago.CUSTO_BOLA_DE_FOGO:
            print(f"{self.nome} não tem mana suficiente ({self.mana}/{Mago.CUSTO_BOLA_DE_FOGO}) para Bola de Fogo.")
            return

        # Aplica efeito
        self.mana -= Mago.CUSTO_BOLA_DE_FOGO
        alvo.vida = max(alvo.vida - Mago.DANO_BOLA_DE_FOGO, 0)

        print(f"{self.nome} lançou Bola de Fogo em {alvo.nome} causando {Mago.DANO_BOLA_DE_FOGO} de dano!")
        print(f"Mana restante: {self.mana}/{Mago.MAX_MANA}")


    def ataqueEspecial(self, alvo):
        return self.bolaDeFogo(alvo)