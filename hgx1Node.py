import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

plt.style.use('_mpl-gallery')

dataghx = np.genfromtxt ('data/ghx1Node.csv', delimiter=",")
# make data
x = np.linspace(0, 10, 100)
y = 4 + 2 * np.sin(2 * x)

# plot
fig, ax = plt.subplots()
mpl.style.use('seaborn-v0_8')

oneNodeoneGPU = dataghx[np.where(dataghx[:, 4] == 1)]
oneNodetwoGPUs = dataghx[np.where(dataghx[:, 4] == 2)]
oneNodefourGPUs = dataghx[np.where(dataghx[:, 4] == 4)]
oneNodeeightGPUs = dataghx[np.where(dataghx[:, 4] == 8)]


ax.plot(oneNodefourGPUs[:, 0], oneNodeoneGPU[:, 5],  label='1 GPUs', color='b')
ax.plot(oneNodefourGPUs[:, 0], oneNodetwoGPUs[:, 5], label='2 GPUs', color='r')
ax.plot(oneNodefourGPUs[:, 0], oneNodefourGPUs[:, 5],  label='4 GPUs', color='g')
ax.plot(oneNodefourGPUs[:, 0], oneNodeeightGPUs[:, 5],  label='8 GPUs', color='y')

ax.legend()

plt.show()
