# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 13:24:05 2022

@author: Ghost
Learning to graph in matplotlib
"""
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Fixing random state for reproducibility
np.random.seed(19680801)
# Fixing bin edges
HIST_BINS = np.linspace(-4,4,100)

# histogram our data with numpy
data = np.random.randn(1000)
n, _ = np.histogram(data, HIST_BINS)

def prepare_animation(bar_container):
    def animate(frame_number):
        # simulate new data coming in
        data = np.random.randn(1000)
        n, _ = np.histogram(data, HIST_BINS)
        for count, rect in zip(n, bar_container.patches):
            rect.set_height(count)
        return(bar_container.patches)
    return animate

fig, ax = plt.subplots()
_, _, bar_container = ax.hist(data, HIST_BINS, lw=1,
                              ec="yellow", fc="green", alpha=0.5)
ax.set_ylim(top=55) # set safe limit to ensure that all data is visible.

ani = animation.FuncAnimation(fig, prepare_animation(bar_container), 50,
                              repeat=True, blit=True)

plt.show()
window = tk.Tk()
window.resizable(width=True,height=True)
window.columnconfigure([0,1,2,3],minsize=250)
window.rowconfigure([0,1,2,3], minsize=100)
greeting = tk.Label(text="Interactive Ozone Analysis")
execute_button = tk.Button(text="Execute")
animate_button = tk.Button(text="Animate")
animate_button.grid(row=2, column=3, sticky="nsew")
execute_button.grid(row=3, column=3, sticky = "nsew")


greeting.grid(row=0, column=0, sticky="nw")

window.mainloop()