import pandas as pd
import numpy as np
import os
 
tabela_total = pd.DataFrame()
lista_arquivos = os.listdir("teste_planilhas_chip")
lst_ano = []
valores_csv = []

#lista de todos os anos
for all_values in range(len(lista_arquivos)):
    lst_ano.append(int(lista_arquivos[all_values][:4]))
    lst_ano = list(set(lst_ano))

while True:
    data_ou_periodo = input('Data/Periodo (d/p)')
    if data_ou_periodo == 'd':
        try:
            mes = input('Insira um mês: \n')
            ano = input('Insira um ano: \n')
            if ano == '':
                ano = lst_ano[0]
            periodo_total = pd.date_range(start = f'01/{mes}/{ano}', end = f'31/12/{lst_ano[-1]}')
            periodo_total = periodo_total.strftime("%Y%m%d")
            print(periodo_total)
            break

        except ValueError:
            print('\n(!) Erro: data inválida\n')

    
    elif data_ou_periodo == 'p':
        try:
            periodo_primeiro = input('Insira a primeira data do período (formato mes/dia/ano)')
            periodo_segundo = input('Insira a segunda data do período (formato mes/dia/ano)')
            periodo_total = pd.date_range(start = periodo_primeiro, end = periodo_segundo)
            periodo_total = periodo_total.strftime("%Y%m%d")

            print(periodo_total)
            break
        except ValueError:
            print('\n(!) Erro: período inválido\n')
    else:
        print('(!) Comando inválido')
        
for arquivo in lista_arquivos:
    if arquivo[:8] in periodo_total:
        tabela = pd.DataFrame(pd.read_csv(f"teste_planilhas_chip\{arquivo}"))
        valores_csv.append(tabela)


tabela_total = pd.concat(valores_csv[i] for i in range(len(valores_csv)))

if not os.path.isdir(f'{periodo_total[0]}-{periodo_total[-1]}'):
    os.mkdir(f'{periodo_total[0]}-{periodo_total[-1]}')
tabela_total.to_csv(f'{periodo_total[0]}-{periodo_total[-1]}\\{periodo_total[0]}-{periodo_total[-1]}.csv')

print(f'\nCriado o arquivo {periodo_total[0]}-{periodo_total[-1]}.csv')
