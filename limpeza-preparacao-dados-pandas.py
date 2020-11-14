import pandas as pd
import numpy as np

# # dados de test
# dic = { 'A' : [1,2,3],
#         'B' : [4,5,6],
#         'C' : [7,8,9],
#         'D' : [10,11,12] }
# data = pd.DataFrame(dic)
# print("Tabela original")
# print(data)

# # excluir coluna
# data.drop('D', inplace=True, axis=1)
# print(data)

# Lidando com dados ausentes
dic = { 'A' : [1,2,np.nan],
        'B' : [3,4,5],
        'C' : [6,np.nan,8] }
data = pd.DataFrame(dic)
print(data)

data.isnull()
data.isnull().sum()
print(data)

# FONTE: https://medium.com/@lucasoliveiras/limpeza-e-prepara%C3%A7%C3%A3o-dos-dados-com-pandas-856e844abfbb