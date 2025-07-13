import os
import sys
import time
from rich.console import Console


class Utils:
    """Funções utilitárias de terminal."""
    console = Console()
    
    @staticmethod
    def naoVazio(msg: str):
        """
        Solicita ao usuário uma string não-vazia.
        """
        while True:
            valor = input(msg).strip()
            if valor:
                return valor
            Utils.console.print("[red]Entrada não pode ficar vazia. Tente novamente.[/red]")


    @staticmethod
    def lerInteiro(entrada: str):
        """
        Solicita ao usuário um inteiro, repetindo até ser válido.
        """
        while True:
            valor = input(entrada).strip()
            if valor.isdigit() or (valor.startswith('-') and valor[1:].isdigit()):
                return int(valor)
            Utils.console.print("[red]Por favor, digite um número inteiro válido.[/red]")


    @staticmethod
    def pausar():
        """
        Pausa a execução até o usuário pressionar Enter.
        """
        Utils.console.input("\n[grey]Pressione Enter para continuar...[/grey]")


    @staticmethod
    def limparTela():
        """
        Limpa a tela do terminal de forma cross-platform.
        """
        if sys.platform.startswith("win"):
            os.system("cls")
        else:
            os.system("clear")


    @staticmethod
    def escrever(texto: str, delay: float = 0.02):
        """
        Imprime cada caractere de `texto` com um pequeno atraso,
        simulando uma máquina de escrever.
        """
        for c in texto:
            print(c, end='', flush=True)
            time.sleep(delay)
        print()
        
        
    @staticmethod
    def bannerPrincipal():
        """
        Exibe um banner estilizado no topo do jogo.
        """
        title = (
            "\n"
            "  ██████╗   ██████╗  ███╗   ██╗  ██████╗  ██╗   ██╗ ███████╗  ██████╗ \n"
            " ██╔════╝  ██╔═══██╗ ████╗  ██║ ██╔═══██╗ ██║   ██║ ██╔════╝ ██╔══██╗\n"
            " ██║       ██║   ██║ ██╔██╗ ██║ ██║   ██║ ██║   ██║ █████╗   ██████╔╝\n"
            " ██║       ██║   ██║ ██║╚██╗██║ ██║ █╗██║ ██║   ██║ ██╔══╝   ██╔══██╗\n"
            " ╚██████╗  ╚██████╔╝ ██║ ╚████║ ╚██████╔╝ ╚██████╔╝ ███████╗ ██║  ██║\n"
            "  ╚═════╝   ╚═════╝  ╚═╝  ╚═══╝  ╚═════╝   ╚═════╝  ╚══════╝ ╚═╝  ╚═╝ \n"
        )
        Utils.console.print(f"[cyan bold]{title}[/cyan bold]", justify="left")
