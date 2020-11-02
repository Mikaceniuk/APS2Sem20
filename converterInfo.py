from openpyxl import load_workbook

def converterExcelParaTxt(nomeExcel):
    path = '{}.xlsx'.format(nomeExcel)
    wb_obj = load_workbook(path)
    f = open('{}.txt'.format(nomeExcel), 'w+')
    sheet_obj = wb_obj.active

    #Insere os valores
    for row in range(sheet_obj.max_row + 1):
        for column in range(1, sheet_obj.max_column + 1):
            if(row > 0):
                valor = sheet_obj.cell(row = row, column = column).value

                #Cabeçalho
                if(row == 1):
                    if(column != sheet_obj.max_column):
                        f.writelines('{} | '.format(valor))
                    else:
                        f.writelines('{} \n'.format(valor))
                #Data
                elif(row > 1):
                    if(column != sheet_obj.max_column):
                        f.writelines('{} | '.format(valor))
                    else:
                        f.writelines('{} \n'.format(valor))
    f.close()