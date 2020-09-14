# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 18:19:36 2020

@author: Vukašin vailjević
"""

import pandas as pd

cars = pd.read_csv('used_cars.csv')

cars.info()

cars.head()

# "Power" parameter is missing (it's object type instead of int type)
cars.describe()

# This will drop all duplicates based on all the columns except model
#cars.drop_duplicates(subset=['Naziv','Brend','Cena','Godiste','Karoserija','Gorivo','Kilometraza','Snaga','Kubikaza'])


# See model count for each brand
brands = cars.groupby('Brend')
for brand, item in brands:
    print(brand)
    print('Models: ')
    print(cars[cars['Brend']==brand]['Model'].value_counts())
    print('\n')

# Delete duplicated values based on series of models
cars.drop(cars[cars['Brend']=='KIA'].index, inplace=True)
cars.drop(cars[cars['Model']=='GOLF'].index, inplace=True)
cars.drop(cars[cars['Model']=='PASSAT'].index, inplace=True)
cars.drop(cars[cars['Model']=='ASTRA'].index, inplace=True)
cars.drop(cars[cars['Model']=='CORSA'].index, inplace=True)
cars.drop(cars[cars['Model']=='VECTRA'].index, inplace=True)
cars.drop(cars[cars['Model']=='SERIJA 3'].index, inplace=True)
cars.drop(cars[cars['Model']=='SERIJA 5'].index, inplace=True)
cars.drop(cars[cars['Model']=='SERIJA X'].index, inplace=True)
cars.drop(cars[cars['Model']=='SERIJA 7'].index, inplace=True)
cars.drop(cars[cars['Model']=='E KLASA'].index, inplace=True)
cars.drop(cars[cars['Model']=='C KLASA'].index, inplace=True)
cars.drop(cars[cars['Model']=='B KLASA'].index, inplace=True)
cars.drop(cars[cars['Model']=='S KLASA'].index, inplace=True)


# Check for missing values
cars[cars.isna()].count()

# We need to change power variable into int data type
cars['Snaga'] # object type

cars['Snaga'] = cars['Snaga'].apply(lambda power: int(power.split("(")[1].replace('KS)','')))

# Now power is in int type and it's only in horse power (HP)
cars['Snaga']


# Let's explore data a little bit further with seaborn
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# Year distribution and cleaning
sns.distplot(cars['Godiste'], bins=30 )

print(cars[cars['Godiste']<1980]['Godiste'].count())
print(cars[cars['Godiste']<1990]['Godiste'].count())
print(cars[cars['Godiste']<2000]['Godiste'].count())

# Looks like we are going to drop all cars below 1980s threshold
cars.drop(cars[cars['Godiste']<1980].index, inplace=True)

# Let's see now year distribution
sns.distplot(cars['Godiste'], bins=40)

# Mileage distribution and cleaning
sns.distplot(cars['Kilometraza'])

cars[cars['Kilometraza']>500000].count()
cars.drop(cars[cars['Kilometraza']>500000].index, inplace=True)

sns.distplot(cars['Kilometraza'], bins=30)


# Power distribution and cleaning
sns.distplot(cars['Snaga'])

cars[cars['Snaga']>300].count()
cars.drop(cars[(cars['Snaga']>300) | (cars['Snaga']<50)].index, inplace=True)
cars.drop(cars[(cars['Kubikaza']>3000) | (cars['Kubikaza']<900)].index, inplace=True)

sns.distplot(cars['Snaga'], bins=25, kde=False)

# Price distribution and cleaning
sns.distplot(cars['Cena'])

cars[cars['Cena']>35000].count()
cars[cars['Cena']<500]['Brend'].value_counts()
cars.drop(cars[(cars['Cena']>35000) | (cars['Cena']<500)].index, inplace=True)
cars.drop(cars[cars['Cena']<500].index, inplace=True)

sns.distplot(cars['Cena'])

# Volume distribution
sns.distplot(cars['Kubikaza'])

sns.distplot(cars['Kubikaza'], bins=30)

# Count plot for fuel type
sns.countplot(x='Gorivo', data=cars)

# Count plot for chassis type
chart = sns.countplot(x='Karoserija', data=cars)
chart.set_xticklabels(chart.get_xticklabels(),rotation=90)

# Brand count plot
plt.figure(figsize=(5,10))
chart = sns.countplot(y='Brend', data=cars)
#chart.set_xticklabels(chart.get_xticklabels(),rotation=45)

# PASSAT b5.5 has mixed models, we need to clean that
cars[cars['Model']=='PASSAT B5.5']

cars[cars['Model']=='PASSAT B5.5']['Naziv']

# using regex we will distinguish b5.5 model from the rest
import regex as re

def delete(title):
    if re.search(r'B5.5', title):
        return title
    return None
#cars[cars['Model']=='PASSAT B5.5']['Naziv'].apply(lambda title: delete(title))
cars.loc[cars['Model']=='PASSAT B5.5', ['Naziv']] = cars[cars['Model']=='PASSAT B5.5']['Naziv'].apply(lambda title: delete(title))
cars.dropna(inplace=True)

cars.loc[cars['Model']=='PASSAT B5.5', ['Naziv']]
# CROSSLAND X has mixed models without its own model
cars.drop(cars[cars['Model']=='CROSSLAND X '].index, inplace=True)

# Now let's see car count by brand
plt.figure(figsize=(5,10))
chart = sns.countplot(y='Brend', data=cars)

# Dropping all models that has less than 90 cars in dataset
indexes = cars.groupby('Model').filter(lambda x : (x['Model'].count()<90).any()).index

cars.drop(indexes, inplace=True)

# Save cleaned dataframe to new csv file
cars.to_csv('used_carsCleaned.csv', index=False)




