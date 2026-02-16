# Gerador de Resultados – Pedra, Papel e Tesoura

Este projeto implementa um gerador de resultados para o jogo Pedra, Papel e Tesoura em Python, permitindo simular partidas de forma simples via linha de comando.

## Objetivo do projeto

- Praticar lógica condicional em Python.
- Trabalhar com entradas do usuário e validação de opções.
- Simular a lógica de vitória, derrota ou empate entre duas jogadas.

## Tecnologias utilizadas

- Python 3

## Estrutura do projeto

```text
Gerador de Resultados pedra papel tesoura/
├── gerador_ppt.py   # Script principal do jogo Pedra, Papel e Tesoura
└── README.md        # Documentação deste projeto
O arquivo gerador_ppt.py contém a lógica do jogo e a interação via terminal. [page:6]

Como executar
Clonar o repositório (se ainda não clonou):

bash
git clone https://github.com/wellingt0n-0liveira/python_projetos.git
cd "python_projetos/Gerador de Resultados pedra papel tesoura"
(Opcional) Criar e ativar um ambiente virtual:

bash
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
# ou
.venv\Scripts\activate      # Windows
Executar o script do jogo:

bash
python gerador_ppt.py
# ou
python3 gerador_ppt.py
Exemplo de uso
Ao executar o programa, ele irá interagir com o usuário pelo terminal, pedindo para escolher entre Pedra, Papel ou Tesoura (os detalhes exatos podem variar conforme as mensagens definidas no código).
Com base nas escolhas, o script determina e exibe o resultado da partida (vitória, derrota ou empate).

Exemplo ilustrativo:

text
Escolha uma opção:
1 - Pedra
2 - Papel
3 - Tesoura
Digite sua opção: 1
O computador escolheu: Tesoura
Resultado: Você venceu! Pedra quebra Tesoura.
Aprendizados e pontos de destaque
Uso de condicionais (if, elif, else) para definir regras do jogo.

Estruturação de regras de negócio simples (quem ganha de quem) de forma clara.

Boas práticas iniciais para interação com o usuário via linha de comando. [page:6]

Possíveis melhorias futuras
Tratar melhor entradas inválidas (opções fora do menu, texto em vez de número, etc.).

Permitir múltiplas rodadas com placar acumulado (vitórias, derrotas, empates).

Adicionar aleatoriedade na jogada do computador, usando o módulo random.

Criar uma versão com interface gráfica (por exemplo, usando tkinter) ou uma API simples para uso via HTTP.
