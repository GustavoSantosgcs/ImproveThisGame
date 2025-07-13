from heroi import Heroi


class Arqueiro(Heroi):
    """
    Arqueiro:
      - Vida: 85
      - Mana: 110
      - Flechas: 10
      - Habilidade especial: flechadaDeFogo()
    """
    DEFAULT_VIDA: int = 85
    DEFAULT_MANA: int = 110
    CUSTO_MANA_FLECHADA: int = 20
    DANO_FLECHADA: int = 45


    def __init__(self, nome: str, idade: int):
        """
        Cria um Arqueiro com valores padrão.

        Parâmetros:
            nome: nome do arqueiro
            idade: idade em anos
        """
        super().__init__(nome, idade, vida=Arqueiro.DEFAULT_VIDA, mana=Arqueiro.DEFAULT_MANA)
        self.flechas: int = 10
        # Kit inicial de itens
        self.addItem("Poção de Vida", 2)
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

        Parâmetros:
            alvo: instância de Personagem a receber o dano
        """
        faltou: list[str] = []
        if self.mana < Arqueiro.CUSTO_MANA_FLECHADA:
            faltou.append("mana")
        if self.flechas < 1:
            faltou.append("flechas")

        if faltou:
            print(f"{self.nome} não tem recursos suficientes ({' e '.join(faltou)}) para atacar.")
            return

        self.mana -= Arqueiro.CUSTO_MANA_FLECHADA
        self.flechas -= 1
        alvo.receberDano(Arqueiro.DANO_FLECHADA)

        print(f"{self.nome} lançou flechadaDeFogo em {alvo.nome}, causando {Arqueiro.DANO_FLECHADA} de dano!")
        print(f"Mana restante: {self.mana} | Flechas restantes: {self.flechas}")


    def ataqueEspecial(self, alvo):
        """
        Executa o ataque especial do arqueiro (flechadaDeFogo).

        Parâmetros:
            alvo: instância de Personagem a receber o dano
        """
        self.flechadaDeFogo(alvo)
