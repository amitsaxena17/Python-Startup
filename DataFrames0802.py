import numpy as np
import os
import pandas as pd

from matplotlib import pyplot as plt

os.system('cls')

datasaurus = pd.read_table(r'C:\Users\sax38974\.PyCharmCE2019.2\config\scratches\Data Science Pre-Con Data Files\DatasaurusDozen.tsv')
print(datasaurus.head())

print(datasaurus['dataset'].unique())

dino = datasaurus.loc[datasaurus['dataset'] == 'dino']
#print(dino)
#
# print(dino.describe())
#
# print('Dino Mean X: ' + str(np.mean(dino['x'])))
# print('Dino Mean Y: ' + str(np.mean(dino['y'])))
# print('Dino StDev X: ' + str(np.std(dino['x'])))
# print('Dino StDev Y: ' + str(np.std(dino['y'])))
# print('Dino Correlation: ' + str(np.corrcoef(dino['x'], dino['y'])))
#
# plt.scatter(x = dino['x'], y = dino['y'])
# plt.title('Dino Dataset')
# plt.show()
# plt.clf()
#
#
# slant_up = datasaurus.loc[datasaurus['dataset'] == 'slant_up']
# #print(slant_up)
#
# print(slant_up.describe())
#
# plt.scatter(x = slant_up['x'], y = slant_up['y'])
# plt.title('Slant Up Dataset')
# plt.show()
# plt.clf()
#
#
# print('Slant Up Mean X: ' + str(np.mean(slant_up['x'])))
# print('Slant Up Mean Y: ' + str(np.mean(slant_up['y'])))
# print('Slant Up StDev X: ' + str(np.std(slant_up['x'])))
# print('Slant Up StDev Y: ' + str(np.std(slant_up['y'])))
# print('Slant Up Correlation: ' + str(np.corrcoef(slant_up['x'], slant_up['y'])))

stats = datasaurus.groupby('dataset').describe().unstack(1)
print(stats)
#
fig = plt.figure()

dino_plt = fig.add_subplot(4, 4, 1)
dino_plt.scatter(x = datasaurus.loc[datasaurus['dataset'] == 'dino', 'x'], y = datasaurus.loc[datasaurus['dataset'] == 'dino', 'y'])

away_plt = fig.add_subplot(4, 4, 2)
away_plt.scatter(x = datasaurus.loc[datasaurus['dataset'] == 'away', 'x'], y = datasaurus.loc[datasaurus['dataset'] == 'away', 'y'])

h_lines_plt = fig.add_subplot(4, 4, 3)
h_lines_plt.scatter(x = datasaurus.loc[datasaurus['dataset'] == 'h_lines', 'x'], y = datasaurus.loc[datasaurus['dataset'] == 'h_lines', 'y'])

v_lines_plt = fig.add_subplot(4, 4, 4)
v_lines_plt.scatter(x = datasaurus.loc[datasaurus['dataset'] == 'v_lines', 'x'], y = datasaurus.loc[datasaurus['dataset'] == 'v_lines', 'y'])

x_shape_plt = fig.add_subplot(4, 4, 5)
x_shape_plt.scatter(x = datasaurus.loc[datasaurus['dataset'] == 'x_shape', 'x'], y = datasaurus.loc[datasaurus['dataset'] == 'x_shape', 'y'])

star_plt = fig.add_subplot(4, 4, 6)
star_plt.scatter(x = datasaurus.loc[datasaurus['dataset'] == 'star', 'x'], y = datasaurus.loc[datasaurus['dataset'] == 'star', 'y'])

high_lines_plt = fig.add_subplot(4, 4, 7)
high_lines_plt.scatter(x = datasaurus.loc[datasaurus['dataset'] == 'high_lines', 'x'], y = datasaurus.loc[datasaurus['dataset'] == 'high_lines', 'y'])

dots_plt = fig.add_subplot(4, 4, 8)
dots_plt.scatter(x = datasaurus.loc[datasaurus['dataset'] == 'dots', 'x'], y = datasaurus.loc[datasaurus['dataset'] == 'dots', 'y'])

circle_plt = fig.add_subplot(4, 4, 9)
circle_plt.scatter(x = datasaurus.loc[datasaurus['dataset'] == 'circle', 'x'], y = datasaurus.loc[datasaurus['dataset'] == 'circle', 'y'])

bullseye_plt = fig.add_subplot(4, 4, 10)
bullseye_plt.scatter(x = datasaurus.loc[datasaurus['dataset'] == 'bullseye', 'x'], y = datasaurus.loc[datasaurus['dataset'] == 'bullseye', 'y'])

slant_up_plt = fig.add_subplot(4, 4, 11)
slant_up_plt.scatter(x = datasaurus.loc[datasaurus['dataset'] == 'slant_up', 'x'], y = datasaurus.loc[datasaurus['dataset'] == 'slant_up', 'y'])

slant_down_plt = fig.add_subplot(4, 4, 12)
slant_down_plt.scatter(x = datasaurus.loc[datasaurus['dataset'] == 'slant_down', 'x'], y = datasaurus.loc[datasaurus['dataset'] == 'slant_down', 'y'])

wide_lines_plt = fig.add_subplot(4, 4, 13)
wide_lines_plt.scatter(x = datasaurus.loc[datasaurus['dataset'] == 'wide_lines', 'x'], y = datasaurus.loc[datasaurus['dataset'] == 'wide_lines', 'y'])

plt.show()
plt.clf()

#https://en.wikipedia.org/wiki/Anscombe%27s_quartet
# http://greenteapress.com/thinkstats/
# https://www.amazon.com/Python-Data-Analysis-Wrangling-IPython-ebook/dp/B075X4LT6K
# https://www.amazon.com/Python-Data-Analytics-Fabio-Nelli/dp/1484209591
# DataCamp
# Kaggle