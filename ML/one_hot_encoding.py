import pandas as pd

data = pd.DataFrame({
    'City': ['Delhi', 'Mumbai', 'Chennai', 'Delhi']
})

# Step 1: get unique categories
cities = data['City'].unique()

# Step 2: create new columns
for city in cities:
    data[f'City_{city}'] = (data['City'] == city).astype(int)

# Step 3: drop original column
data = data.drop('City', axis=1)

print(data)
