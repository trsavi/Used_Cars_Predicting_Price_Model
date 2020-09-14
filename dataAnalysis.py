# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 18:50:21 2020

@author: Vukašin Vasiljević
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

cars = pd.read_csv('used_carsCleaned.csv')


plt.figure(figsize=(5,10))
chart = sns.countplot(y='Brend', data=cars)


# Just exploratory data analysis

plt.figure(figsize=(20,5))
sns.boxplot(x='Brend', y='Snaga', data=cars, palette='viridis')
plt.tight_layout()

sns.pairplot(cars, hue='Godiste', palette='viridis')

plt.figure(figsize=(10,5))
sns.boxplot(x='Model', y='Kilometraza', data=cars[cars['Brend']=='AUDI'], palette='viridis')
plt.tight_layout()

plt.figure(figsize=(10,5))
sns.boxplot(x='Model', y='Kilometraza', data=cars[cars['Brend']=='BMW'], palette='viridis')
plt.tight_layout()

plt.figure(figsize=(10,5))
sns.boxplot(x='Model', y='Kilometraza', data=cars[cars['Brend']=='OPEL'], palette='viridis')
plt.tight_layout()

plt.figure(figsize=(5,10))
sns.scatterplot(x='Godiste', y='Cena', data = cars, hue='Kilometraza')

plt.figure(figsize=(5,8))
sns.scatterplot('Snaga', 'Kubikaza', data = cars, hue='Gorivo')

plt.figure(figsize=(5,10))
sns.scatterplot(x='Cena', y='Kilometraza', data = cars, hue='Gorivo')

# Here we can see correlation between different type of parameters
plt.figure(figsize=(5,5))
sns.heatmap(cars.corr())