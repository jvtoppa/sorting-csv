import pandas as pd
import numpy as np
import os
 
tabela_total = pd.DataFrame()
lista_arquivos = os.listdir("teste_planilhas_chip")
lista_ano = []
valores_csv = []


for all_values in range(len(lista_arquivos)):
    lista_ano.append(int(lista_arquivos[all_values][:4]))
    lista_ano = list(set(lista_ano))

#SEPARADOR POR PERIODO/DATA

while True:
    data_ou_periodo = input('Data/Periodo (d/p)')
    if data_ou_periodo == 'd':
        try:
            mes = input('Insira um mês: \n')
            ano = input('Insira um ano: \n')
            if ano == '':
                ano = lista_ano[0]
            periodo_total = pd.date_range(start = f'01/{mes}/{ano}', end = f'31/12/{lista_ano[-1]}')
            periodo_total = periodo_total.strftime("%Y%m%d")

            break

        except ValueError:
            print('\n(!) Erro: data inválida\n')

    
    elif data_ou_periodo == 'p':
        try:
            periodo_primeiro = input('Insira a primeira data do período (formato mes/dia/ano)')
            periodo_segundo = input('Insira a segunda data do período (formato mes/dia/ano)')
            periodo_total = pd.date_range(start = periodo_primeiro, end = periodo_segundo)
            periodo_total = periodo_total.strftime("%Y%m%d")

            break
        except ValueError:
            print('\n(!) Erro: período inválido\n')
    else:
        print('(!) Comando inválido')

#AGREGADOR DE .CSV
        
for arquivo in lista_arquivos:
    if arquivo[:8] in periodo_total:
            
        tabela = pd.DataFrame(pd.read_csv(f"teste_planilhas_chip\{arquivo}", header = 1))
        valores_csv.append(tabela)


tabela_total = pd.concat(valores_csv[i] for i in range(len(valores_csv)))

#CRIAÇÃO DE NOVAS COLUNAS

data_leitura_lst = []
horario_leitura_lst = []

seletor_linha = tabela_total.loc[:, "# Reading Time (UTC)"]

for tempo in seletor_linha:
    data_leitura_lst.append(f'{tempo[:4]}-{tempo[4:6]}-{tempo[6:8]}')
    horario_leitura_lst.append(f'{tempo[9:11]}:{tempo[11:13]}:{tempo[13:]}'.strip('Z'))

tabela_total.insert(0, 'Date', data_leitura_lst)
tabela_total.insert(1, 'Hour', horario_leitura_lst)
tabela_total.drop('# Reading Time (UTC)', axis= 1, inplace=True)


#OUTPUT

if not os.path.isdir(f'{periodo_total[0]}-{periodo_total[-1]}'):
    os.mkdir(f'{periodo_total[0]}-{periodo_total[-1]}')

tabela_total.to_csv(f'{periodo_total[0]}-{periodo_total[-1]}\\{periodo_total[0]}-{periodo_total[-1]}.csv', index=False)



print(f'\nCriado o arquivo {periodo_total[0]}-{periodo_total[-1]}.csv')
