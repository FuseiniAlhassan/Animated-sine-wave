import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from IPython.display import HTML

# Data
n = 200
x = np.linspace(0, 6*np.pi, n)
y = np.sin(x)

# Figure
fig, ax = plt.subplots()
ax.set_xlim(0, 6*np.pi)
ax.set_ylim(-1.2, 1.2)

# Plot sine wave
ax.plot(x, y, 'b')
red_circle, = ax.plot([], [], 'ro', markersize=8)

def init():
    red_circle.set_data([], [])
    return red_circle,

def update(frame):
    red_circle.set_data([x[frame]], [y[frame]])
    return red_circle,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=n, init_func=init,
                              interval=20, blit=True)

# Show animation inside Jupyter (with controls)
HTML(ani.to_jshtml())

# Save animation as GIF (for README demo)
ani.save("sine_wave.gif", writer="pillow", fps=30)
print("Animation saved as sine_wave.gif")