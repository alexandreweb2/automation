import pyautogui as pag
from time import sleep

contador = 0
contadorDeposito = 0

#Abrindo o chrome
pag.hotkey('win')
sleep(2)
pag.write('chrome')
pag.typewrite(['enter'])
sleep(2)

#Abrindo o SOMA
pag.click(1753,108,duration=3)
pag.write('https://www.verbodavida.info/apps/index.php')
pag.typewrite(['enter'])

pag.click(1534,827,duration=3)
pag.click(587,768,duration=3)

sleep(5)
pag.click(1407,612,duration=3)
sleep(3)

with open('process/BB Set.csv','r') as arquivo:
    for linha in arquivo:
        pag.click(665,585,duration=3)
        print(linha)
        dataDep = linha.split(';')[12]
        dia = dataDep[0:1]
        mes = dataDep[3:4]
        ano = "2024"
        dataDepStract = dataDep[0:5] + ano
        tipo = linha.split(';')[11]
        descricao = linha.split(';')[9]
        valor = linha.split(';')[10]
        credito = "C"
        print(tipo)
        print(dataDepStract)
        if tipo == credito:
            sleep(6)
            pag.click(1095,847,duration=4)
            sleep(2)
            pag.write('joao pessoa - jardim')
            sleep(1)
            pag.typewrite(['enter'])
            sleep(1)
            pag.click(1233,987,duration=3)
            sleep(1)
            pag.click(1197,1088,duration=3)
            sleep(2)
            pag.write('doa')
            sleep(2)
            pag.typewrite(['enter'])
            pag.click(1078,1452,duration=1)
            pag.write('Dizimo e oferta')
            pag.click(1189,1559,duration=1)
            pag.write(dataDepStract)
            pag.click(1204,1674,duration=1)
            pag.write(valor)
            sleep(1)
            pag.click(655,1480,duration=1)
            pag.press('down')
            pag.press('down')
            pag.press('down')
            pag.press('down')
            pag.press('down')
            pag.press('down')
            pag.press('down')
            pag.press('down')
            pag.press('down')
            pag.press('down')
            pag.press('down')
            pag.press('down')
            pag.press('down')
            pag.press('down')
            pag.click(1141,951,duration=1)
            sleep(0.5)
            pag.write('PIX')
            sleep(0.5)
            pag.typewrite(['enter'])
            pag.click(1108,1202,duration=2)
            pag.write('BANCO')
            sleep(1.5)
            pag.typewrite(['enter'])
            pag.click(1050,1547,duration=2)
            pag.press('down')
            pag.press('down')
            pag.press('down')
            pag.press('down')
            pag.press('down')
            pag.press('down')
            pag.press('down')
            pag.press('down')
            pag.press('down')
            pag.press('down')
            pag.press('down')
            pag.click(628,1292,duration=1)
            sleep(4)
            pag.press('up')
            pag.press('up')
            pag.press('up')
            pag.press('up')
            pag.press('up')
            pag.press('up')
            pag.press('up')
            pag.press('up')
            pag.press('up')
            pag.press('up')
            pag.press('up')
            pag.press('up')
            pag.press('up')
            pag.press('up')
            pag.press('up')
            pag.press('up')
            pag.press('up')