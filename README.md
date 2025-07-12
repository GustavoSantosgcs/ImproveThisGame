# DESAFIO 🕹️ Improve This Game 🕹️

### Universidade Federal Rural de Pernambuco  
**Departamento de Estatística e Informática**  
**Bacharelado em Sistemas de Informação**  
**Disciplina: Princípios de Programação**

---

# **DESAFIO: Melhoria do Jogo de Personagens - POO em Python**

## **Descrição Atual**
O repositório apresenta um jogo de combate em modo texto, agora refatorado com:

- **POO completa:** classes `Personagem`, `Heroi`, `Vilao` e arquétipos (`Mago`, `Arqueiro`, `Ninja`, `Guerreiro`) em `ClassChar/`.  
- **Sistema de batalha:** classe `Batalha` que gerencia turnos, usando `match` para ações e POO.  
- **Fluxo principal:** classe `Jogo` em `main.py` que cria personagens e inicia batalhas.  


## **Funcionalidades Implementadas**

1. **Classes principais:**  
   - `Personagem` (base genérica com `vida`, `ataque`, `defesa`, `curar()`, `receberDano()`).  
   - `Heroi` (atributos de `mana`, métodos de poções: `usarPocaoVida()`, `usarPocaoMana()`, stub de `ataqueEspecial()`).  
   - `Vilao` (níveis de maldade, `ataqueBasico()`, `ataqueSinistro()`, defesa customizada).  
2. **Arquetipos em `ClassChar/`:**  
   - `Mago`: `bolaDeFogo()`.  
   - `Arqueiro`: `ataqueComFlecha()`.  
   - `Ninja`: `ataqueSombrio()`, `tentarEsquivar()`.  
   - `Guerreiro`: `golpeForte()`, bônus de defesa.  
3. **Batalha (`batalha.py`):**  
   - Loop de turnos até um personagem derrotar o outro.  
   - `match` nas escolhas do herói.  
   - Ações randômicas do vilão.  
4. **Jogo (`main.py`):**  
   - Classe `Jogo` encapsula criação de herói/vilão e fluxo de batalha.  
   - Escolha de classe via `match`.  
  

## **Status das Tarefas**

- ✔️ **Concluído**  
  - Personagens com `nome`, `vida`, `ataque`, `defesa`.  
  - `Heroi` herda `Personagem`, implementa `usarPocaoVida()` e `usarPocaoMana()`.  
  - Batalha encapsulada em `Batalha`, usando `match` e POO.  

- ➖ **Pendente**  
  - Método `salvarRefem()` na classe `Heroi`.  
  - Método `dialogar()` para interações narrativas.  
  - Estruturas de **listas** e **dicionários** para múltiplos heróis/vilões.  
  - Registro de histórico de ações (log de batalha).  
  - Integração de sistema de inventário e itens/vouchers.  

## **Estrutura do Projeto**
```text
improve-this-game/
├── personagem.py
├── heroi.py
├── vilao.py
├── batalha.py
├── utils.py
├── main.py
├── README.md
└── ClassChar/
    ├── mago.py
    ├── arqueiro.py
    ├── ninja.py
    └── guerreiro.py
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

## **Proximas Melhorias**

- **Diálogos e narrativa:** implementar dialogar() e eventos randômicos.

- **Inventário e itens:** adicionar armas, poções especiais, vouchers.

- **Registro de log:** histórico detalhado pós-batalha.

- **Sistema de níveis:** experiência e upgrades de atributos.

- **Multiplayer local:** batalha entre dois heróis.

- **Interface aprimorada:** cores, delays, menus dinâmicos.

---

### **Aviso**

_Jogo ainda em desenvolvimento._

