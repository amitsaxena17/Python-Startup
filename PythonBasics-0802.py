import os
os.system('cls');

# How to Comment  - Use #. Also Use Ctrl + /
# Hello World
print("Hello World!")

# Some Comparisons
print (2>1)
print(1>2)
print(2==2)

# Create a list for Teams- They look like Arrays
cities= ['Chicago','Colorado','Dallas','Minnesota','Nashville','St. Louis','Winnipeg']
teams = ['BlackHawks','Avalanche','Stars','Wild','Predators','Blues','Jets']
wins=[32,33,38,34,42,39,44]
losses=[31,29,30,31,27,27,26]
ot_losses=[10,12,6,9,6,8,4]

#Print this list
print(cities)
print('\n')

# First item
print(cities[0] +  ' ' + teams[0])

# Range of Array Items. Look at the difference of Ranges
# print(wins[1:3])
# #Last Item
# print(losses[-1])
# print (teams[3:])
# print(teams[:3])


#When you assign a new array, it creates a new array. However this is by Reference only. Any changes to new array would make changes to original array
# So, in order to create a new copy, use List command.
print([teams])
print('\n')

team_names=list(teams)
team_names[3]='North Stars'
print(teams)
print(team_names)