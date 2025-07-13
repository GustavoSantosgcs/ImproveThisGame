import random
from rich.table   import Table
from rich         import box
from heroi        import Heroi
from vilao        import Vilao
from utils        import Utils

class Batalha:
    """
    Gerencia o loop de batalha entre um herói e um vilão,
    mantendo registro de todas as ações em um histórico.
    """

    def __init__(self, heroi: Heroi, vilao: Vilao):
        self.heroi   = heroi
        self.vilao    = vilao
        self.historico: list[str] = []
        self.console = Utils.console


    def iniciarBatalha(self):
        self.console.clear()
        self.console.print("\n=== BATALHA INICIADA ===", style="bold red")
        self.historico.append(f"Batalha: {self.heroi.nome} vs {self.vilao.nome}")
        turno = 1

        while self.heroi.vida > 0 and self.vilao.vida > 0:

            # Exibir status de herói e vilão
            status = Table(box=box.SIMPLE_HEAVY)
            status.add_column("Personagem", style="cyan")
            status.add_column("Vida", justify="right")
            status.add_column("Mana", justify="right")
            status.add_row(
                self.heroi.nome,
                f"{self.heroi.vida}/{self.heroi.MAX_VIDA}",
                f"{self.heroi.mana}/{self.heroi.MAX_MANA}"
            )
            status.add_row(
                self.vilao.nome,
                str(self.vilao.vida),
                "-"
            )
            self.console.print(f"\n[bold]Turno {turno}[/bold]")
            self.console.print(status)

            # Ações do herói
            self.console.print("\n[bold yellow]Ações:[/] [green](A) Básico[/] [magenta](B) Especial[/] [blue](I) Item[/]")
            escolha = self.console.input("> ").strip().lower()

            if escolha in ("a", "1"):
                self.heroi.ataqueBasico(self.vilao)
                self.historico.append(
                    f"{self.heroi.nome} fez básico em {self.vilao.nome} ({self.vilao.vida} PV)"
                )

            elif escolha in ("b", "2"):
                self.heroi.ataqueEspecial(self.vilao)
                self.historico.append(
                    f"{self.heroi.nome} fez especial em {self.vilao.nome} ({self.vilao.vida} PV)"
                )

            elif escolha in ("i", "3"):
                inv = self.heroi.inventario
                if not inv:
                    self.console.print("[red]Inventário vazio![/red]")
                    self.historico.append(
                        f"{self.heroi.nome} tentou usar item, mas inventário vazio"
                    )
                else:
                    nomes = list(inv.keys())
                    itens = Table(title="Itens", box=box.MINIMAL)
                    itens.add_column("#", justify="center")
                    itens.add_column("Item")
                    itens.add_column("Qtd", justify="right")
                    for i, nome in enumerate(nomes, 1):
                        itens.add_row(str(i), nome, str(inv[nome]))
                    self.console.print(itens)
                    sel = self.console.input("Escolha o item: ").strip()
                    if sel.isdigit() and 1 <= int(sel) <= len(nomes):
                        item_sel = nomes[int(sel)-1]
                        self.heroi.usarItem(item_sel)
                        self.historico.append(f"{self.heroi.nome} usou {item_sel}")
                    else:
                        self.console.print("[red]Escolha inválida![/red]")
                        self.historico.append(
                            f"{self.heroi.nome} fez ação inválida de item"
                        )

            else:
                self.console.print("[red]Opção inválida! Você perdeu a vez.[/red]")
                self.historico.append(
                    f"{self.heroi.nome} perdeu turno por escolha inválida"
                )

            Utils.pausar()
            self.console.clear()

            # Verifica derrota do vilão
            if self.vilao.vida <= 0:
                self.console.print(f"[green]{self.vilao.nome} foi derrotado! 🎉[/green]")
                self.historico.append(f"{self.vilao.nome} derrotado turno {turno}")
                break

            # Ação do vilão
            self.console.print(f"\n[bold magenta]Vez de {self.vilao.nome} atacar[/bold magenta]")
            if random.random() < 0.3:
                self.vilao.ataqueDevastador(self.heroi)
                self.historico.append(
                    f"{self.vilao.nome} devastador em {self.heroi.nome} ({self.heroi.vida} PV)"
                )
            else:
                self.vilao.ataqueBasico(self.heroi)
                self.historico.append(
                    f"{self.vilao.nome} básico em {self.heroi.nome} ({self.heroi.vida} PV)"
                )

            # Verifica derrota do herói
            if self.heroi.vida <= 0:
                self.console.print(f"[red]{self.heroi.nome} foi derrotado... 😢[/red]")
                self.historico.append(f"{self.heroi.nome} derrotado turno {turno}")
                break

            turno += 1
            Utils.pausar()
            self.console.clear()

        # Anexa histórico ao herói e exibe tabela
        self.heroi.historico.extend(self.historico)
        self.console.print("\n=== BATALHA ENCERRADA ===", style="bold red")
        hist_tab = Table(title="Histórico de Ações", box=box.MINIMAL)
        hist_tab.add_column("Evento")
        for ev in self.historico:
            hist_tab.add_row(ev)
        self.console.print(hist_tab)

        return self.heroi.vida > 0

