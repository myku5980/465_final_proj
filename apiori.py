# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 19:40:53 2020

@author: peter
"""
import itertools as iter
import numpy as np
import pandas as pd
totalTrans = 315
minSupportCount = 115 #lowest amount of a single product that was bought gotten ahead of time
minSupport = minSupportCount/totalTrans
minConfidence = 0.60
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

productARR = []
i = 0


#the for loop below goes through the item frequency series and drops the item not meeting the min support threshold
i = 0;
for index, row in ic.iteritems():
    
    if row/totalTrans < minSupport:
        
        print("Dropping " + index)
        
        ic.drop(labels=[index], inplace=True)
    else:
        
        productARR.append(index)
        i = i+1  
        
        

print(ic)
print("Frequency 1-itemset table has been pruned")

print(productARR)
loop = 1
print("creating combinations for 2 itemset table")

newARR = []
itemsetNum = 2
end = False
#commencing the algorithm after first finding the freq item set manually
while loop == 1:
    #creating combinations for the next table
    #itemset will be increasing as the 
    for subset in iter.combinations(productARR,2):
        newARR.append(subset)
    productARR = newARR
    print(productARR)
        
    
    loop = 0
        
        
        
        
     

