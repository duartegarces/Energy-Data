##########  #####        #####          #############
##########  #####        #####          #############
####           #####  #####                ##########
####            ####  ####                 ##########
#######          ########                  ##########
#######            ####                    ##########
####             ########                  ##########
####            ####  ####                 ##########
##########     #####  #####     ###     ############### 
##########  #####        #####  ###     ###############

import pandas as pd

informacao = pd.read_csv("D:\\Universidade\\2º Semestre\\ICD\\Trabalho 1\\owid-energy-data.csv", index_col=0)

print(informacao)

print(informacao.country)

paises_selecionados = informacao.loc[informacao.country.isin(['Italy', 'France', 'Germany', 'United Kingdom'])]

print(paises_selecionados)

paises_selecionados.to_csv(r'D:\\Universidade\\2º Semestre\\ICD\\Trabalho 1\\paisesescolhidos.csv', index=False)


##########  #####        #####          #############
##########  #####        #####          #############
####           #####  #####                     #####
####            ####  ####                      #####
#######          ########               #############
#######            ####                 #############
####             ########               #####
####            ####  ####              #####
##########     #####  #####     ###     #############
##########  #####        #####  ###     #############

import matplotlib.pyplot as plt
import matplotlib.pyplot as mp
import mplcursors
 
plt.close("all")

Italia = paises_selecionados[paises_selecionados.country == "Italy"]
print(Italia.oil_electricity[85:120])

Franca = paises_selecionados[paises_selecionados.country == "France"]
print(Franca)

Alemanha = paises_selecionados[paises_selecionados.country == "Germany"]
print(Alemanha.oil_electricity)

Reino_Unido = paises_selecionados[paises_selecionados.country == "United Kingdom"]
print(Reino_Unido.oil_electricity)

plt.plot(Italia.year, Italia.oil_electricity, marker='o')
plt.plot(Franca.year, Franca.oil_electricity, marker='o')
plt.plot(Alemanha.year, Alemanha.oil_electricity, marker='o')
plt.plot(Reino_Unido.year, Reino_Unido.oil_electricity, marker='o')

plt.title('Evolução da produção de eletricidade nos países')
plt.xlabel('Ano')
plt.ylabel('Produção Eletricidade')
plt.legend(['Italia', 'Frnca', 'Alemanha', 'Reino_Unido'])

plt.show()


##########  #####        #####          #############
##########  #####        #####          #############
####           #####  #####                     #####
####            ####  ####                      #####
#######          ########                    ########
#######            ####                      ########
####             ########                       #####
####            ####  ####                      #####
##########     #####  #####     ###     #############
##########  #####        #####  ###     #############

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.figure(figsize=(7,7))

UK_2010 = paises_selecionados.loc[(paises_selecionados.country == "United Kingdom") & (paises_selecionados.year == 2010)]
print(UK_2010)
UK_2010.to_csv(r'D:\\Universidade\\2º Semestre\\ICD\\Trabalho 1\\UK2010.csv', index=False)
total_produzido = UK_2010.biofuel_electricity + UK_2010.coal_electricity + UK_2010.fossil_electricity + UK_2010.gas_electricity + UK_2010.hydro_electricity + UK_2010.nuclear_electricity + UK_2010.oil_electricity 
print(total_produzido)
labels = ['Biofuel', 'Coal', 'Fossil', 'Gas', 'Hydro', 'Nuclear', 'Oil']
Bio = UK_2010.biofuel_electricity
Coal = UK_2010.coal_electricity
Fossil = UK_2010.fossil_electricity
Gas = UK_2010.gas_electricity
Hydro = UK_2010.hydro_electricity
Nuclear = UK_2010.nuclear_electricity
Oil = UK_2010.oil_electricity
x = np.array([Bio, Coal, Fossil, Gas, Hydro, Nuclear, Oil]).flatten()

plt.pie(x, labels=labels, autopct='%.2f %%')
plt.title('Fontes produção de eletricidade UK 2010')
plt.legend(title = "Tipo Produção")
plt.show()


##########  #####        #####          ####        ####
##########  #####        #####          ####        ####
####           #####  #####             ####        ####  
####            ####  ####              ####        ####
#######          ########               ##################
#######            ####                 ##################
####             ########                           ####
####            ####  ####                          ####
##########     #####  #####     ###                 ####
##########  #####        #####  ###                 ####


Pais = input("Insira o Pais")
print(Pais)


for x in paises_selecionados: 
    verificar = paises_selecionados.loc[paises_selecionados.country == Pais]
    print(verificar)
    
    descobrir_ano = verificar.loc[verificar.nuclear_consumption == verificar.nuclear_consumption.max() ]
    descobrir_ano.loc[:, ['country','nuclear_consumption', 'year']]
    
    
        
    
   