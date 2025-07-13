from personagem import Personagem

class Vilao(Personagem):
    """
    Representa um vilão do jogo,
    com atributos de vida, ataque, defesa e nível de maldade.

    Parâmetros:
        nome: nome do vilão
        idade: idade em anos
        vida: pontos de vida iniciais
        maldade: nível de maldade ('Baixa', 'Média', 'Alta')
        ataque: poder de ataque base (inteiro)
        defesa: poder de defesa base (inteiro)
    """
    _MALDADE_MOD: dict[str, float] = {
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
        ataque: int = 25,
        defesa: int = 10
    ):
        super().__init__(nome, idade, vida)
        maldade = maldade.title()
        if maldade not in Vilao._MALDADE_MOD:
            niveis = list(Vilao._MALDADE_MOD.keys())
            raise ValueError(f"Nível de maldade inválido! Escolha entre {niveis}")
        self.maldade: str = maldade
        self.ataque: int = ataque
        self.defesa: int = defesa
        self._mod: float = Vilao._MALDADE_MOD[self.maldade]


    def ataqueBasico(self, alvo):
        """
        Desferir um ataque básico.

        Parâmetros:
            alvo: instância de Personagem que receberá o dano
        """
        dano: int = int(self.ataque * self._mod)
        print(f"{self.nome} atacou {alvo.nome} com força básica, causando {dano} de dano!")
        alvo.receberDano(dano)


    def ataqueDevastador(self, alvo):
        """
        Habilidade especial: ataque devastador.

        Parâmetros:
            alvo: instância de Personagem que receberá o dano
        """
        dano: int = int(self.ataque * self._mod * 1.5)
        print(
            f"{self.nome} executou Ataque Devastador em {alvo.nome}, "
            f"causando {dano} de dano!"
        )
        alvo.receberDano(dano)


    def dialogar(self, fala: str):
        """
        Permite ao vilão falar algo no meio da aventura.

        Parâmetros:
            fala: texto que o vilão irá dizer
        """
        print(f'{self.nome} diz: "{fala}"')


    def __str__(self):
        return (
            f"Vilão: {self.nome} | Maldade: {self.maldade} | "
            f"Vida: {self.vida} | Ataque: {self.ataque} | Defesa: {self.defesa}"
        )
