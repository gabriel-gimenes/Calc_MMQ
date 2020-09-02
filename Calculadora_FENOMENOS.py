# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 12:11:46 2020

@author: gabri
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

def main():
    lista_exp_data = []
    lista_summation = []
    ix_exp_data = []
    print("Calculadora de MMQ")
    d = (input('Do you want to run an example or to insert experimental data?[r or i]: ')).lower()
    if d == 'r':   
    #Exemplo de Teste:
        n = 10
        x = np.array([-2.09,-1.76,-1.51,-1.22,-.92,-.69,-.56,-.41,-.25,-.07])
        y = np.array([0.002915,.002976,.00303,.003086,.003154,.003215,.003247,
                .003279,.003322,.003356])
        alpha_square = np.array([4E-06,4E-06,4E-06,5E-06,5E-06,5E-06,5E-06,
                            5E-06,6E-06,6E-06])**2
    else:
    #Inserção de dados do experimento
        n = int(input('Qual o número de dados a ser computado?: '))
        x = np.array([float(input(f'Digite o valor de x[{x}]: ')) for x in range(n)])
        y = np.array([float(input(f'Digite o valor de y[{y}]: ')) for y in range(n)])
        alpha_square = np.array([(float(input(f'Digite o erro experimental de y[{y}]: ')))**2 for y in range(n)])
    

#Criando DataFrame para os dados digitados pelo usuário
    for i in range(n):
        lista_exp_data.append([x[i],y[i],alpha_square[i]])
        ix_exp_data.append(i)    
        
    exp_data = pd.DataFrame(lista_exp_data,index = ix_exp_data, columns = ['x-values','y-values','exp-error'])
    
    print('\n'+ 10*'-' + 'Experiment Data' + 10*'-')
    print(exp_data,end = 2*'\n')
    
#Criando DataFrame para os somatórios
    yi_over_alpha_square = y/alpha_square
    xi_over_alpha_square = x/alpha_square
    one_over_alpha_square = 1/alpha_square
    xi_mult_yi_over_alpha_square = (x*y)/alpha_square
    xi_square_over_alpha_square = x**2/alpha_square
    total = [yi_over_alpha_square.sum(),xi_over_alpha_square.sum(),
             one_over_alpha_square.sum(),xi_mult_yi_over_alpha_square.sum(),
             xi_square_over_alpha_square.sum()]
    
    for i in range(n):
        lista_summation.append([yi_over_alpha_square[i],xi_over_alpha_square[i],one_over_alpha_square[i],xi_mult_yi_over_alpha_square[i],xi_square_over_alpha_square[i]])
        
    ix_exp_data.append('Total')
    lista_summation.append(total)
    summation = pd.DataFrame(lista_summation,index = ix_exp_data,columns = ['yi/αi²','xi/αi²','1/αi²','xi*yi/αi²','xi²/αi²'])
    
    print(30*'-' + 'Summation' + 30*'-')
    print(summation)
    
#Calculando coeficientes a e b, além de suas respectivas incertezas (pendente)
    
    a = ((total[0]*total[1])-(total[2]*total[3]))/((total[1]**2) - (total[4]*total[2]))
    
    b = (total[0]-a*total[1])/total[2]
    
    print(f'\nSlope: {a}, Linear Coefficient: {b}')
#plot do gráfico com os pontos das coordenadas x e y, além da reta que melhor se ajusta.
    
    #plt.yticks([0.0025,0.0030,0.0035,0.0040,0.0045,0.0050])
    if x.min() < 0:
        xmin = x.min()*1.1
    else:
        xmin = x.min()*0.9
    
    if x.max() < 0:
        xmax = x.max()*0.9
    else:
        xmax = x.max()*1.1

    if y.min() < 0:
        ymin = y.min()*1.1
    else:
        ymin = y.min()*0.9
    
    if y.max() < 0:
        ymax = y.max()*0.9
    else:
        ymax = y.max()*1.1

    y1 = a*x+b
    plt.title('Graph of  x and y')
    plt.xlabel('x-values')
    plt.ylabel('y-values')
    plt.xlim(xmin,xmax)
    plt.ylim(ymin,ymax)
    plt.tight_layout()
    plt.scatter(x, y, color='k', label = 'Experiment points')
    plt.plot(x, y1, color='b', label = 'Best fit line')
    plt.legend()
    plt.show()

main()