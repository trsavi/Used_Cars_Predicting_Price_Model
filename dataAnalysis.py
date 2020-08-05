# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 18:50:21 2020

@author: Vukašin Vasiljević
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Getting data
data = pd.read_csv('carsPolovni.csv')


# Visualizing power based on brand

plt.figure(figsize=(20,5))
sns.boxplot(x='Brend', y='Snaga', data=data, palette='viridis')
plt.tight_layout()


# Visualizing average price for each brand

plt.figure(figsize=(15,5))
chart = sns.barplot(x='Brend',y='Cena',data=data, estimator=np.std)
chart.set_xticklabels(chart.get_xticklabels(), rotation=60)

# Visualizing BMW brand based on model and power

bmw = data[data['Brend']=="BMW"]
plt.figure(figsize=(12,6))
sns.boxplot(x='Model', y='Kilometraza', data=bmw, palette='viridis')
plt.title('BMW')
plt.xlabel('Model')
plt.ylabel('Kilometraza')
plt.tight_layout()

# V
plt.figure(figsize=(20,5))
sns.boxplot(x='Brend', y='Kilometraza', data=data, palette='viridis')
plt.tight_layout()
