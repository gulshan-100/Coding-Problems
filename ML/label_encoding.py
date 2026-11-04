import pandas as pd 

data = pd.DataFrame({
    "Gender" : ["Male", "Female", "Female", "Male", "Male"]
})

# Find the unique labels 
labels = data['Gender'].unique() 
print("Unique Labels:", labels)
print(len(labels))

# Create the mappings 
label_mapping = {label: idx for idx, label in enumerate(labels)}
print(label_mapping)

# Apply the mappings to encode the labels
data['Gender'] = data['Gender'].map(label_mapping)

print(data)