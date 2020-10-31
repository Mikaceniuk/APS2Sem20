import os
import requests
import json
import xlsxwriter 

os.system('cls')

def fetchAndCreatePartidoData():
    print('Buscando dados...')

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
        del partidosLst[i]['id']
        del partidosLst[i]['uri']

    print('Criando arquivo Excel...')
    #Creating
    workbook = xlsxwriter.Workbook('partidos.xlsx')
    worksheet = workbook.add_worksheet()

    worksheet.write('A1', 'Sigla')
    worksheet.write('B1', 'Nome')
    worksheet.write('C1', 'Lider')
    worksheet.write('D1', 'Uf')
    worksheet.write('E1', 'Total de Membros')

    for i in range(len(partidosLst)):
        worksheet.write('A{}'.format(i + 2), partidosLst[i].get('sigla'))
        worksheet.write('B{}'.format(i + 2), partidosLst[i].get('nome'))
        worksheet.write('C{}'.format(i + 2), partidosLst[i].get('lider'))
        worksheet.write('D{}'.format(i + 2), partidosLst[i].get('uf'))
        worksheet.write('E{}'.format(i + 2), partidosLst[i].get('totalMembros'))

    workbook.close()
    print('Criado arquivo excel "partidos.xlsx" com sucesso!')

fetchAndCreatePartidoData()