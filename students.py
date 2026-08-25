import numpy as np
import pandas as pd

marks = np.array([
    [85, 80, 90],
    [70, 75, 65],
    [92, 88, 95],
    [60, 72, 68],
    [78, 82, 80]
])

print("Marks:")
print(sum(marks))
#averge marks of each student

avg_each = np.mean(marks,axis=1)
print("\navg marks:")
print(avg_each)
#each subject
print(np.mean(marks, axis=0)) 
#highest score
print(np.max(marks,axis=0))
#lowest marks
print(np.min(marks,axis=0))
#avg more 80
print(np.where(avg_each >80))
#pass orfail
print(np.where(avg_each >=90,"Pass","fail"))



