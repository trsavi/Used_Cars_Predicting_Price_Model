# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 21:19:20 2020

@author: HP
"""

from selenium import webdriver
from bs4 import BeautifulSoup as bs
import pandas as pd
import sys
driver = webdriver.Chrome('C:/Users/HP/Downloads/chromedriver.exe')



def parse_page(url):
    try:
        driver.get(url)
        content = driver.page_source
        soup = bs(content,'html.parser')
        return soup
    except:
        pass

# returns a list of all models of one brand
def get_models(brand):
	brand = (brand.replace(' ', '-')).lower()
	url ='https://www.polovniautomobili.com/auto-oglasi/pretraga?brand=' + brand
	soup = parse_page(url)
	models= soup.find(id='model')
	models_list=[]
	for model in models:
		if model.get_text()=='Ostalo':
			pass
		else:
			models_list.append(model.get_text())
	return models_list[1:]


# returns a list of all brands 
def all_Brands():
	url = 'https://www.polovniautomobili.com/#'
	soup = parse_page(url)
	brands = soup.find(id='brand')
	brands_list = []
	for brand in brands:
		brands_list.append(brand.get_text())

	return brands_list[1:]

# function that replaces characters in string
def replace(string):
	string = string.replace('š','s')
	string = string.replace('Š','s')
	string = string.replace('ć','c')
	string = string.replace('Ć','c')
	string = string.replace('Ž','z')
	string = string.replace('ž','z')
	string = string.replace('č','c')
	string = string.replace('Č','c')
	return string

def get_num_of_cars(url):
	soup = parse_page(url)
	if soup!=None:
		try:
			num = soup.findAll('small')
			num = num[3].get_text()
			num = num.split(' ')[-1]
			return (round(int(num)/25))
		except:
			pass



# get all cars from one brand and model
def get_cars(brand, model):

	brand = (brand.replace(' ', '-')).lower()
	model = (model.replace(' ', '-')).lower()
	url ='https://www.polovniautomobili.com/auto-oglasi/pretraga?brand=' + brand + '&model[]=' + model


	
	num = get_num_of_cars(url)
	if num==0:
		num=1

	carList = []
	# loop over number of pages
	for i in range(1,num+1):
		soup = parse_page(url+'&page='+str(i))
		#print(soup)
		if soup!=None:
			pages = soup.findAll('article')
			for page in pages:
				pageT = page.find('a')
				try:
					title = pageT.get('title')
					if title==None:
						pass
					else:
                        
						discount = page.find(class_='price price-discount')
						if discount!=None:
							price = discount.get_text()
							continue
						else:
							price = page.find(class_='price')
							price = price.get_text()
						content = page.findAll(class_='inline-block')
						blocks = []
						for con in content:
							blocks.append(con.get_text())
						god = int(blocks[0][:4])
						km = blocks[1].replace('.','')
						km = km.replace(' km |', '')
						km = int(km)
						gor = str(blocks[2][:-2])
						gor = replace(gor)
						kub = int(blocks[3][:4])
						kar = (blocks[4].replace(',',''))
						kar = replace(kar)
						sn = (blocks[5].replace(', ',''))
						

						try:
							price = int(price[:-2].replace('.',''))
							dictionary = {
									'Brend': (brand.replace('-', ' ')).upper(),
									'Model': (model.replace('-', ' ')).upper(),
									'Naziv': replace(title),
									'Cena': price,
									'Godiste': god,
									'Kilometraza':km,
									'Gorivo':gor,
									'Kubikaza':kub,
									'Karoserija':kar,
									'Snaga': sn
							}
							# append every car to list as dictionary
							carList.append(dictionary)

						except:
							pass

				except Exception: 
					pass
 
	return carList


# function that inserts cars into database
def insertDBAll():
    data = pd.DataFrame()
    brands = all_Brands()
    try:
        for brand in brands:
            models = get_models(brand)
            for model in models:
                if model==None:
                    pass
                else:
                    cars = get_cars(brand, model)
                    for car in cars:
                        if car==None:
                            pass
                        else:
                            data = data.append(car,ignore_index=True)
                            print(data)
                            sys.exit()
    except Exception as e:
        pass

# create database and then insert data
#createDB()
insertDBAll()
print("Data inserted")
