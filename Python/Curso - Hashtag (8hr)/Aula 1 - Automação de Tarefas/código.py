import pyautogui # importação para automações de teclas
import time # importação para o Delay
import pandas # importação para base de dados

pyautogui.PAUSE = 0.5 # delay de 0,5 segundos

pyautogui.press("win") # pressiona a tecla do Windows
pyautogui.write("chrome") # escreve Chrome
pyautogui.press("enter") 
pyautogui.write("https://dlp.hastagtreinamentos.com/python/intensivao/login") # escreve o link escolhido
pyautogui.press("enter")
time.sleep(3) # espere 3 segundos

pyautogui.click(x=649, y=477) # mostra as coordenadas do seu mouse
pyautogui.position # procura aonde seu mouse está

pyautogui.write("pythonimpressionador@gmail.com") # escreve o email escolhido
pyautogui.press("tab") # pula para preencher o próximo campo

pyautogui.write("123456789") # escreve a senha
pyautogui.press("tab")
pyautogui.press("enter") # aperta enter para logar
time.sleep(3)

tabela = pandas.read_csv("produtos.csv") # variável tabela criada para a base de dados csv
print(tabela) # mostra a tabela criada

for linha in tabela.index: # para cada linha da tabela é para ser preenchida baseada no banco
    pyautogui.click(x=613, y=328)
    codigo = "MOLO000251"
    codigo = tabela.loc[linha, "codigo"] # localiza a linha e coluna
    pyautogui.write(codigo)
    
    pyautogui.press("tab")
    marca = "Logitech" # valor da variável
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca) # passa a variável para o parâmetro

    pyautogui.press("tab")
    tipo = "Mouse"
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)

    pyautogui.press("tab")
    categoria = "1"
    categoria = str(tabela.loc[linha, "categoria"]) # str transforma tudo em texto 
    pyautogui.write(categoria)

    pyautogui.press("tab")
    preco_unitario = "25.95"
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)

    pyautogui.press("tab")
    custo = "6.50"
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)

    pyautogui.press("tab")
    obs = ""
    obs = str(tabela.loc[linha, "obs"])
    
    if obs != "nan": # se for diferente de Nan, vai rodar [!= = diferente]
        pyautogui.write(obs)
    
    pyautogui.press("tab")
    pyautogui.press("enter")