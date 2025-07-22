import numpy as np
import pandas as pd
import math

def gradient_descent(x,y):
    m_curr = b_curr = 0
    n = len(x)
    learning_rate = 0.0002
    converge = False
    i = 0
    prev_cost = 0

    while converge == False:
        y_predicted = m_curr * x + b_curr
        cost = (1/n) * sum([val**2 for val in (y-y_predicted)])
        md = -(2/n)*sum(x*(y-y_predicted))
        bd = -(2/n)*sum(y-y_predicted)
        m_curr = m_curr - learning_rate * md
        b_curr = b_curr - learning_rate * bd
        print ("m {}, b {}, cost {} iteration {}".format(m_curr,b_curr,cost, i))

        if math.isclose(prev_cost,cost,rel_tol= 1e-20) == True:
            converge = True
    
        prev_cost = cost
        i += 1


df= pd.read_csv('test_scores.csv')

x = df.math
y = df.cs

gradient_descent(x,y)