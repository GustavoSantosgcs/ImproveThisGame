import os
import sys

class Utils:
    """Funções utilitárias de terminal. """
    
    @staticmethod
    def naoVazio(msg: str):
        """
        Solicita ao usuário uma string não-vazia.
        
        Parâmetros:
            msg: texto do input mostrado ao usuário
        
        Retorna:
            A string não-vazia digitada pelo usuário.
        """
        while True:
            valor = input(msg).strip()
            if valor:
                return valor
            print("Entrada não pode ficar vazia. Tente novamente.")


    @staticmethod
    def lerInteiro(entrada: str):
        """
        Solicita ao usuário um inteiro, repetindo até ser válido.
        
        Parâmetros:
            entrada: texto do input mostrado ao usuário
        
        Retorna:
            O inteiro lido do usuário.
        """
        while True:
            entrada = input(entrada).strip()
            if entrada.isdigit() or (entrada.startswith('-') and entrada[1:].isdigit()):
                return int(entrada)
            print("Por favor, digite um número inteiro válido.")


    @staticmethod
    def pausar():
        """
        Pausa a execução até o usuário pressionar Enter.
        """
        input("\nPressione Enter para continuar...")


    @staticmethod
    def limparTela():
        """
        Limpa a tela do terminal de forma cross-platform.
        """
        # Windows
        if sys.platform.startswith("win"):
            os.system("cls")
        # Mac / Linux
        else:
            os.system("clear")
