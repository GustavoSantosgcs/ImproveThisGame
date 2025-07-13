from utils import Utils

class Item:
    """
    Representa um item genérico que pode ser usado por heróis.
    """
    def __init__(self, nome: str, descricao: str):
        self.nome = nome
        self.descricao = descricao


    def usar(self, heroi):
        """
        Aplica o efeito do item no herói.
        Deve ser sobrescrito nas subclasses.
        """
        raise NotImplementedError(f"{self.__class__.__name__} não implementou usar()")


    def __str__(self) -> str:
        return f"{self.nome}: {self.descricao}"


class PocaoVida(Item):
    """
    Poção que restaura vida do herói.
    """
    def __init__(self, cura: int = 20):
        super().__init__("Poção de Vida", f"Restaura {cura} pontos de vida.")
        self.cura = cura


    def usar(self, heroi):
        heroi.usarPocaoVida(self.cura)
        return True


class PocaoMana(Item):
    """
    Poção que restaura mana do herói.
    """
    def __init__(self, recarga: int = 50):
        super().__init__("Poção de Mana", f"Restaura {recarga} pontos de mana.")
        self.recarga = recarga


    def usar(self, heroi):
        heroi.usarPocaoMana(self.recarga)
        return True


class Voucher(Item):
    """
    Voucher concedido ao salvar um refém.
    """
    def __init__(self):
        super().__init__("Voucher de Resgate", "Pode ser trocado por recompensas especiais.")


    def usar(self, heroi):
        Utils.console.print(
            f"[green]{heroi.nome} usou {self.nome}! Nada acontece além da comemoração.[/green]"
        )
        return True
