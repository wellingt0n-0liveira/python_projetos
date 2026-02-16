# Cifra de César em Python

Este projeto implementa a Cifra de César em Python, permitindo aplicar um deslocamento nas letras de um texto para simular um processo simples de criptografia por substituição.  
O foco é treinar lógica de programação, manipulação de strings e conceitos básicos de segurança da informação.

## Como o programa funciona

O script solicita ao usuário:

1. Um texto para ser cifrado ou “decifrado”.
2. Um valor inteiro de deslocamento (positivo ou negativo).

Em seguida, o programa:

- Aplica o deslocamento informado a cada caractere alfabético (maiúsculo ou minúsculo).
- Mantém caracteres não alfabéticos (espaços, pontuação, números) inalterados.
- Exibe o resultado como “Texto cifrado/descifrado”.

> Observação: como a função aplica o deslocamento diretamente, um deslocamento positivo tende a cifrar e um deslocamento negativo tende a reverter (descifrar) o texto.

## Funcionalidades

- Suporte a letras maiúsculas e minúsculas.
- Manutenção de caracteres não alfabéticos sem alteração.
- Aceita qualquer valor inteiro de deslocamento (o código faz o ajuste com módulo 26).

## Pré-requisitos

- Python 3 instalado.

Verifique:

```bash
python --version
# ou
python3 --version
Como executar
Clone o repositório principal:

bash
git clone https://github.com/wellingt0n-0liveira/python_projetos.git
cd python_projetos/"Cifra de Cesar"
Execute o script:

bash
python CifraDeCesar.py
# ou
python3 CifraDeCesar.py
Informe os dados solicitados no terminal:

Texto a ser cifrado/“descifrado”.

Quantidade de posições a ser deslocada (por exemplo, 3 ou -3).

Exemplo de uso
Entrada:

Texto: Seguranca

Deslocamento: 3

Saída (exemplo ilustrativo):

text
Texto cifrado/descifrado: Vhjxudqfd
Se você usar o mesmo texto com deslocamento -3, o resultado tende a reverter o efeito (simulando a “decifragem”).

Estrutura do projeto
text
Cifra de Cesar/
├── CifraDeCesar.py   # Script principal com a implementação da cifra de César
└── README.md         # Documentação deste projeto
Possíveis melhorias futuras
Separar claramente as opções de cifrar e decifrar via menu (interface de linha de comando).

Adicionar testes automatizados em Python (por exemplo, pytest) para validar diferentes cenários.

Tratar erros de entrada (ex.: valor de deslocamento não numérico).

Criar uma versão com interface gráfica ou API para uso via HTTP.

Contexto para portfólio
Este projeto demonstra:

Implementação de um algoritmo clássico de criptografia por substituição.

Manipulação de caracteres, uso de funções e boas práticas básicas de Python.

No contexto de segurança, ilustra como técnicas antigas de cifra funcionam e por que não são adequadas para uso real em produção, mas úteis para estudo de fundamentos.

text

Se quiser, no próximo passo posso sugerir um padrão de README semelhante para todos os outros projetos dentro de `python_projetos`, para deixar o repositório inteiro com uma cara mais profissional.[2][1]
Se quiser, no próximo passo posso sugerir um padrão de README semelhante para todos os outros projetos dentro de `python_projetos`, para deixar o repositório inteiro com uma cara mais profissional.[2][1]

sim
Faz sentido padronizar, principalmente porque seu repositório é claramente de portfólio para mercado de trabalho.
​

Padrão geral do repositório
Sugestão para manter tudo organizado:

README.md na raiz explicando a ideia do repositório e listando os projetos com links.
​

Um README.md simples dentro de cada pasta de projeto, seguindo um mesmo esqueleto.
​

Exemplo de índice no README.md da raiz (você pode adaptar os nomes):

text
# python_projetos

Projetos práticos envolvendo Python, focados em lógica, automação, análise de dados e aplicações para o mercado de trabalho.

## Projetos

- [Calculadora](./Calculadora/README.md) – Calculadora simples em Python com operações básicas.
- [Cifra de César](./Cifra%20de%20Cesar/README.md) – Implementação da cifra de César para cifrar textos.
- [Dia 1 – Automações de Tarefa](./Dia%201%20Projeto%201%20Automa%C3%A7%C3%B5es%20de%20Tarefa/README.md) – Scripts de automação de tarefas do dia a dia.
- [Dia 2 – Analisando Dados com Python](./Dia%202%20Projeto%202%20Analisando%20Dados%20com%20Python/README.md) – Projeto de análise de dados usando Python e Jupyter.
- [Dia 3 – Inteligência Artificial e Previsões](./Dia%203%20Projeto%203%20Intelig%C3%AAncia%20Artificial%20e%20Previs%C3%B5es/README.md) – Modelos de previsão e IA com Python.
- [Gerador de Resultados – Pedra, Papel e Tesoura](./Gerador%20de%20Resultados%20pedra%20papel%20tesoura/README.md) – Simulador de resultados para o jogo pedra, papel e tesoura.
Template único para cada pasta de projeto
Use este modelo como base para todos os projetos (Calculadora, Dia 1, Dia 2, etc.), só ajustando os trechos em itálico:

text
# Nome do projeto

Descrição curta do que o projeto faz e qual problema resolve.  
Exemplo: *Calculadora em Python com operações básicas de soma, subtração, multiplicação e divisão via linha de comando.*

## Objetivo do projeto

- *Ex.: Praticar lógica de programação e operações matemáticas básicas.*
- *Ex.: Trabalhar com automação de tarefas do dia a dia.*
- *Ex.: Explorar análise de dados com Python e Jupyter Notebook.*

## Tecnologias utilizadas

- Python 3
- (Opcional) Jupyter Notebook
- Bibliotecas específicas do projeto (por exemplo: `pandas`, `numpy`, `matplotlib`, `scikit-learn`, etc.)

## Estrutura do projeto

Descreva rapidamente a organização dos arquivos.  
Exemplo genérico:

```text
Nome do Projeto/
├── main.py                # Arquivo principal do projeto
├── notebooks/             # Notebooks Jupyter (se houver)
├── dados/                 # Arquivos de dados usados no projeto
└── README.md              # Documentação deste projeto
Ajuste os nomes de arquivo/pastas para o que existe em cada projeto.

