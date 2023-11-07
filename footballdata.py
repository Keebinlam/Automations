import pandas as pd

url = 'https://www.football-data.co.uk/mmz4281/2324/E0.csv'
df = pd.read_csv(url)
print(df)
