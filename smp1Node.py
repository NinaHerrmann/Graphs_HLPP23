import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery')

data2080 = np.genfromtxt ('data/smp.csv', delimiter=";")

# plot
fig, ax = plt.subplots()

onenode96threads = data2080[np.where(data2080[:, 3] == 96)]
onenode32threads = data2080[np.where(data2080[:, 3] == 32)]
onenode64threads = data2080[np.where(data2080[:, 3] == 64)]
onenode16threads = data2080[np.where(data2080[:, 3] == 16)]
onenode48threads = data2080[np.where(data2080[:, 3] == 48)]
onenode80threads = data2080[np.where(data2080[:, 3] == 80)]
onenode112threads = data2080[np.where(data2080[:, 3] == 112)]
onenode128threads = data2080[np.where(data2080[:, 3] == 128)]

print(plt.rcParams['axes.prop_cycle'].by_key()['color'])
ax.plot(onenode32threads[:, 0], onenode16threads[:, 5],  label='16 Threads', color='g', linestyle='dashed', marker='.')
ax.plot(onenode32threads[:, 0], onenode32threads[:, 5],  label='32 Threads', color='b', marker='.')
ax.plot(onenode32threads[:, 0], onenode48threads[:, 5],  label='48 Threads', color='y', linestyle='dashed', marker='.')
ax.plot(onenode32threads[:, 0], onenode64threads[:, 5], label='64 Threads', color='r', marker='.')
ax.plot(onenode32threads[:, 0], onenode80threads[:, 5],  label='80 Threads', color='b', linestyle='dashed', marker='.')
ax.plot(onenode32threads[:, 0], onenode96threads[:, 5],  label='96 Threads', color='g', marker='.')
ax.plot(onenode32threads[:, 0], onenode112threads[:, 5],  label='112 Threads', color='r', linestyle='dashed', marker='.')
ax.plot(onenode32threads[:, 0], onenode128threads[:, 5],  label='128 Threads', color='y', marker='.')

ax.legend()
plt.show()
