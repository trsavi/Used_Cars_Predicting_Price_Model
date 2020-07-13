# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 18:19:36 2020

@author: HP
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Collecting data
data = pd.read_csv('cars.csv')


print('Mean for car price is: {}'.format(data.cena.mean()))
print('Median for car price is: {}'.format(data.cena.median()))

brands = data.brend.unique()


print(data.brend.value_counts())
brend_counts = data.brend.value_counts()
to_remove = brend_counts[brend_counts<100].index
print(to_remove)

data = data[~data.brend.isin(to_remove)]


print(data.brend.value_counts())

models = data.model.unique()

"""
x = data.cena
data.cena.mode()
sns.set(style='darkgrid')
plt.figure(figsize=(10,6))
sns.distplot(x).set_title('Frequency Distribution Plot of Prices')
"""