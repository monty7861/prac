import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori

# Load the dataset (update the file path)
# Ensure that you specify the correct file path to your dataset.
# Also, make sure that the CSV file is in the specified location.
ds = pd.read_csv("C:\\Users\\Mamush\\Desktop\\web service\DA\\External_prac_prep\\External DA\\data.csv", header=None)

# Convert the dataset to a list of transactions
transactions = []
for i in range(len(ds)):
    transactions.append([str(ds.values[i, j]) for j in range(len(ds.columns))])

# Perform Apriori
association_rules = apriori(transactions, min_support=0.1, min_confidence=0.5, min_lift=1.0, min_length=2)
association_results = list(association_rules)

for item in association_results:
    pair = item[0]
    items = [x for x in pair]
    print("Items: " + str(items))
    print("Support: " + str(item[1]))
    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("=====================================")
