# -*- coding: utf-8 -*-
"""
Created on Tue May  3 11:26:28 2016

@author: marisarivera
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('max_columns', 50)
%matplotlib inline

import csv
%cd ~/Desktop

!head -n 5 enigma.csv

pd.set_option('max_columns', 50)
from_csv = pd.read_csv('enigma.csv')

#Análisis Estadístico de Todas las Variables
from_csv.head()
from_csv.describe()
from_csv.info()
from_csv.shape



importantes = from_csv[['comcode','cod_alpha','nature_of_transaction','stat_value',
               'period_reference','sitc','no_of_consignments','nett_mass',
               'supp_unit','file_month']]
importantes.head()



#HISTOGRAFÍA
plt.hist(importantes.comcode)
plt.savefig('comcode.png')
plt.hist(importantes.nature_of_transaction)
plt.savefig('nature_of_transaction.png')
plt.hist(importantes.period_reference)
plt.savefig('period_reference.png')
plt.hist(importantes.sitc)
plt.savefig('sitc.png')
plt.hist(importantes.no_of_consignments)
plt.savefig('no_of_consignments.png')


#BOXPLOT
sns.boxplot(importantes.comcode)
sns.boxplot(importantes.cod_alpha)
sns.boxplot(importantes.nature_of_transaction)
sns.boxplot(importantes.stat_value)
sns.boxplot(importantes.period_reference)
sns.boxplot(importantes.sitc)
sns.boxplot(importantes.no_of_consignments)
sns.boxplot(importantes.nett_mass)
sns.boxplot(importantes.supp_unit)
sns.boxplot(importantes.file_month)



#DISTRIBUCIÓN
sns.kdeplot(importantes.comcode, cumulative=True)
sns.kdeplot(importantes.nature_of_transaction, cumulative=True)
sns.kdeplot(importantes.period_reference, cumulative=True)
sns.kdeplot(importantes.sitc, cumulative=True)
sns.kdeplot(importantes.no_of_consignments, cumulative=True)



#DENSIDAD
sns.kdeplot(importantes.comcode, shade=True)
sns.kdeplot(importantes.cod_alpha, shade=True)
sns.kdeplot(importantes.nature_of_transaction, shade=True)
sns.kdeplot(importantes.stat_value, shade=True)
sns.kdeplot(importantes.period_reference, shade=True)
sns.kdeplot(importantes.sitc, shade=True)
sns.kdeplot(importantes.no_of_consignments, shade=True)
sns.kdeplot(importantes.nett_mass, shade=True)
sns.kdeplot(importantes.supp_unit, shade=True)
sns.kdeplot(importantes.file_month, shade=True)