# creating a pivot table using python
import pandas as pd

df = pd.read_excel(
    # good practice to slim the columns by selecting what you want by rewriting the variable
    '/Users)
# if we want to select more than 1 column, you have to do double square brackets # if we want to select more than 1 column, you have to do double square brackets
df = df[['Gender', 'Product line', 'Total']]


# Index Y axis, Column is X axis, Value is crosspoints, aggfunc is the function across all cells
pivot_table = df.pivot_table(
    index='Gender', columns='Product line', values='Total', aggfunc='sum')
print(pivot_table)

pivot_table.to_excel('pivot_table.xlsx', 'Report', startrow=4)