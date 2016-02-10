import csv
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import seaborn

my_v = []
my_a = []
my_d = []

with open('outputsw.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        if row[-3] != 'v':
            my_v.append(float(row[-3]))
            my_a.append(float(row[-2]))
            my_d.append(float(row[-1]))

bins = np.arange(0, 10, 0.25)
plt.hist(my_d, bins=bins, alpha=0.5)
plt.title('Star Wars: Dominance')
plt.show()