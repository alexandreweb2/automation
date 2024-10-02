valor = valor.replace("-", "", 1)
if "." in valor:
    valorD = valor.split('.')[0]
    valorF = valor.split('.')[1]
    if len(valorF) >= 3 :
        valorX = valorD.strip() + valorF.strip()
        print('deu 3',valorX)
    else :
        valorX = valorD.strip() + valorF.strip() + "0"
        print('deu outra coisa',valorX)
else :
    valorX = valor.strip() + "00"
#with open('controllers/debit.py') as f:
#    exec(f.read())
with open('data/out.csv', 'r', encoding='utf-8') as arquivo2:
    for outline in arquivo2:
        type = outline.split(',')[0]
        bank = outline.split(',')[1]
        description = outline.split(',')[2]
        flat = outline.split(',')[3]
        found = 0
        if descricao == bank:
            with open('data/find.csv', 'a', encoding='utf-8', newline='') as find_file:
                find_file.write(f'{linha}')
            sleep(4)
            pag.click(665,585,duration=3)
            sleep(6)
            #pag.click(1081,869,duration=3)
            #sleep(4)
            #pag.write('joao pessoa - jardim')
            #pag.typewrite(['enter'])
            #sleep(2)
            pag.click(1050,1182,duration=3)
            sleep(2)
            pag.write(flat)       #plano de contas
            sleep(0.5)
            pag.typewrite(['enter'])
            sleep(0.5)
            pag.click(1431,1549,duration=0.5)
            sleep(0.5)
            pag.write(description)
            pag.click(1066,1665,duration=0.5)
            sleep(1)
            pag.write(dataDep)
            pag.click(639,1534,duration=0.5)
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
            pag.press('down')
            pag.press('down')
            pag.press('down')
            pag.click(1065,608,duration=0.5)
            pag.write(valorX)
            sleep(1)
            pag.click(1047,1397,duration=0.5)
            sleep(5)
            pag.click(639,1534,duration=3)
            #if pixel_color == (102, 187, 106):
            pag.click(1442,314,duration=2)
            sleep(10)
            pag.click(639,1534,duration=3)
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
            pag.press('down')
            pag.press('down')
            pag.press('down')
            sleep(2)
            pag.click(1065,608,duration=2)
            pag.click(1893,1284,duration=2)
            pag.click(1034,427,duration=0.1)
            pag.click(1034,427,duration=0.1)
            pag.click(1034,427,duration=0.1)
            pag.write(dataDep)
            pag.click(979,561,duration=1)
            pag.write('PIX')
            pag.click(1867,564,duration=1)
            pag.write('0000')
            pag.click(1761,698,duration=1)
            pag.write('CORA')
            pag.click(2148,902,duration=1)
            #if pixel_color2 == (165, 220, 134):
            pag.click(1367,1219,duration=1)
            pag.click(673,1189,duration=1)
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
            pag.click(865,491,duration=1)
            sleep(4)
            #else:
            #with open('data/not_found.csv', 'a', encoding='utf-8', newline='') as not_found_file:
            #   not_found_file.write(f'Não deu baixa: {linha}')
            #else:
            #   with open('data/not_found.csv', 'a', encoding='utf-8', newline='') as not_found_file:
            #      not_found_file.write(f'Não lançou: {linha}')
            found = 1
            break
    if found == 0:
        with open('data/not_found.csv', 'a', encoding='utf-8', newline='') as not_found_file:
            not_found_file.write(f'{linha}')