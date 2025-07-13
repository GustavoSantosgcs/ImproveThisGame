import os
import json
from heroi import Heroi
from vilao import Vilao
from ClassesChar.mago      import Mago
from ClassesChar.arqueiro  import Arqueiro
from ClassesChar.ninja     import Ninja
from ClassesChar.guerreiro import Guerreiro

# Diretório e arquivos de repositório
DIR = 'repositorio'
ARQUIVO_HEROIS = os.path.join(DIR, 'herois.json')
ARQUIVO_VILOES = os.path.join(DIR, 'viloes.json')

# Garante que o diretório exista
os.makedirs(DIR, exist_ok=True)

# Mapeia o nome da classe no JSON para a classe Python
CLASS_MAP = {
    "Mago":      Mago,
    "Arqueiro":  Arqueiro,
    "Ninja":     Ninja,
    "Guerreiro": Guerreiro
}

def carregarHerois() -> list[Heroi]:
    """
    Carrega a lista de heróis do JSON, instanciando a subclasse correta.
    """
    try:
        with open(ARQUIVO_HEROIS, encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        return []

    herois: list[Heroi] = []
    for entry in data:
        cls_name = entry.get("classe", "")
        cls = CLASS_MAP.get(cls_name, Heroi)
        heroi = cls.fromDict(entry)
        herois.append(heroi)
    return herois


def salvarHerois(herois: list[Heroi]) -> None:
    """
    Salva a lista de heróis no JSON.
    """
    to_save = [h.toDict() for h in herois]
    with open(ARQUIVO_HEROIS, "w", encoding="utf-8") as f:
        json.dump(to_save, f, ensure_ascii=False, indent=2)


def carregarViloes() -> list[Vilao]:
    """
    Carrega a lista de vilões do JSON.
    """
    if not os.path.exists(ARQUIVO_VILOES):
        return []
    with open(ARQUIVO_VILOES, "r", encoding="utf-8") as f:
        data = json.load(f)
    return [Vilao.fromDict(entry) for entry in data]


def salvarViloes(viloes: list[Vilao]) -> None:
    """
    Salva a lista de vilões em JSON.
    """
    to_save = [v.toDict() for v in viloes]
    with open(ARQUIVO_VILOES, "w", encoding="utf-8") as f:
        json.dump(to_save, f, ensure_ascii=False, indent=2)
