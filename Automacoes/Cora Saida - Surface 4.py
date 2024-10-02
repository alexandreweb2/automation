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
sleep(2)
pag.click(1753,108,duration=3)
pag.write('https://www.verbodavida.info/apps/index.php')
pag.typewrite(['enter'])
sleep(2)
pag.click(1534,827,duration=3)
sleep(2)
pag.click(587,768,duration=3)
#pag.click(1625,758,duration=3)#Aqui é se for a conta alexandrefilho@verbodavida.com
sleep(5)
pag.click(1407,612,duration=3)
sleep(3)

descricoes = {
    "COMERCIAL DE TINTAS TAMBAU LTDA":"TINTAS PARA PINTURA DE IGREJA",
    "RA COMERCIO DE INFORMATICA E INSTRUMENTOS MUSICAIS LTDA":"REPARO DE EQUIPAMENTO",
    "Darf/darf-simples 0385":"IMPOSTO SOBRE TRANSFERENCIA FINANCEIRA",
    "Cora Scd Sa":"CALICES DA SANTA CEIA",
    "Seicon Servicos De Elevadores Eireli":"MANUTENCAO PREVENTIVA DO ELEVADOR",
    "Af Comercio Varejista De Embalagens E Sa":"DESCARTAVEIS PARA IGREJA",
    "JOSE DANIEL SILVA PEREIRA":"PAGAMENTO DO PINTOR DA IGREJA",
    "Maple Serv Apoio Ltda":"SERVICO PRESTADO DE SEGURANCA ELETRONICA",
    "Energisaparaiba Diste Enesa":"ENERGIA",
    "WMMM ADMINISTRACAO E PARTICIPACOES S/A":"ALUGUEL TEMPLO",
    "Cagepa Recebimento":"AGUA",
    "Vancouver Servicos M E Ltda":"SERVICO PRESTADO DE SEGURANCA ELETRONICA",
    "PG SOLUCOES DIGITAIS":"-84.48",
    "Municipio De Joao Pessoa":"TRIBUTOS FEDERAIS",
    "JOAO WELLINGTON FERREIRA DE OLIVEIRA":"AJUDA DE CUSTO - JOAO WELLINGTON FERREIRA DE OLIVEIRA",
    "Brisanet":"MENSALIDADE INTERNET",
    "Jussara Pereira da Silva":"OFERTA MISSIONARIA - PARA JUSSARA PEREIRA",
    "Jane Eyre Marinho Dantas Figueirêdo Fernandes":"OFERTA MISSIONARIA - ALEXANDRE FERNANDES E JANE EYRE",
    "ERNANI MOREIRA FRANCO NETO":"OFERTA MISSIONARIA - ERNANI MOREIRA FRANCO NETO",
    "Tributos Federais - Fgts Grf Convenio 0179":"TRIBUTOS FEDERAIS",
    "GIACOME TRAVASSOS DUARTE JACOME":"PRÉ-BENDA DO PASTOR GIACOME TRAVASSOS",
    "JOAO WELLINGTON FERREIRA DE OLIVEIRA":"SALÁRIO - JOAO WELLINGTON",
    "BRENNA SANTOS DE ANDRADE":"REFERENTE SERVICOS CONTÁBEIS",
    "Igreja Evangélica Verbo da Vida Praia":"-3000",
}

categories = {
    "TINTAS PARA PINTURA DE IGREJA":"manutencao e conservacao de bens imoveis",
    "REPARO DE EQUIPAMENTO":"MANUTENCAO E CONSERVACAO DE BENS",
    "IMPOSTO SOBRE TRANSFERENCIA FINANCEIRA":"OUTRAS DESPESAS DE IMPOSTOS",
    "CALICES DA SANTA CEIA":"SANTA CEIA",
    "MANUTENCAO PREVENTIVA DO ELEVADOR":"MANUTENCAO E CONSERVACAO",
    "DESCARTAVEIS PARA IGREJA":"MATERIAL DE CONSUMO",
    "PAGAMENTO DO PINTOR DA IGREJA":"SERVICOS PRESTADOS - PESSOA FISICA",
    "SERVICO PRESTADO DE SEGURANCA ELETRONICA":"MONITORAMENTO E SEGURANCA",
    "ENERGIA":"ENERGIA ELÉTRICA",
    "ALUGUEL TEMPLO":"ALUGUEL",
    "ÁGUA":"ÁGUA E ESGOTO",
    "SERVICO PRESTADO DE SEGURANCA ELETRONICA":"MONITORAMENTO E SEGURANCA",
    "TRIBUTOS FEDERAIS":"IMPOSTOS E CONTRIBUICÕES FEDERAIS",
    "AJUDA DE CUSTO - JOAO WELLINGTON FERREIRA DE OLIVEIRA":"AJUDA DE CUSTO",
    "MENSALIDADE INTERNET":"SERVICOS PRESTADOS - PESSOA JU",
    "OFERTA MISSIONARIA - PARA JUSSARA PEREIRA":"OFERTAS PARA MISSIONÁRIOS",
    "OFERTA MISSIONARIA - ALEXANDRE FERNANDES E JANE EYRE":"OFERTAS PARA MISSIONÁRIOS",
    "OFERTA MISSIONARIA - ERNANI MOREIRA FRANCO NETO":"OFERTAS PARA MISSIONÁRIOS",
    "TRIBUTOS FEDERAIS":"IMPOSTOS E CONTRIBUICÕES FEDERAIS",
    "PRÉ-BENDA DO PASTOR GIACOME TRAVASSOS":"OFERTAS PARA MINISTROS",
    "SALÁRIO - JOAO WELLINGTON":"SALÁRIOS E ORDENADOS",
    "REFERENTE SERVICOS CONTÁBEIS":"HONORÁRIOS CONTÁBEIS",
}

