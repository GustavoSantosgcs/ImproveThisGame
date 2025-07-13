# DESAFIO 🕹️ Improve This Game 🕹️

### Universidade Federal Rural de Pernambuco  
**Departamento de Estatística e Informática**  
**Bacharelado em Sistemas de Informação**  
**Disciplina: Princípios de Programação**

---

# **DESAFIO: Melhoria do Jogo de Personagens - POO em Python**


## **Descrição Atual**
Este repositório apresenta um jogo de combate em modo texto, já refatorado e ampliado com:

- **Modelagem POO completa**: classes Personagem, Heroi, Vilao e arquétipos (Mago, Arqueiro, Ninja, Guerreiro) em `ClassChar/.
- **Sistema de batalha**: classe Batalha gerencia turnos, usando match para escolhas e POO para lógica de combate.
- **Fluxo principal em main.py**: classe Jogo gerencia criação, seleção, exclusão, listagem, modos de batalha (PvE e História) e visualização de inventário/histórico.
- **Persistência**: arquivos JSON (`herois.json`, `viloes.json`) armazenam heróis com inventário e histórico, e vilões.
---

## **Funcionalidades Implementadas**

1. **Personagens**
   - **Personagem**: atributos genéricos (`nome`, `idade`, `vida`, `ataque`, `defesa`), métodos `curar()` e `receberDano()`.
   - **Heroi**: adiciona mana, poções (`usarPocaoVida()`, `usarPocaoMana()`), `salvarRefem()`, `dialogar()`, inventario com `adicionarItem()`/`usarItem()`, serialização `toDict()`/`fromDict()`.
   - **Vilao**: níveis de maldade, `ataqueBasico()`, `ataqueDevastador()`, `dialogar()`, serialização.

2. **Arquétipos em `ClassChar/`**
   - **Mago**: `bolaDeFogo()`, kit inicial de poções.
   - **Arqueiro**: `flechadaDeFogo()`, flechas e poções.
   - **Ninja**: `ataqueSombrio()`, chance de esquiva, poções.
   - **Guerreiro**: `marretadaBruta()`, bônus de defesa, poções.

3. **Batalha (`batalha.py`)**
   - **Menu de ações:** 1) básico, 2) especial, 3) itens.
   - **Histórico** de eventos registrado e anexado ao `heroi.historico`.

4. **Itens (`itens.py`)**
   - Item (base), `PocaoVida`, `PocaoMana`, `Voucher`.
   - Uso durante a batalha via `heroi.usarItem()`.

5. **Repositório (`repositorio.py`)**
   - Garante diretório `repositorio/`.
   - `salvarHerois()`/`carregarHerois()`: inventário e histórico incluídos.
   - `salvarViloes()`/`carregarViloes()`: usa `toDict()`/`fromDict()`.

6. **Aplicação (`main.py`)**
   - Criação, seleção, exclusão, listagem de heróis/vilões.
   - Modos **PvE** (seleção de herói e vilão) e **História** (duas fases com recompensas).
   - Opção de visualizar inventário e histórico.

---
## **Status das Tarefas**

- ✔️ **Concluído**  
  - Modelagem POO completa.  
  - Sistema de poções e itens.  
  - Batalhas com histórico.  
  - Persistência via JSON.  
  - Menu robusto em `main.py`.

- ➖ **Em Planejamento**   
  - UI com cores e ASCII art.

---
## **Estrutura do Projeto**
```text
improve-this-game/
├── personagem.py
├── heroi.py
├── vilao.py
├── itens.py
├── batalha.py
├── utils.py
├── repositorio.py
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
---
## **Proximas Melhorias**

- **Diálogos e narrativa:** implementar dialogar() e eventos randômicos.

- **Inventário e itens:** adicionar armas, poções especiais.

- **Sistema de níveis:** experiência e upgrades de atributos.

- **Multiplayer local:** batalha entre dois heróis.

- **Interface aprimorada:** cores, delays, menus dinâmicos.

---

### **Aviso**

_Jogo ainda em desenvolvimento._

