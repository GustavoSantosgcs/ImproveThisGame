from personagem import Personagem
from itens import Item, PocaoVida, PocaoMana, Voucher


class Heroi(Personagem):
    """
    Representa as características de um herói no jogo.
    Herda da classe Personagem.
    """
    MAX_VIDA: int = 120
    MAX_MANA: int = 120

    def __init__(self, nome: str, idade: int, vida: int, mana: int):
        """
        Inicializa o herói com atributos básicos e inventário.

        Parâmetros:
            nome: nome do herói
            idade: idade
            vida: pontos de vida iniciais
            mana: pontos de mana iniciais
        """
        super().__init__(nome, idade, vida)
        self.mana: int = mana
        self.inventario: dict[str, int] = {}
        self.historico: list[str] = []


    def descricao(self):
        """
        Retorna uma breve descrição desta classe de herói.
        Deve ser implementado em cada subclasse.
        """
        raise NotImplementedError(
            f"{self.__class__.__name__} precisa implementar descricao()"
        )
        
        
    def ataqueBasico(self, alvo):
        """
        Herói desferindo ataque básico utilizando seu atributo de ataque.

        Parâmetros:
            alvo: instância de Personagem a receber o dano
        """
        print(f"{self.nome} atacou {alvo.nome}! (básico)")
        alvo.receberDano(self.ataque)


    def ataqueEspecial(self, alvo):
        """
        Chama o ataque especial da subclasse, se existir.
        Caso contrário, faz um ataque básico.
        """
        print(f"{self.nome} não possui ataque especial! Usando ataque básico.")
        self.ataqueBasico(alvo)
        
        
    def usarPocaoVida(self, cura: int = 30):
        """Soma o parâmetro cura ao total de pontos de vida, sem ultrapassar MAX_VIDA."""
        if self.vida < Heroi.MAX_VIDA:
            self.vida = min(self.vida + cura, Heroi.MAX_VIDA)
            print(f"{self.nome} usou poção de vida! Vida: {self.vida}, Mana: {self.mana}")
        else:
            print("Vida já está cheia! Não é possível usar poção.")


    def usarPocaoMana(self, recarga: int = 30):
        """Soma o parâmetro recarga ao total de pontos de mana, sem ultrapassar MAX_MANA."""
        if self.mana < Heroi.MAX_MANA:
            self.mana = min(self.mana + recarga, Heroi.MAX_MANA)
            print(f"{self.nome} usou poção de mana! Vida: {self.vida}, Mana: {self.mana}")
        else:
            print("Mana já está cheia! Não é possível usar poção.")


    def adicionarItem(self, item: Item):
        """Acrescenta um item ao inventário (contagem)."""
        self.inventario[item.nome] = self.inventario.get(item.nome, 0) + 1
        print(f"{self.nome} recebeu 1x {item.nome}.")


    def usarItem(self, nome_item: str):
        """Usa uma unidade do item, se existir, aplicando seu efeito."""
        qtd = self.inventario.get(nome_item, 0)
        if qtd < 1:
            print(f"{self.nome} não tem {nome_item} no inventário.")
            return
        # criar instância temporária para chamar usar()
        if nome_item == "Poção de Vida":
            item = PocaoVida()
        elif nome_item == "Poção de Mana":
            item = PocaoMana()
        else:
            print("Item desconhecido.")
            return

        item.usar(self)
        self.inventario[nome_item] -= 1
        if self.inventario[nome_item] == 0:
            del self.inventario[nome_item]
        print(f"{self.nome} agora tem {self.inventario.get(nome_item,0)}x {nome_item}.")


    def salvarRefem(self, nome_refem: str):
        """
        Simula salvar um refém e concede um voucher ao herói.

        Parâmetros:
            nome_refem: nome do refém resgatado
        """
        print(f"{self.nome} salvou o refém {nome_refem}! Parabéns.")
        voucher = Voucher()
        self.adicionarItem(voucher)
        

    def dialogar(self, fala: str):
        """
        Permite ao herói falar algo no meio da aventura.

        Parâmetros:
            fala: texto que o herói vai dizer
        """
        print(f'{self.nome} diz: "{fala}"')


    def toDict(self) -> dict:
        """
        Serializa o herói para um dicionário pronto para JSON.
        """
        return {
            "nome": self.nome,
            "idade": self.idade,
            "vida": self.vida,
            "mana": self.mana,
            "ataque": self.ataque,
            "defesa": self.defesa,
            "inventario": self.inventario,
            "historico": self.historico,
        }


    @classmethod
    def fromDict(cls, data: dict) -> "Heroi":
        """
        Desserializa um dicionário em uma instância de Heroi.
        """
        heroi = cls(
            nome=data["nome"],
            idade=data["idade"],
            vida=data["vida"],
            mana=data["mana"],
        )
        heroi.ataque = data.get("ataque", heroi.ataque)
        heroi.defesa = data.get("defesa", heroi.defesa)
        heroi.inventario = data.get("inventario", {})
        heroi.historico = data.get("historico", [])
        return heroi


    def __str__(self):
        return (
            f"Herói: {self.nome} | Idade: {self.idade} | "
            f"Vida: {self.vida}/{Heroi.MAX_VIDA} | Mana: {self.mana}/{Heroi.MAX_MANA} | "
            f"Itens: {self.inventario}"
        )
