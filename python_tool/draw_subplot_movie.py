import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


t0 = np.linspace(-np.pi, np.pi, 201)
t1 = np.arange(0, 2*np.pi, 0.01)


def step_fun(time, jump:int):
    return np.where(time <= jump, 0, 10)
# sin = np.sin(t0)


# 1st data
fig, ax = plt.subplots(2,1, figsize=(6,6), dpi=140, layout="constrained")
ax[0].set_title("ax[0] pic")
line0, = ax[0].plot([], [])
ax[0].set_ylim(-1.2, 1.2)
ax[0].set_xlim(-np.pi, np.pi)
# ax[0].set_xlim(0, 100)
# ax[0].set_ylim(0, 500)
ax[0].set_xlabel("ax0 X-label")
ax[0].set_ylabel("ax0 Y-label")


# 2rd data
ax[1].set_title("ax[1] pic")
ax[1].plot(t1, step_fun(t1, 3))
# ax[1].set_xlim(0, 100)
# ax[1].set_ylim(0, 400)
ax[1].set_xlabel("ax1 X-label")
ax[1].set_ylabel("ax1 Y-label")


def init():
    line0.set_xdata( t0 )
    return line0,


def animate(i):
    line0.set_ydata(np.sin(t0 + i / 50))  # update the data.
    return line0,

ani = animation.FuncAnimation( fig, animate, frames=100, interval=20, init_func=init )

plt.suptitle("suptitle")
plt.show()
