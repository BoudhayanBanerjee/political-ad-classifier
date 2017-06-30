import pickle
import webcolors
import numpy as np
import matplotlib.pyplot as plt


with open('../templates/dominantColorP.pickle', 'rb') as f:
    color = pickle.load(f)

colors = [key for key, value in color.items()]
colors = ['#FDF5E6' if x == 'white' else x for x in colors]
plt.title('Dominant Colors in Political Ads')
plt.ylabel('Number of Ads')
plt.xlabel('Dominant Colors')
plt.bar(range(len(color)), color.values(), align='center', color=colors)
plt.xticks(range(len(color)), list(color.keys()), rotation=70)

plt.show()
