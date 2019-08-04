import numpy as np
import os
import pandas as pd

os.system('cls')
#read from a data file
datasaurus = pd.read_table(r'C:\Users\sax38974\.PyCharmCE2019.2\config\scratches\Data Science Pre-Con Data Files\DatasaurusDozen.tsv', sep='\t')
# print from the first 5 records
print(datasaurus.head())
#
# #	Run as spaced
# # copy first records into a new array
print('Print first 5 records')
ds = datasaurus.head()
 # Print first 5 rows
print(ds.x)
#
# # Print first column
print('Print first column')
print(ds['x'])
#
# # Print
print('ds[[x]] with two braces is same as ds[x]')
print(ds[['x']])
#
print('print columns by names')
print(ds[['x', 'y']])
#
#
# #	Run each print separately
#
print('print rows by Indexes - Loc returns Actual Location - Returns difference of records. from 138 to 145')
print(datasaurus[138:146])
#
# print('print rows by Indexes -Loc returns difference of records included last - from 138 to 146')
print(datasaurus.loc[138:146])
#
print('print rows by Indexes -iLoc is Relative and returns difference of records included last - from 138 to 145')
print(datasaurus.iloc[138:146])
#
#
# #	Run each print separately
print(datasaurus.loc[138, 'x'])
print(datasaurus.loc[138:146, 'x'])
print(datasaurus.loc[138:146, ['x', 'y']])
print(datasaurus.iloc[138:146, [1, 2]])

print('Drop rows from 0 to 9')
datasaurus.drop([0,1,2,3,4,5,6,7,8,9], inplace=True)
print(datasaurus)

#	Run as spaced
standings = pd.DataFrame()
standings['City'] = ['Chicago', 'Colorado', 'Dallas', 'Minnesota', 'Nashville', 'St. Louis', 'Winnipeg']
standings['Team'] = ['Blackhawks', 'Avalanche', 'Stars', 'Wild', 'Predators', 'Blues', 'Jets']
standings['Wins'] = [32, 33, 38, 34, 42, 39, 44]
standings['Losses'] = [31, 29, 30, 31, 27, 27, 26]
standings['OvertimeLosses'] = [10, 12, 6, 9, 6, 8, 4]
print(standings)

losses = standings['Losses']
print(standings[losses >= 30])

#   print(standings[losses >= 29 and losses < 31])
mediocre_teams = np.logical_and(losses >= 29, losses < 31)
print(standings[mediocre_teams])