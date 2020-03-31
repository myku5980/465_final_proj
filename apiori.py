
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 19:40:53 2020

@author: peter
"""

import numpy as np
import pandas as pd

        #this is just the path to the dataset location   
retail = 'C:/Users/peter/OneDrive/Documents/cp 465/retail_dataset.csv'
retail_DF = pd.read_csv(retail)
oneCol = []
itemCount = retail_DF["Product 1"]
print(itemCount)
itemCount = itemCount.append(retail_DF["Product 2"])
print(itemCount)
itemCount = itemCount.append(retail_DF["Product 3"])
print(itemCount)
itemCount = itemCount.append(retail_DF["Product 4"])
print(itemCount)
itemCount = itemCount.append(retail_DF["Product 5"])
print(itemCount)
itemCount = itemCount.append(retail_DF["Product 6"])
print(itemCount)
itemCount = itemCount.append(retail_DF["Product 7"])
print(itemCount)

ic = itemCount.value_counts()
print(ic)
