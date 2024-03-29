import numpy as np
import os
import pandas as pd

from matplotlib import pyplot as plt

os.system('cls')
#
population = pd.read_csv(r'C:\Users\sax38974\.PyCharmCE2019.2\config\scratches\Data Science Pre-Con Data Files\Total_Population.csv')
# print(population.head())
#
# plt.hist(population['2017'], bins = 10)
# plt.show()
# plt.clf()
# #
# plt.hist(population['2018'], bins = 10, facecolor = 'red', alpha = 1)
# plt.title('Population Distribution By Country')
# plt.xlabel('Population in Billions')
# plt.show()
# plt.clf()
# #
#
life_expectancy = pd.read_csv(r'C:\Users\sax38974\.PyCharmCE2019.2\config\scratches\Data Science Pre-Con Data Files\Life_Expectancy.csv')
# print(life_expectancy.head())
#
# #plt.hist(life_expectancy['2018'], bins = 10)
# plt.hist(life_expectancy['2018'].dropna(), bins = 10)
# plt.show()
# plt.clf()
#
# plt.hist(life_expectancy['2018'].dropna(), bins = 10, facecolor = 'red', alpha = 1)
# plt.title('Life Expectancy Distribution By Country')
# plt.xlabel('Life Expectancy in Years')
# plt.show()
# plt.clf()
# # #
# print(life_expectancy.loc[life_expectancy['geo'] == 'United States'])
# us_life_expectancy = (life_expectancy.loc[life_expectancy['geo'] == 'United States']).T
# print(us_life_expectancy)
# us_life_expectancy.drop(us_life_expectancy.index[0], inplace = True)
# us_life_expectancy.columns = ['Life_Expectancy']
# print(us_life_expectancy)
#
# japan_life_expectancy = (life_expectancy.loc[life_expectancy['geo'] == 'Japan']).T
# japan_life_expectancy.drop(japan_life_expectancy.index[0], inplace = True)
# japan_life_expectancy.columns = ['Life_Expectancy']

# plt.plot(us_life_expectancy)
# plt.plot(japan_life_expectancy)
# # plt.show()
# # plt.clf()
#
# plt.plot(us_life_expectancy, label = 'United States')
# plt.plot(japan_life_expectancy, label = 'Japan')
# plt.xlabel('Year')
#
# plt.ylabel('Life Expectancy In Years')
# plt.xticks(['1800','1850','1900','1950','2000'])
# plt.legend(loc = 'upper center', shadow = True)
# plt.title('Life Expectancy Comparision')
# plt.show()

#
gdp_per_capita = pd.read_csv(r'C:\Users\sax38974\.PyCharmCE2019.2\config\scratches\Data Science Pre-Con Data Files\GDP_Per_Capita_Inflation_Adjusted.csv')
print(gdp_per_capita.head())
#
# plt.scatter( x = population['2018'],
#             y = gdp_per_capita['2018'])
# plt.show()
# plt.clf()

pop2018 = population[['geo', '2018']]
pop2018.set_index('geo', inplace = True, drop = True)
print(pop2018)
gdp2018 = gdp_per_capita[['geo', '2018']]
gdp2018.set_index('geo', inplace = True, drop = True)
# print(gdp2018)
# print(len(pop2018.index))
# print(len(gdp2018.index))
#
# pop_vs_gdp = pop2018.join(gdp2018, lsuffix = '_pop', rsuffix = '_gdp')
# print(pop_vs_gdp)
#
# plt.scatter(pop_vs_gdp['2018_pop'], pop_vs_gdp['2018_gdp'])
# plt.show()
# plt.clf()


life2018 = life_expectancy[['geo', '2018']]
life2018.set_index('geo', inplace = True, drop = True)
gdp_vs_life = gdp2018.join(life2018, lsuffix = '_gdp', rsuffix = '_life')
print(gdp_vs_life)
#
# plt.scatter(gdp_vs_life['2018_gdp'], gdp_vs_life['2018_life'])
# plt.title('GDP vs Life Expectancy')
# plt.xlabel('GDP in $M')
# plt.ylabel('Life Expectancy In Years')
# plt.show()
# plt.clf()
#
# #
# gdp_vs_life['2018_gdp_log'] = np.log(gdp_vs_life['2018_gdp'])
#
# plt.scatter(gdp_vs_life['2018_gdp_log'], gdp_vs_life['2018_life'])
# plt.title('GDP vs Life Expectancy')
# plt.xlabel('Log (base 10) of GDP in $M')
# plt.ylabel('Life Expectancy In Years')
# plt.show()
# plt.clf()
# #
#
# plt.scatter(gdp_vs_life['2018_gdp'], gdp_vs_life['2018_life'])
# plt.xscale('log')
# plt.title('GDP vs Life Expectancy')
# plt.xlabel('GDP per capita in USD')
# plt.ylabel('Life Expectancy In Years')
# plt.show()
# plt.clf()


plt.scatter(gdp_vs_life['2018_gdp'], gdp_vs_life['2018_life'])
plt.xscale('log')
plt.title('GDP vs Life Expectancy')
plt.xlabel('GDP per capita in USD')
plt.ylabel('Life Expectancy In Years')
plt.xticks([1000, 10000, 100000], ['1K', '10K', '100K'])
plt.show()
plt.clf()