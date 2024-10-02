import pyautogui as pag
import controllers.init as init
from time import sleep

contador = 0
contadorDeposito = 0

init.init()

pixel_color = pag.pixel(1445,316)
pixel_color2 = pag.pixel(1368,775)

with open('process/Cora Set.csv', 'r') as arquivo_entrada:
    for linha in arquivo_entrada:
        with open('data/run.csv', 'a', encoding='utf-8', newline='') as file:
            file.write(f'{linha}')
        sleep(4)
        dataDep = linha.split(',')[0]
        mode = linha.split(',')[1]
        tipo = linha.split(',')[2]
        descricao = linha.split(',')[3]
        valor = linha.split(',')[4]
        credito = "Transf Pix recebida"
        deposito = "Pagamento recebido"
        if mode == credito or mode == deposito:
            print('credit:',linha)
            with open('controllers/credit.py') as f:
               exec(f.read())        
        if tipo != credito:
            print('debit:',linha)
            #with open('controllers/debit.py') as f:
            #   exec(f.read())      