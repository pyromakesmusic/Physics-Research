# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 13:24:05 2022

@author: Ghost
Learning to graph in matplotlib
"""
import tkinter as tk
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()

axis = plt.axes(xlim=(0,140),
                ylim=(0,300))

line, = axis.plot([],[], lw=3)


def bin_maker(xy, height):
    rect = matplotlib.patches.Rectangle(xy, 3, height, angle=0.0)
    return(True)

a = bin_maker((0,0), 0)
b = bin_maker((1,0), 1)
c = bin_maker((2,0), 2)
d = bin_maker((3,0), 3)
e = bin_maker((4,0), 2)

barcontainer = matplotlib.container.BarContainer((a,b,c,d,e))

def init():
    line.set_data([],[])
    return line,

def animate(i):
    x=np.linspace(0,100,1000)
    
    y= 100 * np.sin(2 * np.pi * (x - 0.01 * i))
    line.set_data(x,y)

    return line,

"""
anim = animation.FuncAnimation(fig, animate, init_func = init,
                    frames = 400, interval = 5, blit = True)

anim.save('continuousSineWave.gif',
          writer = "ffmpeg", fps= 20)
"""



window = tk.Tk()
window.resizable(width=True,height=True)
window.columnconfigure([0,1,2,3],minsize=250)
window.rowconfigure([0,1,2,3], minsize=100)
greeting = tk.Label(text="Interactive Ozone Analysis")
execute_button = tk.Button(text="Execute")
animate_button = tk.Button(text="Animate")
var1=tk.IntVar()
save_checkbox = tk.Checkbutton(window, text = "Save to File", variable=var1, onvalue=1, offvalue=0, command=print_selection)
animate_button.grid(row=2, column=3, sticky="nsew")
execute_button.grid(row=3, column=3, sticky = "nsew")


greeting.grid(row=0, column=0, sticky="nw")

window.mainloop()
