from heroi import Heroi


class Mago(Heroi):
    """
    Arquetipo: Mago
      - Menos vida, mais mana
      - Habilidade especial: bolaDeFogo()
    """
    MAX_VIDA: int = 80
    MAX_MANA: int = 140
    CUSTO_BOLA_DE_FOGO: int = 25
    DANO_BOLA_DE_FOGO: int = 45


    def __init__(self, nome: str, idade: int):
        """
        Cria um Mago com valores padrão.

        Parâmetros:
            nome: nome do mago
            idade: idade em anos
        """
        super().__init__(nome, idade, vida=Mago.MAX_VIDA, mana=Mago.MAX_MANA)
        # Kit inicial de itens
        self.addItem("Poção de Vida", 1)
        self.addItem("Poção de Mana", 3)


    def descricao(self):
        """
        Descrição do Mago, incluindo kit inicial de itens.
        """
        pocao_vida = self.inventario.get("Poção de Vida", 0)
        pocao_mana = self.inventario.get("Poção de Mana", 0)
        return (
            "Mago: arquetipo com alta mana e feitiços poderosos.\n"
            f"Vida: {self.vida}/{Mago.MAX_VIDA} | Mana: {self.mana}/{Mago.MAX_MANA}\n"
            f"Itens iniciais: Poção de Vida x{pocao_vida}, Poção de Mana x{pocao_mana}\n"
            "Ataque especial: Bola de Fogo (dano 45, custo 25 de mana)."
        )

   
    def bolaDeFogo(self, alvo):
        """
        Lança uma bola de fogo no alvo:
        - consome CUSTO_BOLA_DE_FOGO de mana
        - causa DANO_BOLA_DE_FOGO de dano

        Parâmetros:
            alvo: instância de Personagem a receber o dano
        """
        if self.mana < Mago.CUSTO_BOLA_DE_FOGO:
            print(f"{self.nome} não tem mana suficiente ({self.mana}/{Mago.CUSTO_BOLA_DE_FOGO}) para Bola de Fogo.")
            return

        self.mana -= Mago.CUSTO_BOLA_DE_FOGO
        alvo.receberDano(Mago.DANO_BOLA_DE_FOGO)
        print(f"{self.nome} lançou Bola de Fogo em {alvo.nome}, causando {Mago.DANO_BOLA_DE_FOGO} de dano!")
        print(f"Mana restante: {self.mana}/{Mago.MAX_MANA}")


    def ataqueEspecial(self, alvo) -> None:
        """
        Chama o método especial do mago (bolaDeFogo).

        Parâmetros:
            alvo: instância de Personagem a receber o dano
        """
        self.bolaDeFogo(alvo)
