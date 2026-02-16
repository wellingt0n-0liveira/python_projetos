# Dia 3 – Projeto 3: Inteligência Artificial e Previsões

Este projeto utiliza técnicas de Inteligência Artificial / Machine Learning em Python para treinar um modelo de previsão a partir da base `clientes.csv` e aplicar esse modelo em uma nova base `novos_clientes.csv`, gerando previsões para apoiar decisões de negócio.

## Objetivo do projeto

- Praticar o fluxo completo de um projeto de Machine Learning (carregar dados, treinar modelo, avaliar e prever).
- Utilizar um notebook Jupyter para documentar o passo a passo da solução.
- Gerar previsões para um conjunto de novos clientes, simulando um cenário real de uso de modelo em produção.

## Tecnologias utilizadas

- Python 3
- pandas
- scikit-learn (ou biblioteca similar de ML)
- Jupyter Notebook
- (Opcional) matplotlib / seaborn para visualização

## Estrutura do projeto

```text
Dia 3 Projeto 3 Inteligência Artificial e Previsões/
├── clientes.csv           # Base de dados usada para treino/validação do modelo
├── novos_clientes.csv     # Base de novos clientes para os quais serão feitas previsões
├── inicial.ipynb          # Notebook Jupyter com todo o fluxo de IA/ML e previsões
└── README.md              # Documentação deste projeto
clientes.csv: contém o histórico de clientes e as variáveis alvo (por exemplo, churn, score, compra, etc.), usado para treinar o modelo.

novos_clientes.csv: contém apenas as features dos novos clientes, para os quais o modelo irá gerar previsões.

inicial.ipynb: centraliza o código, os testes e as explicações do processo de Machine Learning.

Como executar o projeto
Clonar o repositório (se ainda não clonou):

bash
git clone https://github.com/wellingt0n-0liveira/python_projetos.git
cd "python_projetos/Dia 3 Projeto 3 Inteligência Artificial e Previsões"
(Opcional) Criar e ativar um ambiente virtual:

bash
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
# ou
.venv\Scripts\activate      # Windows
Instalar dependências principais:

bash
pip install pandas scikit-learn jupyter matplotlib seaborn
Iniciar o Jupyter Notebook:

bash
jupyter notebook
No navegador, abrir o arquivo inicial.ipynb e executar as células em ordem (Kernel → Restart & Run All ou rodar uma a uma).

Fluxo típico da solução em IA/ML
O notebook inicial.ipynb normalmente segue um pipeline como:

Carregar e explorar a base clientes.csv:

Ver estrutura, tipos de dados, valores ausentes.

Tratar e preparar os dados:

Selecionar features relevantes.

Tratar nulos, normalizar/transformar colunas, codificar variáveis categóricas, se necessário.

Dividir os dados em treino e teste.

Treinar um modelo de Machine Learning (por exemplo, regressão, árvore de decisão, random forest, etc.).

Avaliar o modelo em dados de teste (métricas como acurácia, precisão, recall, RMSE, etc., dependendo do problema).

Carregar novos_clientes.csv e aplicar o modelo treinado para gerar previsões.

(Opcional) Salvar as previsões para arquivo ou exibi-las em tabelas/gráficos dentro do notebook.

Adapte esta descrição para refletir exatamente o que o seu notebook faz.

Exemplo de resultados esperados
Alguns tipos de saída que esse projeto pode gerar:

Tabela com clientes e a probabilidade de cancelamento ou classificação em algum grupo.

Gráficos comparando distribuições entre clientes que realizaram determinado evento e os que não realizaram.

Arquivo com previsões (ex.: nova coluna "previsao" associada a novos_clientes.csv).

Exemplo ilustrativo de saída em tabela:

text
id_cliente, probabilidade_cancelamento
101, 0.83
102, 0.12
103, 0.45
...
Aprendizados e pontos de destaque
Aplicação prática do ciclo de Machine Learning: preparação de dados, treino, avaliação e previsão para novos exemplos.

Uso de pandas e scikit-learn em um cenário de negócio (clientes, cancelamento, score ou similar).

Organização da análise e do modelo em um notebook Jupyter, formato comum em projetos de Data Science e fácil de mostrar em portfólio.

Possíveis melhorias futuras
Testar diferentes algoritmos de modelo e comparar métricas de desempenho.

Implementar validação cruzada e/ou tuning de hiperparâmetros.

Salvar o modelo treinado em disco (por exemplo, com joblib) para reaproveitar em outros scripts.

Construir um script ou API simples que carregue o modelo e receba novos clientes para prever via linha de comando ou HTTP.