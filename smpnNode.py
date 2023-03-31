import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors
from matplotlib.lines import Line2D

plt.style.use('ggplot')

onenodesmp = np.genfromtxt ('data/smp.csv', delimiter=";")
fournodessmp = np.genfromtxt ('data/smp4nodes.csv', delimiter=";")
twonodessmp = np.genfromtxt ('data/smp2nodes.csv', delimiter=";")
eightnodessmp = np.genfromtxt ('data/smp8nodes.csv', delimiter=";")


# plot
fig, ax = plt.subplots()

onenode96threads = onenodesmp[np.where(onenodesmp[:, 3] == 96)]
onenode32threads = onenodesmp[np.where(onenodesmp[:, 3] == 32)]
onenode32threads = onenode32threads[np.where(onenode32threads[:, 5] < 616)]
onenode64threads = onenodesmp[np.where(onenodesmp[:, 3] == 64)]
onenode16threads = onenodesmp[np.where(onenodesmp[:, 3] == 16)]
onenode16threads = onenode16threads[np.where(onenode16threads[:, 5] < 616)]
print(onenode16threads)
onenode128threads = onenodesmp[np.where(onenodesmp[:, 3] == 128)]

twonode96threads = twonodessmp[np.where(twonodessmp[:, 3] == 96)]
twonode32threads = twonodessmp[np.where(twonodessmp[:, 3] == 32)]
twonode64threads = twonodessmp[np.where(twonodessmp[:, 3] == 64)]
twonode16threads = twonodessmp[np.where(twonodessmp[:, 3] == 16)]
twonode128threads = twonodessmp[np.where(twonodessmp[:, 3] == 128)]

fournode96threads = fournodessmp[np.where(fournodessmp[:, 3] == 96)]
fournode32threads = fournodessmp[np.where(fournodessmp[:, 3] == 32)]
fournode64threads = fournodessmp[np.where(fournodessmp[:, 3] == 64)]
fournode16threads = fournodessmp[np.where(fournodessmp[:, 3] == 16)]
fournode128threads = fournodessmp[np.where(fournodessmp[:, 3] == 128)]

eightnode96threads = eightnodessmp[np.where(eightnodessmp[:, 3] == 96)]
eightnode32threads = eightnodessmp[np.where(eightnodessmp[:, 3] == 32)]
eightnode64threads = eightnodessmp[np.where(eightnodessmp[:, 3] == 64)]
eightnode16threads = eightnodessmp[np.where(eightnodessmp[:, 3] == 16)]
eightnode128threads = eightnodessmp[np.where(eightnodessmp[:, 3] == 128)]

colors = mcolors.CSS4_COLORS
print(plt.rcParams['axes.prop_cycle'].by_key()['color'])
colors = plt.rcParams['axes.prop_cycle'].by_key()['color']

ax.plot(onenode16threads[:, 0], onenode16threads[:, 5], color=colors[0], label='16 Threads',  linestyle='solid', marker='.')
ax.plot(onenode32threads[:, 0], onenode32threads[:, 5], color=colors[1], label='32 Threads', linestyle='solid', marker='.')
ax.plot(onenode64threads[:, 0], onenode64threads[:, 5], color=colors[2], label='64 Threads', linestyle='solid', marker='.')
ax.plot(onenode96threads[:, 0], onenode96threads[:, 5], color=colors[3], label='96 Threads',  linestyle='solid', marker='.')
ax.plot(onenode128threads[:, 0], onenode128threads[:, 5], color=colors[4], label='128 Threads',  linestyle='solid', marker='.')

#ax.plot(twonode16threads[:, 0], twonode16threads[:, 5],  label='16 Threads',  linestyle='dashed', marker='.')
#ax.plot(twonode32threads[:, 0], twonode32threads[:, 5],  label='32 Threads',   linestyle='dashed', marker='.')
#ax.plot(twonode64threads[:, 0], twonode64threads[:, 5], label='64 Threads',   linestyle='dashed', marker='.')
#ax.plot(twonode96threads[:, 0], twonode96threads[:, 5],  label='96 Threads',  linestyle='dashed', marker='.')
#ax.plot(twonode128threads[:, 0], twonode128threads[:, 5],  label='128 Threads',  linestyle='dashed', marker='.')

#ax.plot(fournode16threads[:, 0], fournode16threads[:, 5], color=colors[0],label='6 Threads', linestyle='dotted', marker='.')
ax.plot(fournode32threads[:, 0], fournode32threads[:, 5], color=colors[1], label='32 Threads', linestyle='dotted', marker='.')
ax.plot(fournode64threads[:, 0], fournode64threads[:, 5], color=colors[2], label='64 Threads',  linestyle='dotted', marker='.')
ax.plot(fournode32threads[:, 0], fournode96threads[:, 5], color=colors[3], label='96 Threads',  linestyle='dotted', marker='.')
ax.plot(fournode128threads[:, 0], fournode128threads[:, 5], color=colors[4], label='128 Threads', linestyle='dotted', marker='.')

#ax.plot(eightnode16threads[:, 0], eightnode16threads[:, 5], color=colors[0], label='6 Threads', linestyle='dashed', marker='.')
ax.plot(eightnode32threads[:, 0], eightnode32threads[:, 5], color=colors[1], label='32 Threads', linestyle='dashed', marker='.')
ax.plot(eightnode64threads[:, 0], eightnode64threads[:, 5], color=colors[2], label='64 Threads', linestyle='dashed',  marker='.')
ax.plot(eightnode32threads[:, 0], eightnode96threads[:, 5], color=colors[3], label='96 Threads', linestyle='dashed',  marker='.')
ax.plot(eightnode128threads[:, 0], eightnode128threads[:, 5], color=colors[4], label='128 Threads', linestyle='dashed',  marker='.')
ax.set_ylabel('Seconds')
ax.set_xlabel('Datasize K')
legend_elements = [Line2D([0], [0], color=colors[0], lw=2, label='16 Threads'),
                   Line2D([0], [0], color=colors[1], lw=2, label='32 Threads'),
                   Line2D([0], [0], color=colors[2], lw=2, label='64 Threads'),
                   Line2D([0], [0], color=colors[3],  lw=2, label='96 Threads'),
                   Line2D([0], [0], color=colors[4],  lw=2, label='128 Threads'),
                   Line2D([0], [0], color='grey', linestyle='solid', lw=2, label='1 Node'),
                   Line2D([0], [0], color='grey', linestyle='dotted', lw=2, label='4 Nodes'),
                   Line2D([0], [0], color='grey', linestyle='dashed', lw=2, label='8 Nodes')]
ax.legend(handles=legend_elements)
plt.show()
