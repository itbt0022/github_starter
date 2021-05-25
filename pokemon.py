# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'

# %%
import pandas as pd
import numpy as np

df = pd.read_csv('c:/Users/m226504/NASA Internship - Summer 2021/test/github_starter/pokemon_data.csv', encoding='utf-8')
#print(df.head(5))


# %%
'''
Reading Data
'''

## Read Headers
#df.columns

## Read each column
#print(df[['Name', 'Type 1', 'HP']])

## Read each row
#print(df.iloc[0:4])
#df.loc[df['Type 1'] == "Fire"]

## Read a specific location
#print(df.iloc[2,1])


# %%
'''
Sorting/Describing Data
'''

#df.sort_values(['Type 1', 'HP'], ascending=[1,0]) 
# Ascending: 1 = True, 0 = False


# %%
'''
Making Changes to Data
'''

#df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Def'] + df['Speed']

#df = df.drop(columns=['Total'])

df['Total'] = df.iloc[:, 4:10].sum(axis=1)
# Axis: 1 = adding horizontally, 0 = adding vertically

cols = list(df.columns.values)
df = df[cols[0:4] + [cols[-1]] + cols[4:12]]

df.head(5)


# %%
'''
Saving Changed Data
'''

df.to_csv('modified_pokemon_data.csv', index=False)


# %%
'''
Filtering Data
'''

#df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison')]
#df.loc[(df['Type 1'] == 'Grass') | (df['Type 2'] == 'Poison')]
# Use & for 'and' and | for 'or'

new_df = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 70)]

new_df.to_csv('filtered_pokemon_data.csv')

new_df.reset_index(drop=True, inplace=True)

new_df


# %%
'''
Filtering Data (contd.)
'''
import re

#df.loc[df['Name'].str.contains('Mega')]
# Only displays names that contain "Mega"

#df.loc[~df['Name'].str.contains('Mega')]
# Only displays names that DO NOT contain "Mega"

#df.loc[df['Type 1'].str.contains('fire|grass', flags=re.I, regex=True)]
# flags=re.I --> ignores cases of letters

#df.loc[df['Name'].str.contains('^pi[a-z]*', flags=re.I, regex=True)]
# only shows names of pokemon that start with 'pi' (^ forces beginning of name)


# %%
'''
Conditional Changes
'''

#df.loc[df['Type 1'] == 'Fire', 'Type 1'] = 'Flamer'
# Changes 'Fire' to 'Flamer'

#df.loc[df['Type 1'] == 'Fire', 'Legendary'] = True
# The only fire type pokemon to be shown will be legendary

df = pd.read_csv('modified_pokemon_data.csv')
df


# %%
'''
Aggregate Statistics (GroupBy)
'''

df = pd.read_csv('modified_pokemon_data.csv')
df

df.groupby(['Type 1']).mean().sort_values('Defense', ascending=False)


