from personagem import Personagem 

class Heroi(Personagem):
    """
    Representa as características de um herói no jogo.
    Herda da classe Personagem.
    """
    def __init__(self, nome, idade, vida, maldade):
        super().__init__(nome, idade, vida)
        niveis_validos = ['Baixa', 'Média', 'Alta']
        if maldade not in niveis_validos:
            raise ValueError(f"Nível de maldade inválido! Escolha entre {niveis_validos}")
        self.maldade = maldade

    def ataque(self, personagem):
        """
        Reduz a vida de outro personagem atacado pelo vilão.
        """
        print(f'{self.nome} atacou {personagem.nome}!')
        personagem.downgrade_vida()

    def __str__(self):
        return f'Herói: {self.nome}, Idade: {self.idade}, Vida: {self.vida}, Maldade: {self.maldade}'
