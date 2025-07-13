from heroi import Heroi
from utils import Utils

class Mago(Heroi):
    """
    Arquetipo: Mago
      - Menos vida, mais mana
      - Habilidade especial: bolaDeFogo()
    """
    MAX_VIDA = 80
    MAX_MANA = 140
    CUSTO_BOLA_DE_FOGO = 25
    DANO_BOLA_DE_FOGO = 45


    def __init__(self, nome: str, idade: int):
        """
        Cria um Mago com valores padrão.
        """
        super().__init__(nome, idade, vida=Mago.MAX_VIDA, mana=Mago.MAX_MANA)
        # Kit inicial de itens
        self.addItem("Poção de Vida", 2)
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
        """
        console = Utils.console
        if self.mana < Mago.CUSTO_BOLA_DE_FOGO:
            console.print(
                f"[red]{self.nome} não tem mana suficiente ({self.mana}/{Mago.CUSTO_BOLA_DE_FOGO})![/red]"
            )
            return

        self.mana -= Mago.CUSTO_BOLA_DE_FOGO
        dano = Mago.DANO_BOLA_DE_FOGO
        alvo.receberDano(dano)

        console.print(
            f"[magenta]{self.nome} lançou Bola de Fogo em {alvo.nome}, causando {dano} de dano![/magenta]"
        )
        console.print(f"Mana restante: {self.mana}/{Mago.MAX_MANA}")


    def ataqueEspecial(self, alvo):
        """
        Override do Heroi: executa bolaDeFogo.
        """
        self.bolaDeFogo(alvo)