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
%cd ~/Desktop/ARRIVALS

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
plt.savefig('comcode_boxplot.png')
sns.boxplot(importantes.nature_of_transaction)
plt.savefig('nature_of_transaction_boxplot.png')
sns.boxplot(importantes.stat_value)
plt.savefig('stat_value_boxplot.png')
sns.boxplot(importantes.period_reference)
plt.savefig('period_reference_boxplot.png')
sns.boxplot(importantes.sitc)
plt.savefig('sitc_boxplot.png')
sns.boxplot(importantes.no_of_consignments)
plt.savefig('no_of_consignments_boxplot.png')
sns.boxplot(importantes.nett_mass)
plt.savefig('nett_mass_boxplot.png')
sns.boxplot(importantes.supp_unit)
plt.savefig('supp_unit_boxplot.png')
sns.boxplot(importantes.file_month)
plt.savefig('file_month_boxplot.png')



#DISTRIBUCIÓN
sns.kdeplot(importantes.comcode, cumulative=True)
plt.savefig('comcode_distribucion.png')
sns.kdeplot(importantes.nature_of_transaction, cumulative=True)
plt.savefig('nature_of_transaction_distribucion.png')
sns.kdeplot(importantes.period_reference, cumulative=True)
plt.savefig('period_reference_distribucion.png')
sns.kdeplot(importantes.sitc, cumulative=True)
plt.savefig('sitc_distribucion.png')



#DENSIDAD
sns.kdeplot(importantes.comcode, shade=True)
plt.savefig('comcode_densidad.png')
sns.kdeplot(importantes.nature_of_transaction, shade=True)
plt.savefig('nature_of_transaction_densidad.png')
sns.kdeplot(importantes.stat_value, shade=True)
plt.savefig('stat_value_densidad.png')
sns.kdeplot(importantes.period_reference, shade=True)
plt.savefig('period_reference_densidad.png')
sns.kdeplot(importantes.sitc, shade=True)
plt.savefig('sitc_densidad.png')
sns.kdeplot(importantes.no_of_consignments, shade=True)
plt.savefig('no_of_consignments_densidad.png')
sns.kdeplot(importantes.nett_mass, shade=True)
plt.savefig('nett_mass_densidad.png')
sns.kdeplot(importantes.supp_unit, shade=True)
plt.savefig('supp_unit_densidad.png')
sns.kdeplot(importantes.file_month, shade=True)
plt.savefig('file_month_densidad.png')