import pandas as pd 

data = pd.DataFrame({
    "Age": [25, 30, 35, 40, 45],
    "Salary": [50000, 60000, 70000, 80000, 90000]
})  

mean_age = data['Age'].mean()
mean_salary = data['Salary'].mean()
std_age = data['Age'].std()
std_salary = data['Salary'].std()

data['Age'] = (data['Age'] - mean_age) / std_age
data['Salary'] = (data['Salary'] - mean_salary) / std_salary

print(data)