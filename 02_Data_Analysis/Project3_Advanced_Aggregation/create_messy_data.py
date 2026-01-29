import pandas as pd
import numpy as np

# Create a dictionary with messy data
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Alice"],
    "Age": [25, 300, 35, 40, 28, 300, 45, 25],  # Note the 300s
    "City": [
        "new york",
        "New York",
        "Los Angeles",
        "chicago",
        "Chicago",
        "Boston",
        "boston",
        "new york",
    ],  # Inconsistent casing
    "Amount": [
        "$100",
        "$200",
        np.nan,
        "$50",
        "$10",
        "$1000",
        "$20",
        "$100",
    ],  # Strings with $ and a missing value
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV in the data folder
# Make sure the 'data' folder exists first!
df.to_csv("cleaning_practice.csv", index=False)


df["Amount"] = df["Amount"].str.replace("$", "")
