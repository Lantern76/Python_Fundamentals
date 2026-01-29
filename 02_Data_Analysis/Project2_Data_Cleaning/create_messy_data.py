import pandas as pd
import numpy as np

# Create a dictionary with messy data
data = {
    "Transaction_ID": [101, 102, 103, 103, 105, 106],
    "Customer_Name": ["Alice", "Bob", "Charlie", "Charlie", "Eve", None],
    "Amount": ["$500", "200", "300.50", "300.50", "ERROR", "450"],
    "Age": [25, 300, 35, 35, 40, 22],
    "City": ["New York", "new york", "Boston", "Boston", "Chicago", "Chicago"],
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("cleaning_practice.csv", index=False)

print("Messy dataset 'cleaning_practice.csv' created successfully!")
