# DESAFIO 🕹️ Improve This Game 🕹️

### Universidade Federal Rural de Pernambuco  
**Departamento de Estatística e Informática**  
**Bacharelado em Sistemas de Informação**  
**Disciplina: Princípios de Programação**

---

# **DESAFIO: Melhoria do Jogo de Personagens - POO em Python**


## **Objetivo**
Melhorar e refatorar um jogo de combate em modo texto, usando:
- Programação orientada a objetos
- Biblioteca **Rich** para menus e tabelas coloridas
- Persistência via JSON com carregamento dinâmico de subclasses

---

## **Funcionalidades**

### Personagens e Itens
- **Personagem**: classe base com `nome`, `idade`, `vida`, `ataque`, `defesa`.
- **Herói**: herda Personagem e adiciona `mana`, poções, inventário, histórico e métodos de serialização (`toDict`/`fromDict`).
- **Vilão**: herda Personagem, define níveis de maldade e ataques especiais.
- **Itens**: `PocaoVida`, `PocaoMana` e `Voucher`, aplicáveis durante a batalha.

### Arquétipos (`ClassesChar/`)
- **Mago**: lança `bolaDeFogo` (dano 45, custo de mana 25).
- **Arqueiro**: dispara `flechadaDeFogo` (dano 45, custo de mana 20 e flecha).
- **Ninja**: executa `ataqueSombrio` (dano 55, custo de mana 30) e tem chance de esquiva.
- **Guerreiro**: usa `marretadaBruta` (dano 45, custo de mana 15) e possui bônus de defesa.

### Batalha
- Loop de turnos com escolhas: ataque básico, ataque especial ou usar item.
- Registro de histórico de ações exibido ao final.

### Persistência
- **JSON**: heróis e vilões são salvos em `repositorio/herois.json` e `repositorio/viloes.json`.
- **Carregamento dinâmico**: o campo `classe` no JSON determina qual subclasse instanciar.

### Interface (Rich)
- Menus e tabelas coloridas para criação, listagem e seleção.
- Banners e efeitos de escrita simulando máquina de escrever.

---
## **Status das Tarefas**

- ✔️ **Concluído**  
  - Modelagem POO completa.  
  - Sistema de poções e itens.  
  - Batalhas com histórico.  
  - Persistência via JSON.  
  - Menu robusto em `main.py`.
  
---
## **Estrutura do Projeto**
```text
improve-this-game/
├── ClassChar/           # Arquétipos de heróis
│   ├── mago.py
│   ├── arqueiro.py
│   ├── ninja.py
│   └── guerreiro.py
├── batalha.py           # Lógica de combate
├── heroi.py             # Classe Herói e serialização
├── personagem.py        # Classe base Personagem
├── vilao.py             # Classe Vilão e ataques
├── itens.py             # Definição de Itens
├── repositorio.py       # Salvar/carregar JSON
├── utils.py             # Funções utilitárias + banner
├── main.py              # Fluxo principal do jogo
├── README.md            # Este arquivo
└── repositorio/         # Pasta com arquivos JSON
    ├── herois.json
    └── viloes.json
```

## **Como Executar o Código**

1. Clone este repositório:
   ```sh
   git clone https://github.com/GustavoSantosgcs/ImproveThisGame.git
   ```
2. Acesse a pasta do projeto:
   ```sh
   cd improve-this-game
   ```
3. Execute o jogo:
   ```sh
   python main.py
   ```
---
## **Proximas Melhorias**

- *Sistema de níveis e experiência*
- *Itens e habilidades adicionais*
- *Eventos aleatórios e narrativa mais rica*
- *Interface de usuário mais interativa*
- *Multiplayer local*

---

### **Aviso**

_Jogo ainda em desenvolvimento._

