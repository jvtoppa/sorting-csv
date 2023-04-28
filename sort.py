import pandas as pd
import numpy as np
import os


    
    
tabela_total = pd.DataFrame()
lista_arquivos = os.listdir("teste_planilhas_chip")

lst_all = []
lst_ano = []
lst_mes = []
lst = []


fl = 1
#lista de todos as datas
for x in range(len(lista_arquivos)):
    lst_all.append(lista_arquivos[x][:8])

#lista de todos os anos
for y in range(len(lst_all)):
    lst_ano.append(int(lst_all[y][:4]))
    lst_ano = list(set(lst_ano))

#lista de todos os meses
for z in range(1, 13):
    lst_mes.append(int(z))
while True:
    mes_periodo = input('Data/Periodo (d/p)')
    if mes_periodo == 'd':
        m = input('Insira um mês: \n')
        
        if m != '':
            fl = 0
            if int(m) not in lst_mes:
                print('erro\n')
            else:
                if m != '':
                    lst_mes = [int(m)]
            
                
        a = input('Insira um ano: \n')
        if a != '':
            if int(a) not in lst_ano:
                print('erro\n')
            else:
                if a != '':
                    if int(a) in lst_ano:
                        lst_ano = [int(a)]
                        
                        if m != '':
                            fl = 2
                        break

                elif a == '' and m == '':
                    print('erro\n')
                
                else:
                    
                    break
        else:
            break
    
    if mes_periodo == 'p':

        periodo_primeiro = input('Insira a primeira data do período (formato ano-mes-dia)')
        periodo_segundo = input('Insira a segunda data do período (formato ano-mes-dia)')
        date1 = periodo_primeiro.split('-')
        date2 = periodo_segundo.split('-')
        date_end = []

        for i in date1:
            date_end.append(i)

        for i in date2:
            date_end.append(i)

        dia_inicial = date_end[2]
        dia_final = date_end[5]

        lst_dia_inicial = [x for x in range(int(dia_inicial), 32)]
        lst_dia_final = [x for x in range(1, int(dia_final) + 1)]
        lst_dia = [x for x in range(1, 32)]

for arquivo in lista_arquivos:
    if int(arquivo[:4]) in lst_ano and int(arquivo[4:6]) in lst_mes:
        tabela = pd.DataFrame(pd.read_csv(f"teste_planilhas_chip\{arquivo}"))
        lst.append(tabela)

tabela_total = pd.concat(lst[i] for i in range(len(lst)))


if fl == 0:
    if os.path.isdir('mes-' + str(m)) == False:
        os.mkdir('mes-' + str(m))
    tabela_total.to_csv('mes-' + str(m) +'\mes-' + str(lst_mes[0]) + '.csv')

elif fl == 2:
    if os.path.isdir('ano-' + str(a) + '-mes-' + str(m)) == False:
        os.mkdir('ano-' + str(a) + '-mes-' + str(m))
    tabela_total.to_csv('ano-' + str(a) + '-mes-' + str(m) + '\\ano-'+ str(lst_ano[0]) + '-mes-' + str(lst_mes[0]) + '.csv')

else:
    if os.path.isdir('ano-' + str(a)) == False:
        os.mkdir('ano-' + str(a))
    tabela_total.to_csv('ano-' + str(a) + '\\ano-'+ str(lst_ano[0]) + '.csv')