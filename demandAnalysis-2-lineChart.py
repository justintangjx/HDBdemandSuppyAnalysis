# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import numpy as np
import matplotlib.pyplot as plt
import os

title = "Data cleaning of applications (2007 - 2018)"
os.getcwd()

data = np.genfromtxt('./applications-registered-for-resale-flats-and-rental-flats.csv', delimiter=",", skip_header=1, dtype=[('financial_year', 'U10'), ('type', 'U50'), ('applications_registered', 'i8')])
# print(data)

x_resale = data[data['type'] == 'resale']['financial_year']
y_resale = data[data['type'] == 'resale']['applications_registered']

x_rental = data[data['type'] == 'rental']['financial_year']
y_rental = data[data['type'] == 'rental']['applications_registered']

fig = plt.figure()
ax1 = fig.add_subplot(111)

ax1.plot(x_resale, y_resale, c='b',  label='Resale')
ax1.plot(x_rental,y_rental, c='r', label='Rental')
plt.ylabel('Number of applications')
plt.legend(loc='upper right');

plt.show()

