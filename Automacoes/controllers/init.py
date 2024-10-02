import pyautogui as pag
from time import sleep

def init():
    #Abrindo o chrome
    pag.hotkey('win')
    sleep(2)
    pag.write('chrome')
    sleep(2)
    pag.typewrite(['enter'])
    sleep(2)

    #Abrindo o SOMA
    pag.click(1753,108,duration=3)
    pag.write('https://www.verbodavida.info/apps/index.php')
    pag.typewrite(['enter'])

    pag.click(1534,827,duration=5)
    sleep(6)
    pag.click(587,768,duration=5)
    #pag.click(1625,758,duration=3)#Aqui é se for a conta alexandrefilho@verbodavida.com
    sleep(6)
    pag.click(1407,612,duration=5)
    sleep(6)