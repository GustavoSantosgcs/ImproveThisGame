class Personagem:
    """
    Representa um personagem genérico no jogo, com atributos de vida,
    ataque e defesa, e métodos para curar e receber dano.
    """

    DEFAULT_ATAQUE = 10
    DEFAULT_DEFESA = 5


    def __init__(self, nome: str, idade: int, vida: int):
        """ Inicializa o personagem. """
        self.nome = nome
        self.idade = idade
        self.vida = vida
        self.ataque = Personagem.DEFAULT_ATAQUE
        self.defesa = Personagem.DEFAULT_DEFESA


    def curar(self, quantidade: int = 10):
        """
        Restaura 'quantidade' de pontos de vida.

        return: 
            vida atualizada
        """
        self.vida += quantidade
        print(f"{self.nome} recuperou {quantidade} de vida. Vida atual: {self.vida}")
        return self.vida


    def receberDano(self, dano: int):
        """
        Aplica dano líquido descontando a defesa, sem permitir vida negativa.

        return:
            vida atualizada
        """
        dano_liquido = max(dano - self.defesa, 0)
        self.vida = max(self.vida - dano_liquido, 0)
        print(f"{self.nome} recebeu {dano_liquido} de dano (defesa: {self.defesa}). Vida atual: {self.vida}")
        return self.vida


    def alterarNome(self, novo_nome: str):
        """
        Atualiza o nome do personagem.
        """
        self.nome = novo_nome
        print(f"Nome atualizado para {self.nome}")


    def __str__(self) -> str:
        return (
            f"{self.__class__.__name__}: {self.nome} | Idade: {self.idade} | "
            f"Vida: {self.vida} | Ataque: {self.ataque} | Defesa: {self.defesa}"
        )
