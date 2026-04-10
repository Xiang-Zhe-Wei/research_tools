import matplotlib.pyplot as plt
import numpy as np

e0 = 10
x = np.linspace(0, 5, 300)
y = e0*np.exp(-x)

# two points
first, second = 1, 4
x1, y1 = first, e0*np.exp(-first)
x2, y2 = second, e0*np.exp(-second)

# Arithmetic Mean
x_Ari = (x1 + x2) / 2
y_Ari = e0*np.exp(-x_Ari)

# Harmonic Mean
x_harm = 2 / (1/x1 + 1/x2)
y_harm = e0*np.exp(-x_harm)

# Geometric Mean
x_geo = np.sqrt(x1 * x2)
y_geo = e0*np.exp(-x_geo)

# RMS (Quadratic Mean)
x_rms = np.sqrt((x1**2 + x2**2) / 2)
y_rms = e0*np.exp(-x_rms)

# main plot
fig, ax = plt.subplots(1, 1, figsize=(6, 6), dpi=140, layout="constrained")
ax.plot(x, y, label=r"$y = 10e^{-x}$", linewidth=1, color="royalblue")
ax.set_title(r"Exponential Function: $y = 10e^{-x}$")
ax.set_xlabel("x")
ax.set_ylabel("y")
# ax.axhline(0, color='gray', linewidth=0.8, linestyle='--')
# ax.axvline(0, color='gray', linewidth=0.8, linestyle='--')
# # ax.set_xlim(0, 100)
# ax.set_ylim(0, 500)


# plot two points
ax.plot([x1, x2], [y1, y2], color='tomato', linestyle='--', linewidth=1.5)
ax.scatter([x1, x2], [y1, y2], color='tomato', s=60, zorder=5)
ax.annotate(f'({x1}, {y1:.2f})', (x1, y1), textcoords="offset points", xytext=(-10, 10), fontsize=9)
ax.annotate(f'({x2}, {y2:.2f})', (x2, y2), textcoords="offset points", xytext=(8, -15), fontsize=9)



means = [
    (x_harm, y_harm, 'purple',     'Harmonic'),
    (x_geo,  y_geo,  'darkorange', 'Geometric'),
    (x_Ari,  y_Ari,  'green',      'Arithmetic'),
    (x_rms,  y_rms,  'brown',      'RMS'),
]

for xm, ym, color, label in means:
    ax.scatter([xm], [ym], color=color, s=60, zorder=5)
    ax.annotate(f'({xm:.2f}, {ym:.2f}) {label}', (xm, ym), textcoords="offset points",
                xytext=(8, 5), fontsize=9, color=color)

ax.legend(fontsize=13)
ax.grid(True, linestyle=':', alpha=0.6)
plt.show()


