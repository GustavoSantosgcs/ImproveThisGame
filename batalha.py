import time
import random
from heroi import Heroi
from vilao import Vilao
from utils import Utils as ut

class Batalha:
    """
    Gerencia o loop de batalha entre um herói e um vilão,
    mantendo registro de todas as ações em um histórico.

    Parâmetros:
        heroi: instância de Heroi
        vilao: instância de Vilao

    Retorna:
        iniciarBatalha: True se o herói vencer, False caso contrário
    """
    def __init__(self, heroi: Heroi, vilao: Vilao):
        self.heroi = heroi
        self.vilao = vilao
        self.historico: list[str] = []


    def iniciarBatalha(self):
        """
        Loop principal de batalha:
        - Herói escolhe ação (básico, especial ou itens)
        - Vilão ataca (básico ou devastador)
        Continua até vida de um atingir zero.

        Retorna:
            True se o herói sobreviveu, False caso contrário
        """
        ut.limparTela()
        print("\n=== BATALHA INICIADA ===")
        self.historico.append(f"Batalha iniciada: {self.heroi.nome} vs {self.vilao.nome}")
        turno = 1

        while self.heroi.vida > 0 and self.vilao.vida > 0:
            print(f"\n--- Turno {turno} ---")
            print(self.heroi)
            print(self.vilao)
            print("\nAções disponíveis:")
            print("1) Ataque básico")
            print("2) Ataque especial")
            print("3) Usar item")
            escolha = input("> ").strip()

            match escolha:
                case "1":
                    self.heroi.ataqueBasico(self.vilao)
                    self.historico.append(
                        f"{self.heroi.nome} usou ataque básico em {self.vilao.nome}. Vida do vilão: {self.vilao.vida}"
                    )
                case "2":
                    self.heroi.ataqueEspecial(self.vilao)
                    self.historico.append(
                        f"{self.heroi.nome} usou ataque especial em {self.vilao.nome}. Vida do vilão: {self.vilao.vida}"
                    )
                case "3":
                    inv = self.heroi.inventario
                    if not inv:
                        print("Inventário vazio!")
                        self.historico.append(f"{self.heroi.nome} tentou usar item, mas inventário vazio.")
                    else:
                        print("Itens disponíveis:")
                        nomes = list(inv.keys())
                        for i, nome in enumerate(nomes, 1):
                            print(f"{i}) {nome} x{inv[nome]}")
                        escolha_item = input("Escolha o item: ").strip()
                        
                        if escolha_item.isdigit() and 1 <= int(escolha_item) <= len(nomes):
                            item_sel = nomes[int(escolha_item)-1]
                            self.heroi.usarItem(item_sel)
                            self.historico.append(
                                f"{self.heroi.nome} usou item {item_sel}."
                            )
                        else:
                            print("Escolha inválida.")
                            self.historico.append(
                                f"{self.heroi.nome} tentou ação inválida de item."
                            )
                case _:
                    print("Opção inválida! Você perdeu a vez...")
                    self.historico.append(
                        f"{self.heroi.nome} tentou ação inválida e perdeu o turno."
                    )

            time.sleep(1)

            # Verifica derrota do vilão
            if self.vilao.vida <= 0:
                print(f"\n{self.vilao.nome} foi derrotado! 🎉")
                self.historico.append(f"{self.vilao.nome} foi derrotado no turno {turno}.")
                break

            # Ação do vilão
            print(f"\nVez de {self.vilao.nome} atacar!")
            if random.random() < 0.3:
                self.vilao.ataqueDevastador(self.heroi)
                self.historico.append(
                    f"{self.vilao.nome} usou ataque devastador em {self.heroi.nome}. Vida do herói: {self.heroi.vida}"
                )
            else:
                self.vilao.ataqueBasico(self.heroi)
                self.historico.append(
                    f"{self.vilao.nome} usou ataque básico em {self.heroi.nome}. Vida do herói: {self.heroi.vida}"
                )

            time.sleep(1)

            # Verifica derrota do herói
            if self.heroi.vida <= 0:
                print(f"\n{self.heroi.nome} foi derrotado... 😢")
                self.historico.append(f"{self.heroi.nome} foi derrotado no turno {turno}.")
                break

            turno += 1
            ut.pausar()
            ut.limparTela()

        # Anexa todo o histórico desta batalha ao herói
        try:
            self.heroi.historico.extend(self.historico)
        except AttributeError:
            pass

        print("\n=== BATALHA ENCERRADA ===")
        print("\n=== Histórico de Ações ===")
        for evento in self.historico:
            print(f"- {evento}")

        return self.heroi.vida > 0
