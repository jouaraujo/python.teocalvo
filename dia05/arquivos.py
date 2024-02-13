#%%
# Saber aonde python está sendo executado
import os

os.getcwd()

#%%
arquivo = open("meu_arquivo.txt", "w")
arquivo.write("Sint consectetur velit officia eu enim ad Ullamco quis incidunt in.")
arquivo.close()

#%%

with open("meu_arquivo.txt", "a") as open_file:
    open_file.write("e mais uma vez\n")
    
#%%

with open("dados.csv", "r") as open_file:
    dados = open_file.readlines()


cabecalho = dados[0].replace("\n", "").split(";")

data_dict = {}

for i in cabecalho:
    data_dict[i]=[]
    
data_dict

for i in dados[1:]:
    valores = i.replace("\n", "").split(";")
    for i in range(len(cabecalho)):
        data_dict[cabecalho[i]].append(valores[i])

data_dict