import matplotlib.pyplot as plt
import numpy as np

def step_fun(time, jump:int):
    return np.where(time <= jump, 0, 10)

t0 = np.linspace(-np.pi, np.pi, 201)
t1 = np.arange(0, 2*np.pi, 0.01)

sin = np.sin(t0)



fig, ax = plt.subplots(2,1, figsize=(6,6), dpi=140, layout="constrained")
ax[0].set_title("ax[0] pic")
ax[0].plot(t0, sin)
# ax[0].set_xlim(0, 100)
# ax[0].set_ylim(0, 500)
ax[0].set_xlabel("ax0 X-label")
ax[0].set_ylabel("ax0 Y-label")

ax[1].set_title("ax[1] pic")
ax[1].plot(t1, step_fun(t1, 3))
# ax[1].set_xlim(0, 100)
# ax[1].set_ylim(0, 400)
ax[1].set_xlabel("ax1 X-label")
ax[1].set_ylabel("ax1 Y-label")


plt.suptitle("suptitle")
plt.show()
