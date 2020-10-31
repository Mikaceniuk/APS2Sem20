import requests
import json
import xlsxwriter

def fetchAndCreatePartidoData():
    print('Buscando dados dos partidos...')

    #Fetching
    resp = requests.get('https://dadosabertos.camara.leg.br/api/v2/partidos?itens=1000')
    partidosDct = json.loads(resp.text)
    partidosLst = partidosDct.get('dados')

    #Pega mais info do partido
    #e adiciona na list
    for i in range(len(partidosLst)):
        resp = requests.get(partidosLst[i].get('uri'))
        partidoInfoDct = json.loads(resp.text)

        partidosLst[i]['lider'] = partidoInfoDct.get('dados').get('status').get('lider').get('nome')
        partidosLst[i]['uf'] = partidoInfoDct.get('dados').get('status').get('lider').get('uf')
        partidosLst[i]['totalMembros'] = partidoInfoDct.get('dados').get('status').get('totalMembros')

    print('Criando arquivo Excel...')
    #Creating
    workbook = xlsxwriter.Workbook('partidos.xlsx')
    worksheet = workbook.add_worksheet()

    worksheet.write('A1', 'sigla')
    worksheet.write('B1', 'nome')
    worksheet.write('C1', 'lider')
    worksheet.write('D1', 'uf')
    worksheet.write('E1', 'totalMembros')

    for i in range(len(partidosLst)):
        worksheet.write('A{}'.format(i + 2), partidosLst[i].get('sigla'))
        worksheet.write('B{}'.format(i + 2), partidosLst[i].get('nome'))
        worksheet.write('C{}'.format(i + 2), partidosLst[i].get('lider'))
        worksheet.write('D{}'.format(i + 2), partidosLst[i].get('uf'))
        worksheet.write('E{}'.format(i + 2), partidosLst[i].get('totalMembros'))

    workbook.close()
    print('Criado arquivo excel "partidos.xlsx" com sucesso!')

def fetchAndCreateDeputadosData():
    print('Buscando dados dos deputados...')

    #Fetching
    resp = requests.get('https://dadosabertos.camara.leg.br/api/v2/deputados?itens=1000')
    deputadosDct = json.loads(resp.text)
    deputadosLst = deputadosDct.get('dados')

    #Pega mais info do partido
    #e adiciona na list
    for i in range(len(deputadosLst)):
        resp = requests.get(deputadosLst[i].get('uri'))
        deputadosInfoDct = json.loads(resp.text)

        deputadosLst[i]['nome'] = deputadosInfoDct.get('dados').get('nomeCivil')
        deputadosLst[i]['cpf'] = deputadosInfoDct.get('dados').get('cpf')
        deputadosLst[i]['email'] = deputadosInfoDct.get('dados').get('email')
        deputadosLst[i]['sexo'] = deputadosInfoDct.get('dados').get('sexo')
        deputadosLst[i]['dataNascimento'] = deputadosInfoDct.get('dados').get('dataNascimento')
        deputadosLst[i]['dataFalescimento'] = deputadosInfoDct.get('dados').get('dataFalecimento')
        deputadosLst[i]['escolaridade'] = deputadosInfoDct.get('dados').get('escolaridade')

    print('Criando arquivo Excel...')
    #Creating
    workbook = xlsxwriter.Workbook('deputados.xlsx')
    worksheet = workbook.add_worksheet()

    worksheet.write('A1', 'nomeCivil')
    worksheet.write('B1', 'cpf')
    worksheet.write('C1', 'email')
    worksheet.write('D1', 'sexo')
    worksheet.write('E1', 'dataNascimento')
    worksheet.write('F1', 'dataFalescimento')
    worksheet.write('G1', 'escolaridade')
    worksheet.write('H1', 'siglaPartido')
    worksheet.write('I1', 'siglaUf')
    worksheet.write('J1', 'urlFoto')

    for i in range(len(deputadosLst)):
        worksheet.write('A{}'.format(i + 2), deputadosLst[i].get('nome'))
        worksheet.write('B{}'.format(i + 2), deputadosLst[i].get('cpf'))
        worksheet.write('C{}'.format(i + 2), deputadosLst[i].get('email'))
        worksheet.write('D{}'.format(i + 2), deputadosLst[i].get('sexo'))
        worksheet.write('E{}'.format(i + 2), deputadosLst[i].get('dataNascimento'))
        worksheet.write('F{}'.format(i + 2), deputadosLst[i].get('dataFalescimento'))
        worksheet.write('G{}'.format(i + 2), deputadosLst[i].get('escolaridade'))
        worksheet.write('H{}'.format(i + 2), deputadosLst[i].get('siglaPartido'))
        worksheet.write('I{}'.format(i + 2), deputadosLst[i].get('siglaUf'))
        worksheet.write('J{}'.format(i + 2), deputadosLst[i].get('urlFoto'))

    workbook.close()
    print('Criado arquivo excel "deputados.xlsx" com sucesso!')