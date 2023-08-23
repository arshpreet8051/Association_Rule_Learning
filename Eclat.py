# Note : we will change Apriori algorithm only to use it as Eclat
# Note : only Support plays an important role in Eclat

! pip install apyori

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('Market_Basket_Optimisation.csv',header=None) # header = None coz we have no 1st row for headings

transactions = [] # apyori demands list of strings
for i in range(0,7501):
  transactions.append([str(dataset.values[i,j]) for j in range(0,20)])

from apyori import apriori

# min_support = a item should occur atleast for thrice a week so -> 3*7 / 7500 = 0.003
# min_confidence = genrally below 0.8 is considered good , so -> 0.2
# min_lift = for relevant rules it's generally 3
# min & max length = 2 , coz we want to create buy one get one free like deals, association of only 2 items
rules = apriori(transactions=transactions,min_support = 0.003, min_confidence=0.2,min_lift=3,min_length=2,max_length=2)

results = list(rules)

results

# code snippet to convert rules in well mannered pandas dataframe
def inspect(results):
    lhs         = [tuple(result[2][0][0])[0] for result in results]
    rhs         = [tuple(result[2][0][1])[0] for result in results]
    supports    = [result[1] for result in results]
    support_percentage = [x*10000 for x in supports]
  
    return list(zip(lhs, rhs, supports, support_percentage))
resultsinDataFrame = pd.DataFrame(inspect(results), columns = ['One product', 'Another Product', 'Support', 'Support %'])

resultsinDataFrame

# using nlargest() function to sort dataframe on the basis of 'Support' column
resultsinDataFrame.nlargest(n=10,columns='Support')
