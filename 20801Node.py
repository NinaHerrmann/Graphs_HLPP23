import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery')

data2080 = np.genfromtxt ('data/20801Node.csv', delimiter=",")
# make data
x = np.linspace(0, 10, 100)
y = 4 + 2 * np.sin(2 * x)

# plot
fig, ax = plt.subplots()

oneNodeoneGPU = data2080[np.where(data2080[:, 4] == 1)]
oneNodetwoGPUs = data2080[np.where(data2080[:, 4] == 2)]
oneNodefourGPUs = data2080[np.where(data2080[:, 4] == 4)]
oneNodeeightGPUs = data2080[np.where(data2080[:, 4] == 8)]
print(oneNodefourGPUs[:, 0])

ax.plot(oneNodefourGPUs[:, 0], oneNodeoneGPU[:, 5],  label='1 GPUs', color='b')
ax.plot(oneNodefourGPUs[:, 0], oneNodetwoGPUs[:, 5], label='2 GPUs', color='r')
ax.plot(oneNodefourGPUs[:, 0], oneNodefourGPUs[:, 5],  label='4 GPUs', color='g')
ax.plot(oneNodefourGPUs[:, 0], oneNodeeightGPUs[:, 5],  label='8 GPUs', color='y')

ax.legend()
plt.show()
