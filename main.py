from rich.console import Console
from rich.table   import Table
from rich         import box
from ClassesChar.mago      import Mago
from ClassesChar.arqueiro  import Arqueiro
from ClassesChar.ninja     import Ninja
from ClassesChar.guerreiro import Guerreiro
from vilao                 import Vilao
from batalha               import Batalha
from utils                 import Utils
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
        self.console = Console()
        self.herois = carregarHerois()
        self.viloes = carregarViloes()
        self.heroi: Heroi | None = None
        self.vilao: Vilao | None = None
        self.viloes_modo_hist = [ 
            Vilao("Goblin", 30, 80, "Média", 15, 5), #nome, idade, vida, maldade, ataque, defesa
            Vilao("Dragão", 300, 130, "Alta", 22, 10)
        ]


    def showMenu(self, title, items, style="yellow"):
        """
        Exibe um menu rico no terminal usando Rich:
        - title: cabeçalho do menu
        - items: lista de tuplas (chave, descrição)
        - style: cor principal do menu
        """
        
        self.console.clear()
        tbl = Table(title=f"[bold {style}]{title}[/bold {style}]", box=box.ROUNDED, border_style=style)
        tbl.add_column("Opção", style="cyan", justify="center")
        tbl.add_column("Descrição", style="white")
        for key, desc in items:
            tbl.add_row(key, desc)
        self.console.print(tbl)


    def menuInicial(self):
        """
        Mostra o banner principal e aguarda Enter,
        depois exibe o menu de opções e retorna a escolha.
        """
        self.console.clear()
        Utils.bannerPrincipal()
        Utils.console.input("\nPressione enter para continuar…")
        itens = [
            ("1", "Criar Herói"),
            ("2", "Selecionar Herói"),
            ("3", "Excluir Herói"),
            ("4", "Listar Heróis e Vilões"),
            ("5", "Criar Vilão"),
            ("6", "Iniciar Batalha"),
            ("7", "Ver Inventário e Histórico"),
            ("0", "Sair"),
        ]
        self.showMenu("Menu Principal", itens)
        return Utils.naoVazio("Escolha uma opção: ")


    def criarHeroi(self):
        """
        Cria um herói pedindo nome, idade, classe e confirmando descrição.
        """
        self.console.clear()
        nome  = Utils.naoVazio("Nome: ")
        idade = Utils.lerInteiro("Idade: ")
        classes = [("1","Mago"),("2","Arqueiro"),("3","Ninja"),("4","Guerreiro")]
        while True:
            tbl = Table(title="Escolha a Classe", box=box.SIMPLE)
            tbl.add_column("#", justify="center")
            tbl.add_column("Classe")
            for k, c in classes:
                tbl.add_row(k, c)
            self.console.print(tbl)
            opc = Utils.naoVazio("Opção: ")
            if opc == "1": cls = Mago
            elif opc == "2": cls = Arqueiro
            elif opc == "3": cls = Ninja
            elif opc == "4": cls = Guerreiro
            else:
                self.console.print("[red]Opção inválida![/red]")
                Utils.pausar()
                continue

            # instancia e mostra descrição
            heroi = cls(nome, idade)
            desc = heroi.descricao()
            self.console.print(f"[cyan]{desc}[/cyan]")
            confirma = Utils.naoVazio("Manter esta classe? (S/N): ").strip().lower()
            if confirma == "s":
                break

        # salvar herói
        self.herois.append(heroi)
        salvarHerois(self.herois)
        self.console.print(f"[green]Herói {heroi.nome} ({heroi.__class__.__name__}) criado![/green]")
        Utils.pausar()


    def selecionarHeroi(self):
        """
        Lista heróis salvos, pede um número e
        marca aquele índice como herói ativo.
        """
        self.console.clear()
        if not self.herois:
            self.console.print("[red]Nenhum herói disponível![/red]")
            Utils.pausar()
            return
        tbl = Table(title="Selecione o Herói", box=box.SIMPLE)
        tbl.add_column("#", justify="center")
        tbl.add_column("Nome")
        for i, h in enumerate(self.herois,1): tbl.add_row(str(i), h.nome)
        self.console.print(tbl)
        sel = Utils.lerInteiro("Número do herói: ")
        if 1 <= sel <= len(self.herois):
            self.heroi = self.herois[sel-1]
            self.console.print(f"[green]Herói selecionado: {self.heroi.nome}[/green]")
        else:
            self.console.print("[red]Seleção inválida![/red]")
        Utils.pausar()
        
        
    def excluirHeroi(self):
        """
        Exibe heróis, pede índice para remoção
        e atualiza o arquivo JSON.
        """
        self.console.clear()
        if not self.herois:
            self.console.print("[red]Nenhum herói cadastrado![/red]")
            Utils.pausar()
            return
        tbl = Table(title="Excluir Herói", box=box.SIMPLE)
        tbl.add_column("#", justify="center")
        tbl.add_column("Nome")
        for i, h in enumerate(self.herois,1): tbl.add_row(str(i), h.nome)
        self.console.print(tbl)
        sel = Utils.lerInteiro("Número para excluir: ")
        if 1 <= sel <= len(self.herois):
            rem = self.herois.pop(sel-1)
            if self.heroi == rem: self.heroi=None
            salvarHerois(self.herois)
            self.console.print(f"[green]{rem.nome} excluído![/green]")
        else:
            self.console.print("[red]Opção inválida![/red]")
        Utils.pausar()


    def listarTodos(self):
        """
        Mostra as tabelas de heróis e vilões
        cadastrados no momento.
        """        
        self.console.clear()
        tblH = Table(title="Heróis Cadastrados", box=box.SIMPLE)
        tblH.add_column("Nome")
        tblH.add_column("Classe")
        tblH.add_column("Vida", justify="right")
        tblH.add_column("Mana", justify="right")
        for h in self.herois:
            tblH.add_row(h.nome, h.__class__.__name__, f"{h.vida}/{h.MAX_VIDA}", f"{h.mana}/{h.MAX_MANA}")
        self.console.print(tblH)

        tblV = Table(title="Vilões", box=box.SIMPLE)
        tblV.add_column("Nome")
        tblV.add_column("Maldade")
        tblV.add_column("Vida", justify="right")
        for v in self.viloes_modo_hist + self.viloes:
            tblV.add_row(v.nome, str(v.maldade), str(v.vida))
        self.console.print(tblV)
        Utils.pausar()


    def criarVilao(self):
        """
        Pergunta dados do vilão (nome, idade, atributos)
        e salva no repositório.
        """       
        self.console.clear()
        nome  = Utils.naoVazio("Nome: ")
        idade = Utils.lerInteiro("Idade: ")
        vida  = Utils.lerInteiro("Vida: ")
        maldade = Utils.naoVazio("Maldade (Baixa/Média/Alta): ").title()
        ataque  = Utils.lerInteiro("Ataque: ")
        defesa  = Utils.lerInteiro("Defesa: ")
        v = Vilao(nome, idade, vida, maldade, ataque, defesa)
        self.viloes.append(v)
        salvarViloes(self.viloes)
        self.console.print(f"[green]Vilão {v.nome} criado![/green]")
        Utils.pausar()


    def menuBatalha(self):
        """
        Exibe as opções de batalha (PvE/História)
        e retorna a escolha feita.
        """        
        itens=[("1","PvE"),("2","História"),("0","Voltar")]
        self.showMenu("Modo de Batalha", itens, style="green")
        return Utils.naoVazio("Escolha o modo: ")


    def modoPvE(self):
        self.console.clear()
        if not self.heroi:
            self.console.print("[red]Selecione um herói antes![/red]")
            Utils.pausar()
            return
        todos = self.viloes_modo_hist + self.viloes
        tbl = Table(title="Escolha o Vilão", box=box.SIMPLE)
        tbl.add_column("#", justify="center")
        tbl.add_column("Nome")
        tbl.add_column("Maldade")
        for i,v in enumerate(todos,1): tbl.add_row(str(i), v.nome, str(v.maldade))
        self.console.print(tbl)
        sel = Utils.lerInteiro("Número do vilão: ")
        if 1<=sel<=len(todos): self.vilao = todos[sel-1]
        else:
            self.console.print("[red]Seleção inválida![/red]")
            Utils.pausar()
            return
        venceu = Batalha(self.heroi, self.vilao).iniciarBatalha()
        salvarHerois(self.herois)
        Utils.pausar()


    def modoHistoria(self):
        """
        Roda o modo História em duas fases:
        Goblin e Dragão, com recompensas entre elas.
        """
        self.console.clear()
        if not self.heroi:
            self.console.print("[red]Selecione um herói antes![/red]")
            Utils.pausar()
            return
        fases=[("Goblin",0),("Dragão",1)]
        for nome,i in fases:
            Utils.limparTela()
            self.console.print(f"\n-- Fase: {nome} --")
            inim= self.viloes_modo_hist[i]
            self.heroi.dialogar(f"Encontro: {nome}")
            Utils.pausar()
            venceu = Batalha(self.heroi, inim).iniciarBatalha()
            salvarHerois(self.herois)
            if not venceu:
                Utils.limparTela()
                self.console.print(f"[red]{nome} foi imbatível! Fim de jogo.[/red]")
                Utils.pausar()
                return
            if nome=="Goblin":
                self.heroi.addItem(PocaoVida()); self.heroi.addItem(PocaoMana())
                self.console.print("[green]Recompensa: 2 poções[/green]")
                Utils.pausar()
            else:
                self.heroi.salvarRefem("Princesa")
                self.console.print("[green]História concluída![/green]")
                Utils.pausar()


    def verInventario(self):
        """
        Mostra tabelas de inventário e histórico
        do herói atualmente selecionado.
        """
        self.console.clear()
        if not self.heroi:
            self.console.print("[red]Nenhum herói selecionado![/red]")
            Utils.pausar()
            return
        inv, hist = self.heroi.inventario, self.heroi.historico
        tblI = Table(title=f"Inventário de {self.heroi.nome}", box=box.MINIMAL)
        tblI.add_column("Item"); tblI.add_column("Qtd", justify="right")
        if inv: [tblI.add_row(k,str(v)) for k,v in inv.items()]
        else: tblI.add_row("(vazio)","")
        self.console.print(tblI)
        tblH = Table(title="Histórico de Batalhas", box=box.MINIMAL)
        tblH.add_column("Evento")
        if hist: [tblH.add_row(e) for e in hist]
        else: tblH.add_row("(nenhum histórico)")
        self.console.print(tblH)
        Utils.pausar()


    def executar(self):
        """
        Laço principal:
        - chama menuInicial()
        - despacha para o método certo
        - sai quando o usuário escolher 0
        """       
        while True:
            opc=self.menuInicial()
            match opc:
                case "1": self.criarHeroi()
                case "2": self.selecionarHeroi()
                case "3": self.excluirHeroi()
                case "4": self.listarTodos()
                case "5": self.criarVilao()
                case "6":
                    m=self.menuBatalha()
                    if m=="1": self.modoPvE()
                    elif m=="2": self.modoHistoria()
                case "7": self.verInventario()
                case "0": break
                case _: self.console.print("[red]Opção inválida![/red]")


if __name__=="__main__":
    Jogo().executar()