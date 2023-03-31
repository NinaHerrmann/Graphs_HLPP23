import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
import matplotlib.transforms as mtransforms

bottom, top = 0.1, 0.9
plt.style.use('_mpl-gallery')

data2080 = np.genfromtxt ('data/20801Nodeallsizes.csv', delimiter=";")
twonodes2080 = np.genfromtxt ('data/20802nodesmuesli.csv', delimiter=";")
fournodes2080 = np.genfromtxt ('data/20804nodesmuesli.csv', delimiter=";")
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

twonodes2080oneGPU = twonodes2080[np.where(twonodes2080[:, 4] == 1)]
twonodes2080twoGPUs = twonodes2080[np.where(twonodes2080[:, 4] == 2)]
twonodes2080fourGPUs = twonodes2080[np.where(twonodes2080[:, 4] == 4)]
twonodes2080eightGPUs = twonodes2080[np.where(twonodes2080[:, 4] == 8)]

fournodes2080oneGPU = fournodes2080[np.where(fournodes2080[:, 4] == 1)]
fournodes2080twoGPUs = fournodes2080[np.where(fournodes2080[:, 4] == 2)]
fournodes2080fourGPUs = fournodes2080[np.where(fournodes2080[:, 4] == 4)]
fournodes2080eightGPUs = fournodes2080[np.where(fournodes2080[:, 4] == 8)]

ax[0].plot(oneNodeoneGPU[:, 0], oneNodeoneGPU[:, 6],  label='1 GPUs', color='b', marker='.')
ax[0].plot(oneNodetwoGPUs[:, 0], oneNodetwoGPUs[:, 6], label='2 GPUs', color='b', marker='.', linestyle='dotted')
ax[0].plot(oneNodefourGPUs[:, 0], oneNodefourGPUs[:, 6], label='2 GPUs', color='b', marker='.', linestyle='dashed')

ax[0].plot(twonodes2080oneGPU[:, 0], twonodes2080oneGPU[:, 5],  label='1 GPU', color='r', marker='.')
ax[0].plot(twonodes2080twoGPUs[:, 0], twonodes2080twoGPUs[:, 5], label='2 GPUs', color='r', linestyle='dotted', marker='.')
ax[0].plot(twonodes2080fourGPUs[:, 0], twonodes2080fourGPUs[:, 5], label='4 GPUs', color='r', linestyle='dashed', marker='.')

ax[0].plot(fournodes2080oneGPU[:, 0], fournodes2080oneGPU[:, 5],  label='1 GPU', color='g', marker='.')
ax[0].plot(fournodes2080twoGPUs[:, 0], fournodes2080twoGPUs[:, 5], label='2 GPUs', color='g', linestyle='dotted', marker='.')
ax[0].plot(fournodes2080fourGPUs[:, 0], fournodes2080fourGPUs[:, 5], label='4 GPUs', color='g', linestyle='dashed', marker='.')

print(np.divide(oneNodeoneGPU[:, 1], 1000))
ax[1].plot(np.divide(oneNodeoneGPU[:, 1], 1000), oneNodeoneGPU[:, 6],  label='1 GPUs', color='b', marker='.')
ax[1].plot(np.divide(oneNodetwoGPUs[:, 1], 1000), oneNodetwoGPUs[:, 6], label='2 GPUs', color='b', marker='.', linestyle='dotted')
ax[1].plot(np.divide(oneNodefourGPUs[:, 1], 1000), oneNodefourGPUs[:, 6], label='2 GPUs', color='b', marker='.', linestyle='dashed')

ax[1].plot(twonodes2080oneGPU[:, 1], twonodes2080oneGPU[:, 5],  label='1 GPU', color='r', marker='.')
ax[1].plot(twonodes2080twoGPUs[:, 1], twonodes2080twoGPUs[:, 5], label='2 GPUs', color='r', linestyle='dotted', marker='.')
ax[1].plot(twonodes2080fourGPUs[:, 1], twonodes2080fourGPUs[:, 5], label='4 GPUs', color='r', linestyle='dashed', marker='.')

ax[1].plot(fournodes2080oneGPU[:, 1], fournodes2080oneGPU[:, 5],  label='1 GPU', color='g', marker='.')
ax[1].plot(fournodes2080twoGPUs[:, 1], fournodes2080twoGPUs[:, 5], label='2 GPUs', color='g', linestyle='dotted', marker='.')
ax[1].plot(fournodes2080fourGPUs[:, 1], fournodes2080fourGPUs[:, 5], label='4 GPUs', color='g', linestyle='dashed', marker='.')

legend_elements = [Line2D([0], [0], color='b', lw=2, label='1 Node'),
                   Line2D([0], [0], color='r', lw=2, label='2 Nodes'),
                   Line2D([0], [0], color='g', lw=2, label='4 Nodes'),
                   Line2D([0], [0], color='grey',  lw=2, label='1 GPU'),
                   Line2D([0], [0], color='grey', linestyle='dotted', lw=2, label='2 GPUs'),
                   Line2D([0], [0], color='grey', linestyle='dashed', lw=2, label='4 GPUs')]
ax[0].legend(handles=legend_elements)
plt.show()
