# Apriori

! pip install apyori

# Importing the libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Data Preprocessing

dataset = pd.read_csv('Market_Basket_Optimisation.csv',header=None) # header = None coz we have no 1st row for headings

transactions = [] # apyori demands list of strings
for i in range(0,7501):
  transactions.append([str(dataset.values[i,j]) for j in range(0,20)])

# Training the Apriori model on the dataset

from apyori import apriori

# min_support = a item should occur atleast for thrice a week so -> 3*7 / 7500 = 0.003
# min_confidence = genrally below 0.8 is considered good , so -> 0.2
# min_lift = for relevant rules it's generally 3
# min & max length = 2 , coz we want to create buy one get one free like deals, association of only 2 items
rules = apriori(transactions=transactions,min_support = 0.003, min_confidence=0.2,min_lift=3,min_length=2,max_length=2)

# Visualising the results

# Displaying the first results coming directly from the output of the apriori function

results = list(rules)

results

# Putting the results well organised into a Pandas DataFrame

# code snippet to convert rules in wel mannered pandas dataframe
def inspect(results):
    lhs         = [tuple(result[2][0][0])[0] for result in results]
    rhs         = [tuple(result[2][0][1])[0] for result in results]
    supports    = [result[1] for result in results]
    support_percentage = [x*10000 for x in supports]
    confidences = [result[2][0][2] for result in results]
    confidences_percentage = [x*100 for x in confidences]
    lifts       = [result[2][0][3] for result in results]
    return list(zip(lhs, rhs, supports, support_percentage, confidences, confidences_percentage, lifts))
resultsinDataFrame = pd.DataFrame(inspect(results), columns = ['Left Hand Side', 'Right Hand Side', 'Support', 'Support %', 'Confidence', 'Confidence %', 'Lift'])

# Displaying the results non sorted

resultsinDataFrame

# Displaying the results sorted by descending lifts

# using nlargest() function to sort dataframe on the basis of 'Lift' column
resultsinDataFrame.nlargest(n=10,columns='Lift')
