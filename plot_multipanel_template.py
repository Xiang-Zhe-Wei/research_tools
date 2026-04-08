import numpy as np
import matplotlib.pyplot as plt

# ====================================================================
# Multi-panel plot template
# ====================================================================

x = np.linspace(0, 2*np.pi, 300)

# --- data ---
y1_ref = np.sin(x)
y2_ref = np.cos(x)
y3_ref = np.sin(2*x)

y1_A = np.sin(x) + 0.1*np.random.randn(len(x))
y2_A = np.cos(x) + 0.1*np.random.randn(len(x))
y3_A = np.sin(2*x) + 0.1*np.random.randn(len(x))

y1_B = np.sin(x) + 0.2*np.random.randn(len(x))
y2_B = np.cos(x) + 0.2*np.random.randn(len(x))
y3_B = np.sin(2*x) + 0.2*np.random.randn(len(x))

y1_C = np.sin(x) + 0.3*np.random.randn(len(x))
y2_C = np.cos(x) + 0.3*np.random.randn(len(x))
y3_C = np.sin(2*x) + 0.3*np.random.randn(len(x))

# --- plot ---
fig, axes = plt.subplots(3, 1, sharex=True, dpi=140)
fig.subplots_adjust(hspace=0.1)

ylabels       = [r'$\sin(x)$', r'$\cos(x)$', r'$\sin(2x)$']
refs          = [y1_ref, y2_ref, y3_ref]
scheme_data   = [[y1_A, y2_A, y3_A], [y1_B, y2_B, y3_B], [y1_C, y2_C, y3_C]]
scheme_labels = ['Scheme A', 'Scheme B', 'Scheme C']
colors        = ['C0', 'C1', 'C2']

for i, (ax, ylabel, ref) in enumerate(zip(axes, ylabels, refs)):
    ax.plot(x, ref, 'k-', lw=1.2, label='Reference')
    for label, data, color in zip(scheme_labels, scheme_data, colors):
        ax.plot(x, data[i], color, ls='--', lw=0.8, label=label)
    ax.set_ylabel(ylabel)
    ax.legend(fontsize=8, loc='upper right')

axes[-1].set_xlabel(r'$x$')
# plt.savefig('output.png', dpi=140, bbox_inches='tight')
plt.show()