from heroi import Heroi


class Arqueiro(Heroi):
    """
    Arqueiro:
      - Vida: 80
      - Mana: 100
      - Flechas: 10
      - Dano básico: herdado de Heroi
      - Habilidade especial: flechadaDeFogo()
    """

    def __init__(self, nome: str, idade: int):
        """
        Cria um Arqueiro com valores padrão.
        """
        super().__init__(nome, idade, vida=80, mana=100)

        # atributo exclusivo do arqueiro
        self.flechas = 10
        

    def flechadaDeFogo(self, alvo):
        """
        Dispara uma flecha no alvo:
         - consome 1 flecha
         - consome 20 de mana
         - causa 40 de dano
        """
        custo_mana = 20
        dano = 40

        faltou_recursos = []
        if self.mana < custo_mana:
            faltou_recursos.append("mana")
        if self.flechas < 1:
            faltou_recursos.append("flechas")

        if faltou_recursos:
            recursos = " e ".join(faltou_recursos)
            print(f"{self.nome} não tem recursos suficientes ({recursos}) para atacar.")
            return

        # aplica o ataque
        self.mana -= custo_mana
        self.flechas -= 1
        alvo.vida = max(alvo.vida - dano, 0)

        print(f"{self.nome} lançou uma flechada em {alvo.nome} causando {dano} de dano!")
        print(f"Mana restante: {self.mana} | Flechas restantes: {self.flechas}")


    def ataqueEspecial(self, alvo):
        return self.flechadaDeFogo(alvo)