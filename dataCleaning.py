# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 18:19:36 2020

@author: HP
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import regex as re
# Collecting data
data = pd.read_csv('carsPolovni.csv')


print('Mean for car price is: {}'.format(data.Cena.mean()))
print('Median for car price is: {}'.format(data.Cena.median()))
print(data.Cena.min())
data[data['Brend']=='']
brands = data.Brend.unique()
def contains(string):
    regexp = re.compile(r'B5.5')
    if regexp.search(string):
        return True
    


contains('Volkswagen Passat B5.5 1.8T')
print(data.Brend.value_counts())
#brend_counts = data.brend.value_counts()
#to_remove = brend_counts[brend_counts<100].index
#print(to_remove)





"""
x = data.cena
data.cena.mode()
sns.set(style='darkgrid')
plt.figure(figsize=(10,6))
sns.distplot(x).set_title('Frequency Distribution Plot of Prices')
"""