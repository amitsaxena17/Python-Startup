import numpy as np
import os

os.system('cls')


#	Set all values together
cities = np.array(['Chicago', 'Colorado', 'Dallas', 'Minnesota', 'Nashville', 'St. Louis', 'Winnipeg'])
teams = np.array(['Blackhawks', 'Avalanche', 'Stars', 'Wild', 'Predators', 'Blues', 'Jets'])
wins = np.array([32, 33, 38, 34, 42, 39, 44])
losses = np.array([31, 29, 30, 31, 27, 27, 26])
ot_losses = np.array([10, 12, 6, 9, 6, 8, 4])


#	Run each print separately
print('Cities-')
print(cities)
print(cities[0] + ' ' + teams[0])
print(wins[1:3])
print(losses[-1])
print(teams[3:])
print(teams[:3])


#	Run as spaced
games_played = wins + losses + ot_losses
print('games played-')
print( games_played)

points = 2 * wins + ot_losses
winning_percentage = (points / 2) * games_played
print('Winning%-')
print(winning_percentage)


#	Run each print separately
print('Loss>=30')
print(losses >= 30)
print(losses[losses >= 30])
print(teams[losses >= 30])


#	Run as spaced
values = [True, 1, False, 0]
print(values)

values_array = np.array(values)
print(values_array)


#	Run as spaced
record = np.array([[32, 31, 10],
                   [33, 29, 12],
                   [38, 30, 6],
                   [34, 31, 9],
                   [42, 27, 6],
                   [39, 27, 8],
                   [44, 26, 4]])
print('Records-')
print(record)

wins = np.array([32, 33, 38, 34, 42, 39, 44])
losses = np.array([31, 29, 30, 31, 27, 27, 26])
ot_losses = np.array([10, 12, 6, 9, 6, 8, 4])

# This would provide 3rd record's 2 item. Notice 30 in [38,30,6]
print(record[2, 1])

# this will further create a list. Now we are summing up different columns and then pushing that into a new array.
games_played = record[:,0] + record[:,1]
print(games_played)


#	Run each print separately
# this will add mean to all the Array.
print(np.mean(wins))
print('Mean Wins: ' + str(np.mean(wins)))
print('Median Wins: ' + str(np.median(wins)))
print('Most wins:' + str(np.max(wins)))
print(teams[wins == np.max(wins)])

# Correlation Matrix
correlation = np.corrcoef(record[:,0], record[:,1])
print('Correlation: ' + str(correlation))

#Test