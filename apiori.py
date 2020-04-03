# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 19:40:53 2020

@author: peter
"""
import itertools as iter
import numpy as np
import pandas as pd
totalTrans = 315
minSupportCount = 60 #lowest amount of a single product that was bought gotten ahead of time
minSupport = minSupportCount/totalTrans
minConfidence = 0.60
        #this is just the path to the dataset location   
retail = 'C:/Users/peter/OneDrive/Documents/cp 465/retail_dataset.csv'
retail_DF = pd.read_csv(retail)
frequentSetTotal = pd.Series()
print(retail_DF)
oneCol = []
itemCount = retail_DF["Product 1"]
#print(itemCount)
itemCount = itemCount.append(retail_DF["Product 2"])
#print(itemCount)
itemCount = itemCount.append(retail_DF["Product 3"])
#print(itemCount)
itemCount = itemCount.append(retail_DF["Product 4"])
#print(itemCount)
itemCount = itemCount.append(retail_DF["Product 5"])
#print(itemCount)
itemCount = itemCount.append(retail_DF["Product 6"])
#print(itemCount)
itemCount = itemCount.append(retail_DF["Product 7"])
#print(itemCount)

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


itemsetNum = 2
end = False
exists = True

#commencing the algorithm after first finding the freq item set manually
while loop == 1:
    newARR = []
    
    if itemsetNum >2:
        
        
        for sets in productARR:
            for items in sets:
                newARR.append(items)
                
        productARR = np.unique(newARR)
        print(productARR)
    newARR = []
    
    
   
    
    
    
    
    #creating combinations for the next table
    #itemset will be increasing as the 
    for subset in iter.combinations(productARR,itemsetNum):
        newARR.append(subset)
    productARR = newARR
    
    print(productARR)
    
    
    productSetCount= pd.Series(index = productARR)
    productSetCount.fillna(0, inplace = True)
    print(productSetCount)
    
    
    print("Counting itemsets")
        #iterates through the original dataframe counting the itemsets that produceSetCount has
    for itemset, count in productSetCount.iteritems():
        for row in retail_DF.itertuples():
            i = 0
            while i < len(itemset):
                if itemset[i] in row[2:9]:
                    exists = True
                else:
                    exists = False
                    break
                i = i+1
            if exists == True:
                #print(itemset[0] + " and " + itemset[1] + " exist in")
                #print(row)
                count = count + 1
                
        productSetCount.loc[itemset] = count
        #productSetCount.set_value(itemset,count)
    print(productSetCount)
            
    productARR = []
    
    
    
            
            
    
    
        
    for index, row in productSetCount.iteritems():
        if row/totalTrans < minSupport:
            print("Dropping ")
            print(index)
            productSetCount.drop(labels=[index], inplace=True)
        else:
            productARR.append(index)
            i = i+1       
            
            
            
    print(productSetCount)
    frequentSetTotal = frequentSetTotal.append(productSetCount)
    print("Total set: ")
    print(frequentSetTotal)
    print(productARR)
    
    
            
    
    itemsetNum = itemsetNum + 1
    
    if itemsetNum == 5:
        
        loop = 0
        
