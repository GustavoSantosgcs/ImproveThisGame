from personagem import Personagem


class Vilao(Personagem):
    """
    Representa um vilão do jogo, com atributos de ataque e defesa
    e nível de maldade que afeta o dano causado.

    Níveis de maldade:
      - Baixa: multiplicador 0.8
      - Média: multiplicador 1.0
      - Alta : multiplicador 1.2
    """

    _MALDADE_MOD = {
        'Baixa': 0.8,
        'Média': 1.0,
        'Alta': 1.2
    }

    def __init__(
        self,
        nome: str,
        idade: int,
        vida: int,
        maldade: str,
        ataque: int = 30,
        defesa: int = 10
    ):
        """
        Inicializa um vilão com vida, maldade, ataque e defesa.
        """
        super().__init__(nome, idade, vida)

        if maldade not in Vilao._MALDADE_MOD:
            níveis = list(Vilao._MALDADE_MOD.keys())
            raise ValueError(f"Nível de maldade inválido! Escolha entre {níveis}")

        self.maldade = maldade
        self.ataque = ataque
        self.defesa = defesa
        self._mod = Vilao._MALDADE_MOD[maldade]


    def ataqueBasico(self, alvo):
        """
        Desferir um ataque básico:
         - dano = ataque * multiplicador de maldade
        """
        dano = int(self.ataque * self._mod)
        print(f"{self.nome} atacou {alvo.nome} com força básica, causando {dano} de dano!")
        alvo.receber_dano(dano)


    def ataqueDevastador(self, alvo):
        """
        Habilidade especial 'Ataque Devastador':
         - dano = ataque * multiplicador * 1.5
        """
        dano = int(self.ataque * self._mod * 1.5)
        print(f"\n{self.nome} usou Super Ataque Devastador em {alvo.nome}, causando {dano} de dano!")
        alvo.receber_dano(dano)


    def receberAtaque(self, dano: int):
        """
        Aplica dano considerando a defesa do vilão.
        """
        dano_liquido = max(dano - self.defesa, 0)
        self.vida = max(self.vida - dano_liquido, 0)
        print(
            f"{self.nome} recebeu {dano_liquido} de dano "
            f"após defesa ({self.defesa}). Vida atual: {self.vida}"
        )


    def __str__(self):
        return (
            f"Vilão: {self.nome} (Maldade: {self.maldade}), "
            f"Vida: {self.vida}, Ataque: {self.ataque}, Defesa: {self.defesa}"
        )
