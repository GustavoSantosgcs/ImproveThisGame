from heroi import Heroi
from utils import Utils

class Arqueiro(Heroi):
    """
    Arqueiro:
      - Vida: 85
      - Mana: 110
      - Flechas: 10
      - Habilidade especial: flechadaDeFogo()
    """
    DEFAULT_VIDA = 85
    DEFAULT_MANA = 110
    CUSTO_MANA_FLECHADA = 20
    DANO_FLECHADA = 45


    def __init__(self, nome: str, idade: int):
        """
        Cria um Arqueiro com valores padrão.
        """
        super().__init__(nome, idade, vida=Arqueiro.DEFAULT_VIDA, mana=Arqueiro.DEFAULT_MANA)
        self.flechas = 10

        # Kit inicial de itens
        self.addItem("Poção de Vida", 3)
        self.addItem("Poção de Mana", 1)


    def descricao(self):
        """
        Descrição do Arqueiro, incluindo kit inicial de itens.
        """
        pocao_vida = self.inventario.get("Poção de Vida", 0)
        pocao_mana = self.inventario.get("Poção de Mana", 0)
        return (
            "Arqueiro: equilíbrio entre mobilidade e dano à distância.\n"
            f"Vida: {self.vida}/{Arqueiro.DEFAULT_VIDA} | Mana: {self.mana}/{Arqueiro.DEFAULT_MANA}\n"
            f"Flechas: {self.flechas}\n"
            f"Itens iniciais: Poção de Vida x{pocao_vida}, Poção de Mana x{pocao_mana}\n"
            "Ataque especial: Flechada de Fogo (dano 45, custo 20 de mana e 1 flecha)."
        )


    def flechadaDeFogo(self, alvo):
        """
        Dispara uma flecha no alvo:
         - consome 1 flecha
         - consome CUSTO_MANA_FLECHADA de mana
         - causa DANO_FLECHADA de dano
        """
        console = Utils.console
        faltou = []
        if self.mana < Arqueiro.CUSTO_MANA_FLECHADA:
            faltou.append("mana")
        if self.flechas < 1:
            faltou.append("flechas")

        if faltou:
            console.print(f"[red]{self.nome} não tem recursos ({' e '.join(faltou)})![/red]")
            return

        self.mana -= Arqueiro.CUSTO_MANA_FLECHADA
        self.flechas -= 1
        dano = Arqueiro.DANO_FLECHADA
        alvo.receberDano(dano)

        console.print(
            f"[magenta]{self.nome} lançou Flechada de Fogo em {alvo.nome}, causando {dano} de dano![/magenta]"
        )
        console.print(f"Mana restante: {self.mana} | Flechas restantes: {self.flechas}")


    def ataqueEspecial(self, alvo):
        """
        Override do Heroi: executa flechadaDeFogo.
        """
        self.flechadaDeFogo(alvo)


    def __str__(self):
        base = super().__str__()
        return base + f" | Flechas: {self.flechas}"