import pandas as pd 

data = pd.DataFrame({
    "Age": [25, 30, 35, 40, 45],
    "Salary": [50000, 60000, 70000, 80000, 90000]
})  

data['Age'] = (data['Age'] - data['Age'].min()) / (data['Age'].max() - data['Age'].min())

data['Salary'] = (data['Salary'] - data['Salary'].min()) / (data['Salary'].max() - data['Salary'].min())

print(data)