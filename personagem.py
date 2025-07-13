class Personagem:
    """
    Representa um personagem genérico no jogo, com atributos de vida,
    ataque e defesa, e métodos para curar e receber dano.
    """

    DEFAULT_ATAQUE: int = 12
    DEFAULT_DEFESA: int = 6


    def __init__(
        self,
        nome: str,
        idade: int,
        vida: int
    ):
        """
        Inicializa o personagem.

        Parâmetros:
            nome: nome do personagem
            idade: idade 
            vida: pontos de vida iniciais
        """
        self.nome: str = nome
        self.idade: int = idade
        self.vida: int = vida
        self.ataque: int = Personagem.DEFAULT_ATAQUE
        self.defesa: int = Personagem.DEFAULT_DEFESA


    def curar(self, quantidade: int = 10):
        """
        Restaura pontos de vida.

        Parâmetros:
            quantidade: pontos de vida a restaurar

        Retorna:
            vida atualizada
        """
        self.vida += quantidade
        print(f"{self.nome} recuperou {quantidade} de vida. Vida atual: {self.vida}")
        return self.vida


    def receberDano(self, dano: int) :
        """
        Aplica dano líquido descontando a defesa, sem permitir vida negativa.

        Parâmetros:
            dano: valor bruto de dano recebido

        Retorna:
            vida atualizada
        """
        dano_liquido: int = max(dano - self.defesa, 0)
        self.vida = max(self.vida - dano_liquido, 0)
        print(
            f"{self.nome} recebeu {dano_liquido} de dano "
            f"(defesa: {self.defesa}). Vida atual: {self.vida}"
        )
        return self.vida


    def alterarNome(self, novo_nome: str):
        """
        Atualiza o nome do personagem.

        Parâmetros:
            novo_nome: novo nome para o personagem
        """
        self.nome = novo_nome
        print(f"Nome atualizado para {self.nome}")


    def __str__(self) :
        return (
            f"{self.__class__.__name__}: {self.nome} | "
            f"Idade: {self.idade} | Vida: {self.vida} | "
            f"Ataque: {self.ataque} | Defesa: {self.defesa}"
        )
