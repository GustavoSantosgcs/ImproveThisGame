from heroi import Heroi

class Guerreiro(Heroi):
    """
    Arquetipo: Guerreiro
      - Vida: 130
      - Mana: 60
      - Habilidade especial: marretadaBruta()
      - Bônus de defesa: reduz 10% do dano recebido
    """
    MAX_VIDA: int = 130
    MAX_MANA: int = 60
    CUSTO_MARRETADA: int = 15
    DANO_MARRETADA: int = 45
    BONUS_DEFESA: float = 0.15  # 15% de redução


    def __init__(self, nome: str, idade: int):
        """
        Cria um Guerreiro com vida alta e mana baixa.

        Parâmetros:
            nome: nome do guerreiro
            idade: idade em anos
        """
        super().__init__(nome, idade, vida=Guerreiro.MAX_VIDA, mana=Guerreiro.MAX_MANA)
        # Kit inicial de itens
        self.addItem("Poção de Vida", 3)
        self.addItem("Poção de Mana", 1)
        

    def descricao(self):
        """
        Descrição do Guerreiro, incluindo kit inicial de itens.
        """
        pocao_vida = self.inventario.get("Poção de Vida", 0)
        pocao_mana = self.inventario.get("Poção de Mana", 0)
        return (
            "Guerreiro: tanque resistente com bônus de defesa.\n"
            f"Vida: {self.vida}/{Guerreiro.MAX_VIDA} | Mana: {self.mana}/{Guerreiro.MAX_MANA}\n"
            f"Bônus de defesa: {int(Guerreiro.BONUS_DEFESA*100)}%\n"
            f"Itens iniciais: Poção de Vida x{pocao_vida}, Poção de Mana x{pocao_mana}\n"
            "Ataque especial: Marretada Bruta (dano 45, custo 15 de mana)."
        )


    def marretadaBruta(self, alvo):
        """
        Executa golpe forte:
         - consome CUSTO_MARRETADA de mana
         - causa DANO_MARRETADA de dano

        Parâmetros:
            alvo: instância de Personagem a receber o dano
        """
        if self.mana < Guerreiro.CUSTO_MARRETADA:
            print(
                f"{self.nome} não tem mana suficiente "
                f"({self.mana}/{Guerreiro.CUSTO_MARRETADA}) para Marretada Bruta."
            )
            return

        self.mana -= Guerreiro.CUSTO_MARRETADA
        alvo.receberDano(Guerreiro.DANO_MARRETADA)
        print(
            f"{self.nome} desferiu Marretada Bruta em {alvo.nome}, "
            f"causando {Guerreiro.DANO_MARRETADA} de dano!"
        )
        print(f"Mana restante: {self.mana}/{Guerreiro.MAX_MANA}")


    def receberDano(self, dano: int):
        """
        Recebe dano aplicando o bônus de defesa.

        Parâmetros:
            dano: valor bruto de dano recebido

        Retorna:
            vida atualizada
        """
        dano_reduzido: int = int(dano * (1 - Guerreiro.BONUS_DEFESA))
        self.vida = max(self.vida - dano_reduzido, 0)
        print(
            f"{self.nome} recebeu {dano_reduzido} de dano após defesa "
            f"({Guerreiro.BONUS_DEFESA * 100:.0f}%). Vida atual: {self.vida}"
        )
        return self.vida

    def ataqueEspecial(self, alvo):
        """
        Chama o ataque especial do guerreiro (marretadaBruta).

        Parâmetros:
            alvo: instância de Personagem a receber o dano
        """
        self.marretadaBruta(alvo)
