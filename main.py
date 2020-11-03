import converterInfo
import buscarInfo
import os
from time import sleep
from openpyxl import load_workbook

print('Verificando dados...')
sleep(2)

try:
    converterInfo.converterExcelParaTxt('partidos')
except OSError:
    print('Arquivo partidos não foi encontrado!')
    sleep(1)
    buscarInfo.fetchAndCreatePartidoData()

try:
    converterInfo.converterExcelParaTxt('deputados')
except OSError:
    print('Arquivo deputados não foi encontrado!')
    sleep(1)
    buscarInfo.fetchAndCreateDeputadosData()

sleep(1)
os.system('cls')

opt = int(input('''Deseja converter quais arquivos para TXT?
 [1] Partidos
 [2] Deputados
 [3] Ambos
'''))

if opt == 1:
    print('Você selecionou converter arquivo Partidos!')
    converterInfo.converterExcelParaTxt('partidos')
elif opt == 2:
    print('Você selecionou converter arquivo Deputados!')
    converterInfo.converterExcelParaTxt('deputados')
elif opt == 3:
    print('Você selecionou converter os dois arquivos!')
    converterInfo.converterExcelParaTxt('partidos')
    converterInfo.converterExcelParaTxt('deputados')
else:
    print('Opção inválida, tente novamente!')