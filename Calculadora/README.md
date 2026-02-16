# Calculadora em Python

Este projeto implementa calculadoras simples em Python para operações matemáticas básicas via linha de comando, servindo como prática de lógica, entrada de dados e formatação de saída.

## Objetivo do projeto

- Praticar a leitura de dados do usuário usando `input`.
- Trabalhar com conversão de tipos (`float`) e operações matemáticas.
- Exibir resultados formatados e claros no terminal.

## Tecnologias utilizadas

- Python 3

## Estrutura do projeto

```text
Calculadora/
├── calculadora.py     # Versão simples: soma de dois números
├── calculadora2.py    # Versão evoluída com legenda/explicação (futuras melhorias)
└── README.md          # Documentação deste projeto
Atualmente, o script calculadora.py realiza a soma de dois números informados pelo usuário. [page:5]

Como executar
Clonar o repositório (se ainda não clonou):

bash
git clone https://github.com/wellingt0n-0liveira/python_projetos.git
cd python_projetos/Calculadora
(Opcional) Criar e ativar um ambiente virtual:

bash
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
# ou
.venv\Scripts\activate      # Windows
Executar a calculadora simples:

bash
python calculadora.py
# ou
python3 calculadora.py
Exemplo de uso
Ao rodar calculadora.py, o programa solicitará dois números:

text
Digite o primeiro número: 10
Digite o segundo número: 5
O resultado da soma é: 15.0
O script converte as entradas para float, soma os valores e exibe o resultado no terminal. [page:5]

Aprendizados e pontos de destaque
Leitura de entradas do usuário com input.

Conversão de string para número (float) para permitir operações aritméticas.

Uso de f-strings para formatar a saída (print(f"...")). [page:5]

Possíveis melhorias futuras
Criar um menu de operações (soma, subtração, multiplicação, divisão).

Tratar erros de entrada (ex.: texto em vez de número, divisão por zero).

Unificar a lógica em funções reutilizáveis.

Evoluir calculadora2.py para uma versão mais completa com explicações de cada operação e talvez uma interface mais amigável.