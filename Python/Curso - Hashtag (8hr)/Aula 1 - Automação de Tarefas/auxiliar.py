import pyautogui # importação para automações de teclas
import time # importação para o delay
time.sleep(5) # espere 3 segundos
print(pyautogui.position) # mostra aonde o mouse está [coordenadas]
pyautogui.scroll(100) # rolar o scroller do mouse para cima  
pyautogui.scroll(-100) # rolar o scroller do mouse para baixo  