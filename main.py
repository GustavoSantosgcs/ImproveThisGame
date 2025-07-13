from ClassesChar.mago      import Mago
from ClassesChar.arqueiro  import Arqueiro
from ClassesChar.ninja     import Ninja
from ClassesChar.guerreiro import Guerreiro
from vilao                 import Vilao
from batalha               import Batalha
from utils                 import Utils as ut
from heroi                 import Heroi
from itens                 import PocaoVida, PocaoMana
from repositorio           import (
    salvarHerois,
    carregarHerois,
    salvarViloes,
    carregarViloes
)


class Jogo:
    """
    Gerencia cadastro, seleção, exclusão e batalha de heróis e vilões,
    suportando modos PvE e História.
    """
    def __init__(self):
        # carregar repositórios
        self.herois: list[Heroi] = carregarHerois()
        self.viloes: list[Vilao] = carregarViloes()
        self.heroi: Heroi | None = None
        self.vilao: Vilao | None = None
        # vilões padrão para PvE e História
        self.viloes_modo_hist = [ #nome, idade, vida, maldade,ataque,defesa
            Vilao("Goblin", 30, 80, "Média", 15, 5), 
            Vilao("Dragão", 300, 170, "Alta", 30, 12)
        ]


    def menuInicial(self):
        ut.limparTela()
        print("=== MENU PRINCIPAL ===")
        print("1) Criar Herói")
        print("2) Selecionar Herói")
        print("3) Excluir Herói")
        print("4) Listar Heróis e Vilões")
        print("5) Criar Vilão")
        print("6) Iniciar Batalha")
        print("7) Ver Inventário e Histórico")
        print("0) Sair")
        return ut.naoVazio("Escolha uma opção: ")


    def criarHeroi(self):
        ut.limparTela()
        print("=== CRIAR HERÓI ===")
        nome  = ut.naoVazio("Nome: ")
        idade = ut.lerInteiro("Idade: ")

        while True:
            ut.limparTela()
            print("Classes:")
            print("1 - Mago")
            print("2 - Arqueiro")
            print("3 - Ninja")
            print("4 - Guerreiro")
            escolha = ut.naoVazio("escolha: ")
            if   escolha == "1": heroi = Mago(nome, idade)
            elif escolha == "2": heroi = Arqueiro(nome, idade)
            elif escolha == "3": heroi = Ninja(nome, idade)
            elif escolha == "4": heroi = Guerreiro(nome, idade)
            else:
                print("Opção inválida.")
                ut.pausar()
                continue

            # mostra descrição e confirma
            ut.limparTela()
            print(heroi.descricao())
            conf = ut.naoVazio("Manter esta classe? (S/N): ").strip().lower()
            if conf == "s":
                break

        self.herois.append(heroi)
        salvarHerois(self.herois)
        print(f"Herói '{heroi.nome}' cadastrado.")
        ut.pausar()


    def selecionarHeroi(self):
        ut.limparTela()
        print("=== SELECIONAR HERÓI ===")
        if not self.herois:
            print("\nNenhum herói disponível.")
            ut.pausar()
            return
        for i, h in enumerate(self.herois, 1):
            print(f"{i}) {h.nome}")
        escolha = ut.lerInteiro("Número do herói: ")
        if 1 <= escolha <= len(self.herois):
            self.heroi = self.herois[escolha - 1]
            print(f"\nHerói selecionado: {self.heroi.nome}")
        else:
            print("Seleção inválida.")
        ut.pausar()


    def excluirHeroi(self):
        ut.limparTela()
        print("=== EXCLUIR HERÓI ===")
        if not self.herois:
            print("\nNenhum herói cadastrado.")
            ut.pausar()
            return
        for i, h in enumerate(self.herois, 1):
            print(f"{i}) {h.nome}")
        escolha = ut.lerInteiro("Número do herói para excluir: ")
        if 1 <= escolha <= len(self.herois):
            removido = self.herois.pop(escolha - 1)
            if self.heroi == removido:
                self.heroi = None
            salvarHerois(self.herois)
            print(f"\nHerói '{removido.nome}' excluído com sucesso.")
        else:
            print("Seleção inválida.")
        ut.pausar()


    def listarTodos(self):
        """
        Exibe todos os heróis e vilões cadastrados, incluindo suas classes.
        """
        ut.limparTela()
        print("=== HERÓIS ===")
        if not self.herois:
            print("\n(nenhum)")
        else:
            for h in self.herois:
                classe = h.__class__.__name__
                print(
                    f"- {h.nome} ({classe}): "
                    f"Vida {h.vida}/{h.MAX_VIDA}, Mana {h.mana}/{h.MAX_MANA}"
                )

        print("\n=== VILÕES ===")
        todos = self.viloes_modo_hist + self.viloes
        if not todos:
            print("\n(nenhum)")
        else:
            for v in todos:
                classe_v = v.__class__.__name__
                print(
                    f"- {v.nome} ({classe_v}): "
                    f"Maldade {v.maldade}, Vida {v.vida}"
                )
        ut.pausar()


    def criarVilao(self):
        """
        Cria um vilão personalizado, solicitando todos os atributos.
        """
        ut.limparTela()
        print("=== CRIAR VILÃO ===")
        nome    = ut.naoVazio("Nome: ")
        idade   = ut.lerInteiro("Idade: ")
        vida    = ut.lerInteiro("Vida: ")

        while True:
            maldade = ut.naoVazio("Maldade (Baixa/Média/Alta): ").title()
            if maldade in ("Baixa", "Média", "Alta"):
                break
            print("🔴 Nível de maldade inválido! Escolha entre Baixa, Média ou Alta.")
            ut.pausar()

        ataque = ut.lerInteiro("Ataque: ")
        defesa = ut.lerInteiro("Defesa: ")

        vilao = Vilao(nome, idade, vida, maldade, ataque, defesa)
        self.viloes.append(vilao)
        salvarViloes(self.viloes)

        classe_v = vilao.__class__.__name__
        print(f"✅ Vilão '{vilao.nome}' ({classe_v}) cadastrado com sucesso!")
        ut.pausar()


    def menuBatalha(self):
        ut.limparTela()
        print("=== MODO DE BATALHA ===")
        print("1) PvE")
        print("2) História")
        print("0) Voltar")
        return ut.naoVazio("Escolha o modo: ")


    def modoPvE(self):
        ut.limparTela()
        print("=== PvE: Escolha Herói e Vilão ===")

        if not self.heroi:
            print("\n⚠️  Nenhum herói selecionado.")
            ut.pausar()
            return

        todos = self.viloes_modo_hist + self.viloes
        for i, v in enumerate(todos, 1):
            print(f"{i}) {v.nome} (Maldade {v.maldade})")
        escolha = ut.lerInteiro("Número do vilão: ")
        if 1 <= escolha <= len(todos):
            self.vilao = todos[escolha - 1]
        else:
            print("Seleção inválida.")
            ut.pausar()
            return

        venceu = Batalha(self.heroi, self.vilao).iniciarBatalha()
        salvarHerois(self.herois)
        ut.pausar()


    def modoHistoria(self):
        ut.limparTela()
        print("=== História ===")

        if not self.heroi:
            print("\n⚠️  Selecione um herói antes de iniciar a História.")
            ut.pausar()
            return

        # Fase 1: Goblin
        print("\n-- Fase 1: Goblin --")
        goblin = self.viloes_modo_hist[0]
        self.heroi.dialogar("Cheguei à masmorra e vejo um Goblin!")
        ut.pausar()
        goblin.dialogar("Você não passará!")
        ut.pausar()
        ut.limparTela()
        venceu1 = Batalha(self.heroi, goblin).iniciarBatalha()
        salvarHerois(self.herois)
        ut.pausar()
        if not venceu1:
            print("☠ Seu Herói foi derrotado!\nGame Over. ")
            ut.pausar()
            return
        
        # Recompensa por vencer o Goblin
        print("\n-- Fase 1: Goblin --")
        print("🏆 Você derrotou o Goblin e ganhou 2 poções!")
        self.heroi.adicionarItem(PocaoVida())  # +1 Poção de Vida
        self.heroi.adicionarItem(PocaoMana())  # +1 Poção de Mana
        ut.pausar()
        ut.limparTela()
        

        # Fase 2: Dragão
        print("\n-- Fase 2: Dragão --")
        dragao = self.viloes_modo_hist[1]
        self.heroi.dialogar("O Goblin foi derrotado. Agora vem o Dragão!")
        ut.pausar()
        dragao.dialogar("ROOOOAR! Eu sou seu fim!")
        ut.pausar()
        venceu2 = Batalha(self.heroi, dragao).iniciarBatalha()
        salvarHerois(self.herois)
        ut.pausar()
        if venceu2:
            ut.limparTela()
            print("\n-- Fase 2: Dragão --")
            print("🎉 Parabéns! Você derrotou o Dragão e concluiu a história!")
            self.heroi.salvarRefem("Princesa")
        else:
            print("☠ Seu Herói foi derrotado!\nGame Over.")
            ut.pausar()


    def verInventario(self):
        """
        Exibe o inventário e o histórico de batalhas do herói selecionado.
        """
        ut.limparTela()
        if not self.heroi:
            print("\n⚠️  Nenhum herói selecionado.")
        else:
            print(f"=== Inventário de {self.heroi.nome} ===")
            if not self.heroi.inventario:
                print("(vazio)")
            else:
                for nome, qtd in self.heroi.inventario.items():
                    print(f"- {nome}: {qtd}")

            print("\n=== Histórico de Batalhas ===")
            if not self.heroi.historico:
                print("(nenhum histórico)")
            else:
                for evento in self.heroi.historico:
                    print(f"- {evento}")
        ut.pausar()


    def executar(self):
        while True:
            opc = self.menuInicial()
            match opc:
                case "1":
                    self.criarHeroi()
                case "2":
                    self.selecionarHeroi()
                case "3":
                    self.excluirHeroi()
                case "4":
                    self.listarTodos()
                case "5":
                    self.criarVilao()
                case "6":
                    modo = self.menuBatalha()
                    match modo:
                        case "1":
                            self.modoPvE()
                        case "2":
                            self.modoHistoria()
                        case _:
                            pass
                case "7":
                    self.verInventario()                
                case "0":
                    print("Encerrando...")
                    break
                case _:
                    print("Opção inválida.")
                    ut.pausar()


if __name__ == "__main__":
    Jogo().executar()
