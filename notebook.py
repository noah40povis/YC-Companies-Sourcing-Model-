import pandas as pd 
df = pd.read_csv('yc_list.csv')
'''reading columns''' 
df.columns
'''dropping columns'''
df.drop( ['Unnamed: 0', 'Unnamed: 0.1'], axis =1, inplace=True)
'''converting nan to active in status column'''
df['Status'].fillna('active', inplace=True)
df['Status'].value_counts()

