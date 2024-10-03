import pandas as pd 

lst = [
    ["John", "Doe", 25],
    ["Jane", "Doe", 22],
    ["John", "Smith", 30],
    ["Jane", "Smith", 27]
]

df = pd.DataFrame(lst, columns = ['FirstName', 'LastName', 'Age'])

columns = ['Name', 'Surname', 'Age']

data = pd.DataFrame(lst, columns = columns)
print(df)
print(data)