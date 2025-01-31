import pandas as pd

# Load the CSV file
df =  pd.read_csv("pred-inst.csv")

# Save as a .pkl file
df.to_pickle("pred-inst.pkl")

print("Pickle file saved")
