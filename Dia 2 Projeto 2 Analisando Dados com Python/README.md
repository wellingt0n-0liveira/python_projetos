# Dia 2 – Projeto 2: Analisando Dados com Python

Este projeto realiza uma análise de dados em Python a partir da base `cancelamento.csv`, com foco em entender padrões e indicadores que podem estar relacionados a cancelamentos (churn) de clientes.

## Objetivo do projeto

- Praticar leitura e tratamento de dados com `pandas`.
- Explorar métricas e insights em cima da base de cancelamentos.
- Utilizar um notebook Jupyter para documentar e visualizar a análise passo a passo.

## Tecnologias utilizadas

- Python 3
- pandas
- Jupyter Notebook
- (Opcional) matplotlib / seaborn para gráficos

## Estrutura do projeto

```text
Dia 2 Projeto 2 Analisando Dados com Python/
├── cancelamento.csv        # Base de dados utilizada na análise
├── inicial.ipynb           # Notebook Jupyter com a análise passo a passo
└── README.md               # Documentação deste projeto
cancelamento.csv: arquivo com os dados de clientes/cancelamentos que serão analisados.

inicial.ipynb: notebook onde a análise é desenvolvida, executada e comentada célula a célula.

Como executar a análise
Clonar o repositório (se ainda não clonou):

bash
git clone https://github.com/wellingt0n-0liveira/python_projetos.git
cd "python_projetos/Dia 2 Projeto 2 Analisando Dados com Python"
(Opcional) Criar e ativar um ambiente virtual:

bash
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
# ou
.venv\Scripts\activate      # Windows
Instalar dependências principais:

bash
pip install pandas jupyter matplotlib seaborn
Iniciar o Jupyter Notebook:

bash
jupyter notebook
No navegador, abrir o arquivo inicial.ipynb e executar as células em ordem (Kernel → Restart & Run All, ou rodando uma a uma).

O que a análise faz (estrutura típica)
A análise em inicial.ipynb geralmente segue um fluxo como: [web:19][web:20][web:24]

Importar bibliotecas (pandas, etc.).

Carregar o arquivo cancelamento.csv em um DataFrame.

Fazer uma visão geral dos dados:

Quantidade de linhas e colunas.

Tipos de dados.

Valores faltantes.

Tratar dados, se necessário (nulos, tipos, duplicidades).

Calcular métricas relevantes, por exemplo:

Quantidade total de clientes.

Taxa de cancelamento.

Cancelamento por categoria (plano, região, tempo de casa, etc.).

(Opcional) Gerar gráficos para visualizar padrões e comparações.

Adapte esta seção conforme o que o seu notebook realmente calcula e exibe.

Exemplo de resultados
Alguns exemplos de saídas que podem ser obtidas e descritas no notebook:

Tabela com a taxa de cancelamento por tipo de plano.

Gráfico de barras com a quantidade de clientes ativos x cancelados.

Métricas resumo, como:

text
Total de clientes: 1.000
Clientes cancelados: 230
Taxa de cancelamento: 23%
Você pode complementar este README depois com prints dos gráficos ou seções do notebook.

Aprendizados e pontos de destaque
Uso de pandas para carregar, explorar e transformar dados de um CSV real. [web:19][web:20]

Prática de análise exploratória de dados (EDA) em inicial.ipynb, com visualização incremental dos resultados. [web:19][web:24]

Organização da análise em um notebook, que é um formato comum em projetos de dados e muito usado em portfólio. [web:25]

Possíveis melhorias futuras
Refatorar partes da análise em funções reutilizáveis (por exemplo, funções para cálculo de métricas e geração de gráficos).

Criar mais visualizações (distribuições, comparações por grupo, séries temporais se houver datas).

Exportar resultados consolidados para um arquivo (CSV/Excel ou relatório).

Conectar essa análise a uma automação (por exemplo, rodar periodicamente e gerar relatórios atualizados).