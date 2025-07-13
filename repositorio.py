import os
import json
from heroi import Heroi
from vilao import Vilao

# Diretório e arquivos de repositório
DIR = 'repositorio'
ARQUIVO_HEROIS = os.path.join(DIR, 'herois.json')
ARQUIVO_VILOES = os.path.join(DIR, 'viloes.json')

# Garante que o diretório exista
os.makedirs(DIR, exist_ok=True)


def salvarHerois(herois: list[Heroi]):
    """
    Salva a lista de heróis em JSON, incluindo inventário e histórico.

    Parâmetros:
        herois: lista de instâncias de Heroi
    """
    data = [h.toDict() for h in herois]
    with open(ARQUIVO_HEROIS, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def carregarHerois() -> list[Heroi]:
    """
    Carrega a lista de heróis do JSON.

    Retorna:
        Lista de instâncias de Heroi (pode ser vazia).
    """
    if not os.path.exists(ARQUIVO_HEROIS):
        return []
    with open(ARQUIVO_HEROIS, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return [Heroi.fromDict(item) for item in data]


def salvarViloes(viloes: list[Vilao]) -> None:
    """
    Salva a lista de vilões em JSON.

    Parâmetros:
        viloes: lista de instâncias de Vilao
    """
    data = [v.toDict() for v in viloes]
    with open(ARQUIVO_VILOES, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def carregarViloes() -> list[Vilao]:
    """
    Carrega a lista de vilões do JSON.

    Retorna:
        Lista de instâncias de Vilao (pode ser vazia).
    """
    if not os.path.exists(ARQUIVO_VILOES):
        return []
    with open(ARQUIVO_VILOES, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return [Vilao.fromDict(item) for item in data]
