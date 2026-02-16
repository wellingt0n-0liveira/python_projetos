# Dia 1 – Projeto 1: Automações de Tarefa

Este projeto demonstra uma automação de tarefas em ambiente gráfico usando Python, `pyautogui` e uma base de dados em CSV para cadastrar produtos em um sistema web de forma automática.

## Objetivo do projeto

- Automatizar uma rotina repetitiva de cadastro de produtos em um sistema online.
- Praticar automação de interface gráfica (GUI) com `pyautogui`.
- Ler dados de uma planilha (`CSV`) com `pandas` e integrá-los a um fluxo automatizado.

## Tecnologias utilizadas

- Python 3
- [pyautogui](https://pyautogui.readthedocs.io/) para automação de mouse e teclado. [page:7]
- [pandas](https://pandas.pydata.org/) para leitura da base de produtos (`produtos.csv`). [page:7]
- Navegador (Firefox, conforme o script está hoje). [page:7]

## Estrutura do projeto

```text
Dia 1 Projeto 1 Automações de Tarefa/
├── exercicio01.py   # Script principal de automação: abre navegador, faz login e cadastra produtos
├── pega_posicao.py  # Script auxiliar para capturar coordenadas do mouse na tela
├── produtos.csv     # Base de produtos a ser cadastrada no sistema
└── README.md        # Documentação deste projeto
exercicio01.py: contém o fluxo completo da automação (abrir navegador, acessar URL, login e cadastro em loop). [page:7]

pega_posicao.py: ajuda a descobrir as coordenadas x,y de elementos na tela para uso com pyautogui.click. [page:8]

produtos.csv: tabela com as colunas codigo, marca, tipo, categoria, preco_unitario, custo e obs. [page:7]

Como a automação funciona
O script exercicio01.py executa o seguinte passo a passo: [page:7]

Configura o pyautogui.PAUSE para definir um tempo de espera entre ações.

Abre o menu iniciar, digita “firefox” e abre o navegador.

Acessa a URL do sistema de login (https://dlp.hashtagtreinamentos.com/python/intensivao/login).

Preenche o e-mail e a senha nos campos corretos e faz login.

Lê a base produtos.csv com pandas.

Para cada linha da tabela:

Acessa o menu de produtos.

Preenche código, marca, tipo, categoria, preço unitário, custo e observações.

Envia o formulário e faz scroll para o topo para preparar o próximo cadastro.

A coluna obs só é preenchida quando o valor não é nulo, usando pd.notna(obs). [page:7]

Pré-requisitos
Python 3 instalado.

Bibliotecas Python:

bash
pip install pyautogui pandas
Navegador compatível (no script atual é usado “firefox”).

Sistema operacional com interface gráfica (Windows/Linux com ambiente gráfico).

Importante: as coordenadas de tela usadas no script (pyautogui.click(x=..., y=...)) são específicas da sua resolução/ambiente.
Em outra máquina ou resolução, você deve recalibrar esses valores usando pega_posicao.py. [page:7][page:8]

Como executar
Clonar o repositório (se ainda não clonou):

bash
git clone https://github.com/wellingt0n-0liveira/python_projetos.git
cd "python_projetos/Dia 1 Projeto 1 Automações de Tarefa"
(Opcional) Criar e ativar um ambiente virtual:

bash
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
# ou
.venv\Scripts\activate      # Windows
Instalar dependências:

bash
pip install pyautogui pandas
Ajustar (se necessário) as credenciais de login e a URL no arquivo exercicio01.py. [page:7]

Ajustar as coordenadas de tela, se estiver em outro ambiente:

bash
python pega_posicao.py
# Você terá 5 segundos para posicionar o mouse; o script imprime a posição atual.
Use os valores impressos para atualizar os pyautogui.click(x=..., y=...) em exercicio01.py. [page:8]

Executar a automação:

bash
python exercicio01.py
# ou
python3 exercicio01.py
Não mexa no mouse/teclado durante a execução, para não interferir nas ações da automação.

Exemplo de fluxo (alto nível)
Navegador é aberto automaticamente. [page:7]

Sistema de login é acessado e preenchido.

Para cada linha de produtos.csv, um novo produto é cadastrado no sistema, como se um usuário estivesse digitando manualmente, porém de forma automatizada. [page:7]

Aprendizados e pontos de destaque
Automação de tarefas repetitivas em sistemas web sem API usando GUI automation.

Integração entre dados de planilha (CSV) e um fluxo automatizado com pyautogui. [page:7]

Uso de laços (for linha in tabela.index) para iterar registros e preencher formulários. [page:7]

Boas práticas iniciais: pausas entre ações, checagem de NaN com pd.notna para evitar erros com campos vazios. [page:7]

Possíveis melhorias futuras
Parametrizar URL, credenciais e caminho do CSV via arquivo de configuração ou variáveis de ambiente.

Melhorar o tratamento de exceções (por exemplo, se o site demorar a carregar ou mudar layout).

Incluir logs estruturados da automação (quais itens foram cadastrados com sucesso, erros, etc.).

Evoluir para uma abordagem usando API (se disponível), removendo a dependência de automação de interface gráfica.