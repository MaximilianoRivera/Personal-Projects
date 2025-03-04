import pandas as pd
from pulp import *

#List of basic Nutrients
Nutrients = [
    "Calories (kcal)",
    "Protein (g)",
    "Calcium (g)",
    "Iron (mg)",
    "Vitamin A (KIU)",
    "Vitamin B1 (mg)",
    "Vitamin B2 (mg)",
    "Niacin (mg)",
    "Vitamin C (mg)"
]

#Directory of diet minimun nutrients requirements.
Nutrients_req = {
    "Calories (kcal)": 3,
    "Protein (g)": 70,
    "Calcium (g)": 0.8,
    "Iron (mg)": 12,
    "Vitamin A (KIU)": 5,
    "Vitamin B1 (mg)": 1.8,
    "Vitamin B2 (mg)": 2.7,
    "Niacin (mg)": 18,
    "Vitamin C (mg)": 75,
}

print(Nutrients_req['Calories (kcal)'])
#Read data and create list of ingredients and nutritional data
df = pd.read_csv('ingredients.csv')
Ingredients_list = df.iloc[:,0].values #list of ingredients
Price_list = df.iloc[:,2].values #list of ingredients prices
Nutritional_inf = df.iloc[:,3:].values # list of the ingredientes nutritional values

#Setting the problem variable
Diet = LpProblem('Diet',LpMinimize)

Ingredients_P = {n_f:round(Price_list[i]) for i,n_f in enumerate(Ingredients_list)}
Nutritional_val = {n_f:{n_t:round(Nutritional_inf[j][i]) for i,n_t in enumerate(Nutrients)} for j,n_f in enumerate(Ingredients_list)}

#Setting decision variables
Ingredients_amt = LpVariable.dicts('ingredients_amt',Ingredients_list,0,None,LpContinuous)


Diet += lpSum(Ingredients_amt[i]*Ingredients_P[i] for i in Ingredients_list) # Total cost of diet ingredients

#Amount of nutrients needed in diet
for i in (Nutrients):
    Diet += lpSum(Ingredients_amt[j]*round(Nutritional_val[j][i]) for j in Ingredients_list) >= Nutrients_req[i]    


#Solve LP and print solutions 
Diet.solve()
print('status:', LpStatus[Diet.status])

for v in Diet.variables():
    print (v.name,' = ',v.varValue)

print('Total cost of food for diet = ', value(Diet.objective))