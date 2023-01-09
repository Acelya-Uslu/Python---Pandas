# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 19:12:37 2022

@author: Acelya
"""

import pandas as pd
dictionary={"Name":["Açelya","Ali","Can","Sarp","Ege"],
            "Maas":[300,800,600,200,100],
            "Yas":[23,30,18,36,28]}

dataframe1 = pd.DataFrame(dictionary)

head=dataframe1.head() #ilk 5 data
tail=dataframe1.tail() #son 5 data

#%% Pandas Basic Methods

print(dataframe1.columns)
print(dataframe1.info())
#infoda pandas kütüphanesi string yazmak yerine object yazar.
#satırlara sample diyoruz.

print(dataframe1.dtypes)
print(dataframe1.describe())
#describe metodu--> numeric featurları(max,min,mean,std) verileri gösterir.columns(age,maas)

#%% Indexing and Slicing


print(dataframe1["Name"])

print(dataframe1.Yas)
print(dataframe1.Maas)

dataframe1["yeni feature"]=[1,2,3,4,5]
print(dataframe1.yeni_feature)


print(dataframe1.loc[:,"Yas"])
print(dataframe1.loc[:3,"Yas"]) #pandas da 3 indexi dahil



print(dataframe1.loc[:4,"Name":"Yas"])
print(dataframe1.loc[:4,["Name","Yas"]])



print(dataframe1.loc[::-1,:]) #Tersten yazdır değerleri

print(dataframe1.loc[:,:"Yas"]) #Yasa kadar yaz.
print("*****")
print(dataframe1.iloc[:,2])#indeksi 2 olan sütunu yazdır.Bütün satırları yazdır.(:)


#%% Filtering Pandas Data Frame

#Mesela maaşı 200 üstü olan insanları bulmak için filtreleme yapılır.

filtre1=dataframe1.Maas>200
filtrelenmis_data=dataframe1[filtre1]

filtre2=dataframe1.Yas>20

dataframe1[filtre1 & filtre2]

print(dataframe1[dataframe1.Yas>29])

#%% List Comprehension

import numpy as np



ortalama_maas=dataframe1.Maas.mean()
print(ortalama_maas)

ortalama_maas_np=np.mean(dataframe1.Maas)
print(ortalama_maas_np)


#list comprehension:
dataframe1["Maas Seviyesi"]=["yuksek" if ortalama_maas < each else "dusuk"for each in dataframe1.Maas]

dataframe1.columns=[each.lower() for each in dataframe1.columns]

dataframe1.columns=[each.split()[0]+"_"+each.split()[1] if(len(each.split())>1)  else each for each in dataframe1.columns]

#%% Drop and Concatenating data


#column drop ediyoroz. axis=1 --> column siler, axis=0--> row siler.inplace=true yaptımızı datafram1e eşitliyor.
dataframe1.drop(["Name"],axis=1,inplace=True)

#numpy da vstack ve hstack vardı.Vertical veya horizantal birleştirme

data1=dataframe1.head()
data2=dataframe1.tail()

#vertical birleştirme
data_concat=pd.concat([data1,data2],axis=0)

maas=dataframe1.Maas
yas=dataframe1.Yas


data_h_concat=pd.concat([maas,yas],axis=1)


#%% Transforming Data


dataframe1["list_comp"]=[each*2 for each in dataframe1.Yas]


# apply metodu
def multiply(age):
    return age*2

dataframe1["apply_method"]=dataframe1.Yas.apply(multiply)


























































