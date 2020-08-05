# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 18:19:36 2020

@author: HP
"""

import pandas as pd


# Getting data
data = pd.read_csv('carsPolovni.csv')

data.info()

print('Mean for car price is: {}'.format(data.Cena.mean()))
print('Median for car price is: {}'.format(data.Cena.median()))
print('Minimun car price is: {}'.format(data.Cena.min())) # 1
print('Maximum car price is: {}'.format(data.Cena.max())) # 
print('Minimun car power is: {}'.format(data.Snaga.min())) # 1
print('Maximum car power is: {}'.format(data.Snaga.max())) # 2175
print('Maximum mileage is: {}'.format(data.Kilometraza.max())) # 3800008
print('Average mileage is: {}'.format(data.Kilometraza.mean())) # 214737



### Cleaning outliers on whole dataset ###

print(data[data['Cena']<600]['Brend'].count()) # 929
print(data[data['Cena']>50000]['Naziv'].count()) # 419
print(data[data['Godiste']<1990]['Naziv'].count()) # 689
print(data[data['Kilometraza']>300000]['Naziv'].count())# 4403

data.drop(data[(data['Cena']<600) | (data['Cena']>50000) | (data['Godiste']<=1990) | (data['Kilometraza']>300000)].index, inplace=True)

# Converting power variable from type of object to integer

data['Snaga'].head()

data['Snaga'] = data['Snaga'].apply(lambda power: int(power.split("(")[1].replace('KS)','')))

data[data['Snaga']<50]['Naziv'].count() # 129
data[data['Snaga']>300]['Naziv'].count() # 129

data.drop(data[(data['Snaga']<50) | (data['Snaga']>300)].index, inplace=True)

# Dropping all models that has less than 100 cars in dataset
indexes = data.groupby('Model').filter(lambda x : (x['Model'].count()<100).any()).index

data.drop(indexes, inplace=True)

data.to_csv('carsPolovni.csv', index=False)





