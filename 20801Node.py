import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
import matplotlib.transforms as mtransforms

bottom, top = 0.1, 0.9
plt.style.use('_mpl-gallery')

data2080 = np.genfromtxt ('data/20801Nodeallsizes.csv', delimiter=";")
nativedata2080 = np.genfromtxt ('data/2080native1Nodeallsizes.csv', delimiter=";")
# make data
x = np.linspace(0, 10, 100)
y = 4 + 2 * np.sin(2 * x)

# plot
fig, ax = plt.subplots(nrows=1, ncols=2)

avepos = 0.5 * (bottom + top)
transform = mtransforms.blended_transform_factory(mtransforms.IdentityTransform(), fig.transFigure)  # specify x, y transform
ax[0].yaxis.label.set_transform(transform)  # changed from default blend (IdentityTransform(), axs[0].transAxes)
ax[0].yaxis.label.set_position((0, avepos))
ax[0].set_ylabel('Seconds')
ax[0].set_xlabel('Datasize ^3')
ax[1].set_xlabel('Datasize')

oneNodeoneGPU = data2080[np.where(data2080[:, 5] == 1)]
oneNodetwoGPUs = data2080[np.where(data2080[:, 5] == 2)]
oneNodefourGPUs = data2080[np.where(data2080[:, 5] == 4)]
oneNodeeightGPUs = data2080[np.where(data2080[:, 5] == 8)]

naoneNodeoneGPU = nativedata2080[np.where(nativedata2080[:, 3] == 1)]
naoneNodetwoGPUs = nativedata2080[np.where(nativedata2080[:, 3] == 2)]
naoneNodefourGPUs = nativedata2080[np.where(nativedata2080[:, 3] == 4)]
naoneNodeeightGPUs = nativedata2080[np.where(nativedata2080[:, 3] == 8)]


ax[0].plot(oneNodeoneGPU[:, 0], oneNodeoneGPU[:, 6],  label='1 GPUs', color='b', marker='.')
ax[0].plot(oneNodetwoGPUs[:, 0], oneNodetwoGPUs[:, 6], label='2 GPUs', color='r', marker='.')
ax[0].plot(oneNodefourGPUs[:, 0], oneNodefourGPUs[:, 6],  label='4 GPUs', color='g', marker='.')
# ax[0].plot(oneNodeeightGPUs[:, 0], oneNodeeightGPUs[:, 6],  label='8 GPUs', color='y', marker='.')

ax[0].plot(naoneNodeoneGPU[:, 0], naoneNodeoneGPU[:, 4],  label='1 GPU', color='b', linestyle='dashed', marker='.')
ax[0].plot(naoneNodetwoGPUs[:, 0], naoneNodetwoGPUs[:, 4], label='2 GPUs', color='r', linestyle='dashed', marker='.')
ax[0].plot(naoneNodefourGPUs[:, 0], naoneNodefourGPUs[:, 4],  label='4 GPUs', color='g', linestyle='dashed', marker='.')
#  ax[0].plot(naoneNodeeightGPUs[:, 0], naoneNodeeightGPUs[:, 4],  label='8 GPUs', color='y', linestyle='dashed', marker='.')
testoneNodeoneGPU = np.divide(oneNodeoneGPU[:,1], 1000)
print(testoneNodeoneGPU)
ax[1].plot( np.divide(oneNodeoneGPU[:, 1], 1000), oneNodeoneGPU[:, 6],  label='1 GPUs', color='b', marker='.')
ax[1].plot(np.divide(oneNodetwoGPUs[:, 1], 1000), oneNodetwoGPUs[:, 6], label='2 GPUs', color='r', marker='.')
ax[1].plot(np.divide(oneNodefourGPUs[:, 1], 1000), oneNodefourGPUs[:, 6],  label='4 GPUs', color='g', marker='.')
# ax[1].plot(np.divide(oneNodeeightGPUs[:, 1], 1000), oneNodeeightGPUs[:, 6],  label='8 GPUs', color='y', marker='.')

ax[1].plot(np.divide(naoneNodeoneGPU[:, 1], 1000), naoneNodeoneGPU[:, 4],  label='1 GPU', color='b', linestyle='dashed', marker='.')
ax[1].plot(np.divide(naoneNodetwoGPUs[:, 1], 1000), naoneNodetwoGPUs[:, 4], label='2 GPUs', color='r', linestyle='dashed', marker='.')
ax[1].plot(np.divide(naoneNodefourGPUs[:, 1], 1000), naoneNodefourGPUs[:, 4],  label='4 GPUs', color='g', linestyle='dashed', marker='.')
# ax[1].plot(np.divide(naoneNodeeightGPUs[:, 1], 1000), naoneNodeeightGPUs[:, 4],  label='8 GPUs', color='y', linestyle='dashed', marker='.')

legend_elements = [Line2D([0], [0], color='grey', lw=2, label='Muesli'),
                   Line2D([0], [0], color='grey', lw=2, label='Native', linestyle='dashed'),
                   Line2D([0], [0], color='b', lw=2, label='1 GPU'),
                   Line2D([0], [0], color='r', lw=2, label='2 GPU'),
                   Line2D([0], [0], color='g', lw=2, label='4 GPU'),
                   Line2D([0], [0], color='y', lw=2, label='8 GPU')]
ax[0].legend(handles=legend_elements)
plt.show()
