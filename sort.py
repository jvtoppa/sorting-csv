import pandas as pd
import numpy as np
import PySimpleGUI as sg
import os
from collections import Counter

def main(): 

    sg.theme('DarkGray7') 
    layout = [
            [sg.Text('AGREGADOR DE ARQUIVOS CSV', font=('Arial Bold', 20), justification='center')],
            [sg.Text('Escolha o caminho dos arquivos a serem analizados: ', font=('Arial Bold', 10))],
            [sg.Input(enable_events=True, key='FILE-IN',font=('Arial Bold', 12),expand_x=True), sg.FolderBrowse()],
            [sg.Text('Escolha o período: ', font=('Arial Bold', 10))],
            [sg.Input(key = 'CALENDAR-INICIAL', size=(20,1)), sg.CalendarButton('Data inicial',format='%m/%d/%Y')],
            [sg.Input(key = 'CALENDAR-FINAL', size=(20,1)), sg.CalendarButton('Data final',format='%m/%d/%Y')],
            [sg.Text('Escolha o filtro: ', font=('Arial Bold', 10))],
            [sg.Combo(['N/A', 'Frequência do Registro', '1', '2'],key='FILTER')],
            [sg.Button('OK'), sg.Button('Exit')]
            ]
    
    window = sg.Window('Leitor CSV', layout, icon='bee-tag.ico')
    while True: 
        event, values = window.read() 
        print(event, values) 
      
        if event in (None, 'Exit'): 
            break
      
        if event == 'OK': 
      
            periodo_primeiro = values['CALENDAR-INICIAL']
            periodo_segundo = values['CALENDAR-FINAL']
            lista_arquivos = os.listdir(values['FILE-IN'])
            periodo_total = pd.date_range(start = periodo_primeiro, end = periodo_segundo)
            periodo_total = periodo_total.strftime("%Y%m%d")

            tabela_total = pd.DataFrame()
    
            lista_ano = []
            valores_csv = []


            for all_values in range(len(lista_arquivos)):
                lista_ano.append(int(lista_arquivos[all_values][:4]))
                lista_ano = list(set(lista_ano))


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

            #FILTRO POR OBJETO
            while True:
                if values['FILTER'] == '':
                    break
                
                elif values['FILTER'] == 'N/A':
                    break

                elif values['FILTER'] == 'Frequência do Registro':
                    tabela_filtrada_0 = tabela_total[' SN'].value_counts()
                    print(tabela_filtrada_0)
                    break


            #OUTPUT

            if not os.path.isdir(f'{periodo_total[0]}-{periodo_total[-1]}'):
                os.mkdir(f'{periodo_total[0]}-{periodo_total[-1]}')

            tabela_total.to_csv(f'{periodo_total[0]}-{periodo_total[-1]}\\{periodo_total[0]}-{periodo_total[-1]}.csv', index=False)
            
            if values['FILTER'] == '0':
                tabela_filtrada_0.to_csv(f'{periodo_total[0]}-{periodo_total[-1]}\\filtro-0.csv')



            print(f'\nCriado o arquivo {periodo_total[0]}-{periodo_total[-1]}.csv')
            
  
    window.close() 


    

if __name__ == "__main__":
    
    main()
