# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa 
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui
import time

# pegar da tabela o valor do campo que a gente quer preencher
 
# preencher o campo
  
# passar para o proximo campo

# preencher o campo

# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas
pyautogui.PAUSE = 0.5  # tempo de espera entre cada ação do pyautogui

# abrir o navegador (LibreWolf)
pyautogui.press("win")
pyautogui.write("firefox")
pyautogui.press("enter")
time.sleep(2)  # esperar o navegador abrir

# entrar no link
pyautogui.click(x=1152, y=72)  # coordenadas da barra de endereço
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(4)  # esperar a página carregar

# Passo 2: Fazer login
# selecionar o campo de email
pyautogui.click(x=1113, y=431)  # coordenadas do campo de email
# escrever o seu email
pyautogui.write("123@gmail.com")
# selecionar o campo de senha
pyautogui.press("tab")
# escrever a sua senha
pyautogui.write("123456")
# clicar no botão de loguin
pyautogui.click(x=1041, y=604)  # coordenadas do botão de login
time.sleep(3)  # esperar a página carregar

# Passo 3: Importar a base de produtos pra cadastrar
import pandas as pd

tabela = pd.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:
    # Passo 4: Cadastrar um produto
    # codigo
    pyautogui.click(x=745, y=317)  # coordenadas do menu de produtos
    codigo = tabela.loc[linha, "codigo"] # pegar exatamente o nome da coluna
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    # Marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    # Tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    # Categoria
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    # Preço Unitario
    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")

    #Custo
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    # Obs
    obs = tabela.loc[linha, "obs"]
    # if obs == obs:  # checar se o valor não é nan (usando a propriedade de que nan != nan) pouco usado
    # if not pd.isna(obs): # checar se o valor não é nan (mais usado e correto)
    if pd.notna(obs):  # checar se o valor não é nan ( usado e correto)
        pyautogui.write(str(obs))
    pyautogui.press("tab") # passar para o botão enviar

    pyautogui.press("enter")  # clicar no botão enviar
    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)  # scroll para cima
    
# Passo 5: Repetir o processo de cadastro até o fim