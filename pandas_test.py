import pandas as pd

df = pd.DataFrame({ 
    "Name" : ["Braund, Mr. Owen Harris","Allen, Mr. William Henry","Bonnell, Miss. Elizabeth"],
    "Age": [22, 35, 58],
    "Sex" : ["male", "male", "female"]}
)
# print(df)
# print(df["Name"])
# print(df["Age"])
# print(df["Sex"])

new_df = df["Name"]
# print(new_df)

# print(df.max())
# print(df.describe())

sample = pd.read_excel(io= , sheet_name=0, header=0, index_col=0)
print(sample)