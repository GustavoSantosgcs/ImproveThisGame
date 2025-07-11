from ClassesChar.mago import Mago
from ClassesChar.arqueiro import Arqueiro
from ClassesChar.ninja import Ninja
from ClassesChar.guerreiro import Guerreiro
from vilao import Vilao
from batalha import Batalha
from utils import Utils as ut


class Jogo:
    """
    Gerencia ciclo de criação e batalha do jogo.
    """
    def __init__(self) -> None:
        self.heroi = None
        self.vilao = None


    def criarHeroi(self) -> None:
        """
        Exibe menu de classes e cria instância de Heroi usando match.
        """
        ut.limparTela()
        print("=== Criação de Herói ===")
        nome = ut.naoVazio("Digite o nome do seu herói: ")
        idade = int(input("Digite a idade do seu herói: ").strip())        

        while True:
            print("1) Mago\n2) Arqueiro\n3) Ninja\n4) Guerreiro")
            escolha = ut.naoVazio("Escolha sua classe: ")
            match escolha:
                case "1":
                    self.heroi = Mago(nome, idade)
                    break
                case "2":
                    self.heroi = Arqueiro(nome, idade)
                    break
                case "3":
                    self.heroi = Ninja(nome, idade)
                    break
                case "4":
                    self.heroi = Guerreiro(nome, idade)
                    break
                case _:
                    print("\nOpção inválida. Você precisa escolher uma classe\n.")
        
                   
    def criarVilao(self) -> None:
        """
        Cria um vilão de exemplo para a batalha.
        """
        self.vilao = Vilao(
            nome="Goblin",
            idade=30,
            vida=80,
            maldade="Média",
            ataque=25,
            defesa=5
        )

    def executar(self) -> None:
        """
        Inicia o fluxo de jogo: criação e batalha.
        """
        while True:
            self.criarHeroi()
            self.criarVilao()
            batalha = Batalha(self.heroi, self.vilao)
            batalha.iniciar_batalha()
            
            print("Deseja uma nova rodada?")
            opcao = ut.naoVazio("Digite: [S] ou [N] ")
            match opcao.lower():
                case 's':
                    input("Entendido! Pressione Enter para continuar...")
                    ut.limparTela()
                
                case 'n':
                    print("Ok! Vamos encerrar por aqui... até logo!")
                    break
                
                case _:
                    print("Não entendi sua opção\n")


if __name__ == "__main__":
    jogo = Jogo()
    jogo.executar()
