# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 19:40:53 2020

@author: peter
"""
from itertools import chain, combinations
import itertools as iter
import numpy as np
import pandas as pd






#this function is used for genreating rules from final itemsets
#lots of declarations of empty lists as i was having issues with variable types
#issues with datatypes in dataframes prevalent all over the prject, but most are now solved

#support functions created by Nikola Popadic
def list_subtract(sub,main):
    
    subArray = []
    mainArray = []
    subArray = np.array(sub)
    subArray = subArray.tolist()
    mainArray = np.array(main)
    mainArray = mainArray.tolist()
    
    i = 0
    answer = [] 
    #goes through the 2^k -2 subsets from the final itemsets
    #by the end of this loop l-s will be returned from the equation s-->(l-s)
    #sub represents s and main represents l 
    while i < len(subArray):
        
        index = 0
        
        if subArray[i] in mainArray:
           
            
            if i>=1:
                index = answer.index(subArray[i])
                
                answer = answer[:index] + answer[index+1:]
                
            else:
                index = mainArray.index(subArray[i])
               
                answer = mainArray[:index] + mainArray[index+1:]
                
        i = i+1
    


   
    return answer
            
    #will return a powerset used for rule generation iterable being any itemset that needs to be split up into subsets
def powerset(iterable):
    "list(powerset([1,2,3])) --> [(), (1,), (2,), (3,), (1,2), (1,3), (2,3), (1,2,3)]"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))






#driver code and algorithm
#initial hot_encode of first iterations made by Peter Mykulak

totalTrans = 315
minSupportCount = 60 #lowest amount of a single product that was bought gotten ahead of time
minSupport = minSupportCount/totalTrans
minConfidence = 0.60
        #this is just the path to the dataset location   
retail = 'https://raw.githubusercontent.com/myku5980/465_final_proj/master/retail_dataset.csv'
#creates dataframe from dataset csv
retail_DF = pd.read_csv(retail)
#creates series table that counts frequency of itemsets that can also be pruned alter
frequentSetTotal = pd.Series()
print(retail_DF)


#i make a new dataframe to facilitate counting 
#allows me to stack columns over each other so i can count all items from one coloumn
#i use the append command that comes with pandas
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
#productARR will allow us to hold a list of items used in the subsets found in the frequentItemSet table
productARR = []
i = 0


#the for loop below goes through the item frequency series and drops the item not meeting the min support threshold

#pruning blocks developed by Nikola Popadic
i = 0;
for index, count in ic.iteritems():
    
    if count/totalTrans < minSupport:
        
        print("Dropping " + index)
        
        ic.drop(labels=[index], inplace=True)
    else:
        
        productARR.append(index)
        i = i+1  
        
        

print(ic)
frequentSetTotal = frequentSetTotal.append(ic)
print("Frequency 1-itemset table has been pruned")

print(productARR)
loop = 1
print("creating combinations for 2 itemset table")


itemsetNum = 2
end = False
exists = True

#commencing the algorithm after first finding the freq item set manually
#main loop algorithm created by Peter Mykulak
while loop == 1:
    newARR = []
    
    if itemsetNum >2:
        
        
        for sets in productARR:
            for items in sets:
                newARR.append(items)
                
        productARR = np.unique(newARR)
        print("This array is a collection of allitems used in the previous table")
        print(productARR)
    newARR = []
    
    
   
    
    
    
    
    #creating combinations for the next table
    #itemset will be increasing as the 
    for subset in iter.combinations(productARR,itemsetNum):
        newARR.append(subset)
    productARR = newARR
    
    #print(productARR)
    
    
    productSetCount= pd.Series(index = productARR)
    productSetCount.fillna(0, inplace = True)
    #print(productSetCount)
    
    
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
    
    
    
            
            
    #simle pruning of the function
    
    print("Comencing pruning")
    for index, row in productSetCount.iteritems():
        if row/totalTrans < minSupport:
            
            productSetCount.drop(labels=[index], inplace=True)
            print("Dropping: ", index)
        else:
            productARR.append(index)
            i = i+1       
            
            
            #once pruning is finished the productsetcount table will be appeneded to the frequent total table to be used at the end for rule generation
    print(productSetCount)
    frequentSetTotal = frequentSetTotal.append(productSetCount)
    print("This series table holds all Freequent sets derived from previous k+1 itemsets  ")
    print(frequentSetTotal)
    #print(productARR)
    
    
            
    
    itemsetNum = itemsetNum + 1
    
    if productSetCount.empty == True:
        itemsetNum = itemsetNum - 1
        loop = 0
        
print("Gathering association rules")

itemSetLength = itemsetNum - 1
#print(itemSetLength)

amountOfRules = 2**itemSetLength - 2
#print(amountOfRules)
itemSetRuleARR = []
for itemset, amount in frequentSetTotal.iteritems():
    if len(itemset) == 3:
        itemSetRuleARR.append(itemset)
#print(itemSetRuleARR)
i = 0
j = 0
n = 0;
res = []
res1 = []
res2 = []
itemRule = []
itemRule = np.asarray(itemSetRuleARR)
print
print("fetching Sets to be used for rule generation ")
print(itemRule)

#accositation rules will begin to be created below
while i < len(itemSetRuleARR): #length of array carrying all our itemsets used for rule generation
    rules = pd.DataFrame(columns = ['item','withProd','conf','minConf','rule'])
    
    print("forming rules for: ",itemRule[i])
    #creates power sets
    #print("Relevant sub sets: ")
    sublist = list(powerset(itemRule[i]))
    res = np.asarray(sublist[0:len(sublist)-1])
    res = np.delete(res,0)
    
    withProd = []
    
   
    #final association rule block done by Peter Mykulak
    j = 0
    while j < len(res):
        y = 0
        #print("test1")
        #fills arrToDel to be used as s in the formula s->(l-s)
        #itemRule[i]  repesnts l
        arrToDel = []
        while y < len(res[j]):
            arrToDel.append(res[j][y])    
            
            y = y+1
        #print(arrToDel)
        x = 0
        rule = 'yes'
        wpSupport = 0
        iSupport = 0
        #subtracts arrtoDell from itemrule[i] using the formula arrToDel->(itemrule[i]-arrtodel)
        withProd = list_subtract(arrToDel,itemRule[i])   
        itemSet = (arrToDel)
        print(itemSet,"->",withProd)
       
        j = j+1
        
        
        
        
        
            
    i += 1
    
