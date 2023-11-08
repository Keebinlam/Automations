import pandas as pd

#Extracting a CVS file from a website.
url = 'https://www.football-data.co.uk/mmz4281/2324/E0.csv'
df = pd.read_csv(url)


# renaming 2 columns 
df.rename(columns={'FTHG': 'Final Time Home Goals',
          'FTAG': 'Final Time Away Goals'}, inplace=True)
#showing table with new columns 
print(df)
