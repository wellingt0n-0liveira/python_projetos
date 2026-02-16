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