Como executar
Clonar o repositório (se ainda não clonou):

bash
git clone https://github.com/wellingt0n-0liveira/python_projetos.git
cd python_projetos/"Nome da Pasta do Projeto"
(Opcional) Criar e ativar um ambiente virtual:

bash
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
# ou
.venv\Scripts\activate      # Windows
Instalar dependências (se houver requirements.txt):

bash
pip install -r requirements.txt
Executar o projeto:

bash
python main.py
# ou o nome real do arquivo principal, ex.: python calculadora.py
Se for notebook:

bash
jupyter notebook
# abrir o .ipynb correspondente
Exemplo de uso
Explique como usar, de forma rápida:

Para projetos de CLI: quais opções o usuário informa, como é a interação.

Para notebooks: quais células executar e o que o usuário vai ver de resultado.

Para scripts de automação: que tarefa é automatizada e o que é gerado (arquivo, relatório, e-mail etc.).

Exemplo (Calculadora):

text
Escolha a operação:
1 - Soma
2 - Subtração
3 - Multiplicação
4 - Divisão
Digite sua opção: 1
Digite o primeiro número: 10
Digite o segundo número: 5
Resultado: 15
Aprendizados e pontos de destaque
Principais conceitos praticados (ex.: estruturas de controle, funções, manipulação de arquivos, automação de tarefas, análise de dados).

O que você considera mais importante neste projeto pensando em mercado (ex.: automação de rotina, leitura de CSV, consumo de API, etc.).

Possíveis melhorias futuras
Exemplos:

Adicionar testes automatizados.

Criar interface gráfica ou API.

Tornar o código mais genérico/reutilizável.

Integrar com banco de dados ou outro serviço.

text

## Como isso ajuda seu portfólio

- Mostra organização e padrão entre projetos, o que passa maturidade profissional.[1]
- Recrutador consegue navegar fácil: raiz -> projeto -> README -> entender objetivo, stack e como rodar.[1]

Se quiser, no próximo passo posso escrever um README concreto para mais um dos seus projetos (por exemplo, a **Calculadora** ou o **Gerador de Resultados pedra papel tesoura**) já no formato acima, usando o que realmente existe no código.