with open('FAZER/Cora Out.csv', 'r') as arquivo_entrada, open('registro.csv', 'w') as arquivo_saida,open('logs/log.csv', 'w') as log:
    for linha in arquivo_entrada:
        sleep(4)
        pag.click(665,585,duration=3)
        print(linha)
        dataDep = linha.split(',')[0]
        mode = linha.split(',')[1]
        tipo = linha.split(',')[2]
        descricao = linha.split(',')[3]
        valor = linha.split(',')[4]
        credito = "Transf Pix recebida"
        deposito = "Pagamento recebido"
        debito = "Transf Pix enviada"
        if mode == debito:
            if descricao in descricoes:
                valor = valor.replace("-", "", 1)
                if "." in valor:
                    valorD = valor.split('.')[0]
                    valorF = valor.split('.')[1]
                    if len(valorF) == 2 :
                        valorX = valorD.strip() + valorF.strip()
                    else :
                        valorX = valorD.strip() + valorF.strip() + "0"
                    print(len(valorF))
                else :
                    valorX = valor.strip() + "00"
                print(len(valorX))
                texto = descricoes[descricao]
                categories = categories[texto]
                # Remova o primeiro "-" de valorX.
                valorX = valorX.replace("-", "", 1)     
                sleep(6)
                pag.click(1095,847,duration=4)
                sleep(2)
                pag.write('joao pessoa - jardim')
                sleep(1)
                pag.typewrite(['enter'])
                sleep(1)
                pag.click(1188,1177,duration=3)
                sleep(2)
                pag.write(categories)
                sleep(2)
                pag.typewrite(['enter'])
                pag.click(1074,1554,duration=1)
                pag.write(texto)
                pag.click(1103,1661,duration=1)
                pag.write(dataDep)
                sleep(3)
                pag.click(644,1304,duration=1)
                sleep(3)
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
                sleep(1)
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
                pag.click(1129,608,duration=3)
                pag.write(valorX)
                sleep(1)
                pag.click(1043,1405,duration=3)
                sleep(5)
                pag.click(1449,315,duration=3)
                sleep(4)
                pag.click(1449,315,duration=3)
                sleep(4)
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
                sleep(1)
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
                pag.click(1917,1292,duration=1)
                pag.click(992,429,duration=1)
                pag.hotkey('ctrl', 'a')
                pag.press('delete')
                pag.write(dataDep)
                pag.press('tab')
                pag.click(920,563,duration=1)
                pag.write('PIX')
                pag.typewrite(['enter'])
                pag.click(1835,562,duration=1)
                pag.write('0000')
                pag.click(1763,698,duration=1)
                pag.write('CORA')
                pag.typewrite(['enter'])
                pag.click(2139,896,duration=1)
                pag.click(665,914,duration=1)
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
                pag.press('up')
                pag.press('up')
                pag.press('up')
                pag.press('up')
                pag.press('up')
                pag.press('up')
                pag.press('up')
                pag.press('up')
                pag.click(869,488,duration=1)                           
            else:
                # Se a descriçAo nAo estiver no dicionário, escreva a descriçAo em um arquivo de log.
                #with open("log.txt", "a") as arquivo_log:
                #    arquivo_log.write(f"DescriçAo nAo encontrada: {descricao}\n")
                print(linha, "- Não encontrada")
        if mode == credito or mode == deposito:
            print(linha, "Credito")

