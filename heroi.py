from personagem import Personagem


class Heroi(Personagem):
    """
    Representa as características de um herói no jogo.
    Herda da classe Personagem.
    """
    MAX_VIDA = 100
    MAX_MANA = 120


    def __init__(self, nome: str, idade: int, vida: int, mana: int):
        super().__init__(nome, idade, vida)
        self.mana = mana


    def ataqueBasico(self, alvo):
        """
        Herói desferindo ataque básico utilizando seu atributo de ataque.
        """
        print(f"{self.nome} atacou {alvo.nome}! (básico)")
        alvo.receber_dano(self.ataque)


    def ataqueEspecial(self, alvo):
        """
        Deve ser sobrescrito por cada subclasse de Heroi
        para chamar seu método especial (ex.: bola_de_fogo, ataque_com_flecha etc).
        """
        raise NotImplementedError(
            f"{self.__class__.__name__} não implementou ataque_especial()"
        )


    def usarPocaoVida(self, cura: int = 20):
        """Soma o parâmetro cura(int) ao total de pontos de vida, sem ultrapassar MAX_VIDA."""
        if self.vida < Heroi.MAX_VIDA:
            self.vida = min(self.vida + cura, Heroi.MAX_VIDA)
            print(f"{self.nome} usou poção de vida! Vida: {self.vida}, Mana: {self.mana}")
        else:
            print("Vida já está cheia! Não é possível usar poção.")


    def usarPocaoMana(self, recarga: int = 30):
        """Soma o parâmetro recarga(int) ao total de pontos de mana, sem ultrapassar MAX_MANA."""
        if self.mana < Heroi.MAX_MANA:
            self.mana = min(self.mana + recarga, Heroi.MAX_MANA)
            print(f"{self.nome} usou poção de mana! Vida: {self.vida}, Mana: {self.mana}")
        else:
            print("Mana já está cheia! Não é possível usar poção.")


    def __str__(self):
        return (
            f"Herói: {self.nome} | Idade: {self.idade} | "
            f"Vida: {self.vida}/{Heroi.MAX_VIDA} | Mana: {self.mana}/{Heroi.MAX_MANA}"
        )
