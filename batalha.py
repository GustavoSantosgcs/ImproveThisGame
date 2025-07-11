import time
import random
from heroi import Heroi
from vilao import Vilao
from utils import Utils as ut


class Batalha:
    """
    Gerencia o loop de batalha entre um herói e um vilão.
    """
    def __init__(self, heroi: Heroi, vilao: Vilao):
        self.heroi = heroi
        self.vilao = vilao


    def iniciar_batalha(self):
        """
        Loop principal de batalha:
        - Herói escolhe ação (básico, especial, poções)
        - Vilão ataca (básico ou sinistro)
        Continua até vida de um atingir zero.
        """
        ut.limparTela()
        print("\n=== BATALHA INICIADA ===")
        turno = 1

        while self.heroi.vida > 0 and self.vilao.vida > 0:
            print(f"\n--- Turno {turno} ---")
            print(self.heroi)
            print(self.vilao)

            # Ações do herói
            print("\nAções disponíveis:")
            print("1) Ataque básico")
            print("2) Ataque especial")
            print("3) Poção de vida")
            print("4) Poção de mana")
            escolha = input("> ").strip()

            match escolha:
                case "1":
                    self.heroi.ataqueBasico(self.vilao)
                    
                case "2":
                    self.heroi.ataqueEspecial(self.vilao)
                    
                case "3":
                    self.heroi.usarPocaoVida()
                    
                case "4":
                    self.heroi.usarPocaoMana()
                    
                case _:
                    print("Opção inválida! Você perdeu a vez...")

            time.sleep(1)

            # Verifica derrota do vilão
            if self.vilao.vida <= 0:
                print(f"\n{self.vilao.nome} foi derrotado! 🎉")
                break

            # Ação do vilão
            print(f"\nVez de {self.vilao.nome} atacar!")
            if random.random() < 0.3:
                self.vilao.ataque_sinistro(self.heroi)
            else:
                self.vilao.ataque_basico(self.heroi)

            time.sleep(1)

            # Verifica derrota do herói
            if self.heroi.vida <= 0:
                print(f"\n{self.heroi.nome} foi derrotado... 😢")
                break

            turno += 1
            input("Pressione enter para novo turno")
            ut.limparTela()

        print("\n=== BATALHA ENCERRADA ===")
