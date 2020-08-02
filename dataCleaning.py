# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 18:19:36 2020

@author: HP
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Getting data
data = pd.read_csv('carsPolovni.csv')


print('Mean for car price is: {}'.format(data.Cena.mean()))
print('Median for car price is: {}'.format(data.Cena.median()))
print('Minimun car price is: {}'.format(data.Cena.min()))
print('Maximum car price is: {}'.format(data.Cena.max()))



### Cleaning outliers on whole dataset ###

print(data[data['Cena']<600]['Brend'].count()) # 929
print(data[data['Cena']>50000]['Naziv'].count()) # 419
print(data[data['Godiste']<1990]['Naziv'].count()) # 689
print(data[data['Kilometraza']>300000]['Naziv'].count())# 4403


data.drop(data[(data['Cena']<600) | (data['Cena']>50000) | (data['Godiste']<=1990)].index, inplace=True)

# Visualizing average price for each brand

plt.figure(figsize=(15,5))
chart = sns.barplot(x='Brend',y='Cena',data=data, estimator=np.std)
chart.set_xticklabels(chart.get_xticklabels(), rotation=60)

# Year distribution
sns.distplot(data['Godiste'], bins=30)

# Mileage distribution

sns.distplot(data['Kilometraza'], bins=30)


# Dropping all models that has less than 100 cars in dataset
indexes = data.groupby('Model').filter(lambda x : (x['Model'].count()<100).any()).index

data.drop(indexes, inplace=True)

data.to_csv('carsPolovni.csv', index=False)





