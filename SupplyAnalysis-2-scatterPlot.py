# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import numpy as np
import matplotlib.pyplot as plt
import os

title = "Number of flats constructed (1977 - 2017)"
os.getcwd()

data = np.genfromtxt('./flats-constructed-by-housing-and-development-board-annual.csv', delimiter=",", skip_header=1, dtype=[('year', 'U10'), ('flats_constructed', 'i8')] )

# print(data)

cleanedData = []
for i in data:
    if int(i['year']) > 2006:
        cleanedData.append(i)
parsedData = np.array(cleanedData)
# print(parsedData)

x_year = parsedData['year']
y_count = parsedData['flats_constructed']

fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.scatter(x_year , y_count , s=25, c='black', marker="*", label='flats constructed')

plt.legend(loc='upper left')

plt.show()


# %%


