import numpy as np;
salary = np.array([     
    [25000, 2, 80],     
    [45000, 5, 90],     
    [30000, 3, 75],     
    [60000, 8, 95],     
    [35000, 4, 85]
])
#average salary of all employees
print(np.mean(salary[:, 0]))
#max salary of all employees
print(np.max(salary[:, 0]))
#min salary of all employees
print(np.min(salary[:, 0]))
#average experience of all employees
print(np.mean(salary[:, 1]))
#salary greater than 40000
print(np.where(salary[:, 0] > 40000))
#performance greater than 80
print(np.where(salary[:, 2] > 80))
#highest performance score
print(np.where(salary[:, 2] == np.max(salary[:, 2])))
#standard deviation of salary
print(np.std(salary[:, 0]))
#high or low salary
print(np.where(salary[:, 0] > 40000, "High Salary", "Low Salary"))
#convert result to dataframe
import pandas as pd
result_df = pd.DataFrame(salary, columns=['Salary', 'Experience', 'Performance'])
print(result_df)