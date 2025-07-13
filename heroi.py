from personagem import Personagem
from itens import Item, PocaoVida, PocaoMana, Voucher
from utils import Utils


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
        self.mana = mana
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
        Executa ataque básico contra o alvo.

        Parâmetros:
            alvo: instância de Personagem que receberá o dano
        """
        Utils.console.print(f"[green]{self.nome} atacou {alvo.nome}! (básico)[/green]")
        alvo.receberDano(self.ataque)


    def ataqueEspecial(self, alvo):
        """
        Chama o ataque especial da subclasse ou, se não existir,
        faz um ataque básico.
        """
        Utils.console.print(
            f"[yellow]{self.nome} não possui ataque especial! Usando básico[/yellow]"
        )
        self.ataqueBasico(alvo)


    def usarPocaoVida(self, cura: int = 30):
        """
        Usa uma poção de vida, sem ultrapassar o máximo.

        Parâmetros:
            cura: pontos de vida restaurados (padrão 30)
        """
        if self.vida < Heroi.MAX_VIDA:
            self.vida = min(self.vida + cura, Heroi.MAX_VIDA)
            Utils.console.print(
                f"[blue]{self.nome} usou poção de vida! Vida: {self.vida}, Mana: {self.mana}[/blue]"
            )
        else:
            Utils.console.print("[red]Vida já está cheia![/red]")


    def usarPocaoMana(self, recarga: int = 30):
        """
        Usa uma poção de mana, sem ultrapassar o máximo.

        Parâmetros:
            recarga: pontos de mana restaurados (padrão 30)
        """
        if self.mana < Heroi.MAX_MANA:
            self.mana = min(self.mana + recarga, Heroi.MAX_MANA)
            Utils.console.print(
                f"[blue]{self.nome} usou poção de mana! Vida: {self.vida}, Mana: {self.mana}[/blue]"
            )
        else:
            Utils.console.print("[red]Mana já está cheia![/red]")


    def addItem(self, item, qtd: int = 1):
        """
        Alias compatível com subclasses antigas.
        item pode ser instância de Item ou nome de item.
        qtd: quantidade a adicionar.
        """
        from itens import PocaoVida, PocaoMana, Voucher
        # resolve instância
        if isinstance(item, str):
            mapping = {
                "Poção de Vida": PocaoVida,
                "Poção de Mana": PocaoMana,
                "Voucher": Voucher,
            }
            cls = mapping.get(item)
            if not cls:
                return
            item_obj = cls()
        else:
            item_obj = item

        for _ in range(qtd):
            self.inventario[item_obj.nome] = self.inventario.get(item_obj.nome, 0) + 1
        Utils.console.print(f"[green]{self.nome} recebeu {qtd}x {item_obj.nome}[/green]")


    def usarItem(self, nome_item: str):
        """
        Usa uma unidade do item, aplicando seu efeito.
        """
        qtd = self.inventario.get(nome_item, 0)
        if qtd < 1:
            Utils.console.print(f"[red]{self.nome} não tem {nome_item}[/red]")
            return

        if nome_item == "Poção de Vida":
            item = PocaoVida()
        elif nome_item == "Poção de Mana":
            item = PocaoMana()
        else:
            Utils.console.print("[red]Item desconhecido.[/red]")
            return

        item.usar(self)
        self.inventario[nome_item] -= 1
        if self.inventario[nome_item] == 0:
            del self.inventario[nome_item]
        Utils.console.print(
            f"[yellow]{self.nome} agora tem {self.inventario.get(nome_item,0)}x {nome_item}[/yellow]"
        )


    def salvarRefem(self, nome_refem: str):
        """
        Simula salvar um refém e concede um voucher.

        Parâmetros:
            nome_refem: nome do refém resgatado
        """
        Utils.console.print(
            f"[green]{self.nome} salvou o refém {nome_refem}![/green]"
        )
        voucher = Voucher()
        self.addItem(voucher)


    def dialogar(self, fala: str):
        """
        Exibe uma fala do herói com efeito de máquina de escrever.
        """
        texto = f"{self.nome} diz: “{fala}”"
        Utils.escrever(texto)
        self.historico.append(f"{self.nome} disse: {fala}")


    def toDict(self):
        """
        Serializa o herói para um dicionário JSON,
        incluindo a classe (Mago, Ninja, etc.).
        """
        base = {
            "nome": self.nome,
            "classe": self.__class__.__name__,   
            "idade": self.idade,
            "vida": self.vida,
            "mana": self.mana,
            "ataque": self.ataque,
            "defesa": self.defesa,
            "inventario": self.inventario,
            "historico": self.historico,
        }
        return base


    @classmethod
    def fromDict(cls, data: dict) -> "Heroi":
        """
        Desserializa um dicionário em instância de Heroi ou de sua subclasse.
        """
        nome = data["nome"]
        idade = data["idade"]
        # Se for exatamente Heroi, passe vida+mana no construtor
        if cls is Heroi:
            heroi = cls(
                nome=nome,
                idade=idade,
                vida=data.get("vida", Heroi.MAX_VIDA),
                mana=data.get("mana", Heroi.MAX_MANA)
            )
        else:
            # Subclasse recebe só nome+idade no __init__
            heroi = cls(nome, idade)
            heroi.vida = data.get("vida", heroi.vida)
            heroi.mana = data.get("mana", heroi.mana)

        # Atributos comuns
        heroi.ataque = data.get("ataque", getattr(heroi, "ataque", 0))
        heroi.defesa = data.get("defesa", getattr(heroi, "defesa", 0))
        heroi.inventario = data.get("inventario", {})
        heroi.historico = data.get("historico", [])
        return heroi


    def __str__(self):
        return (
            f"Herói: {self.nome} | Idade: {self.idade} | "
            f"Vida: {self.vida}/{Heroi.MAX_VIDA} | Mana: {self.mana}/{Heroi.MAX_MANA} | "
            f"Itens: {self.inventario}"
        )
