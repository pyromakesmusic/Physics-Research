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

def save_to_file():
    return(True)
"""
anim = animation.FuncAnimation(fig, animate, init_func = init,
                    frames = 400, interval = 5, blit = True)

anim.save('continuousSineWave.gif',
          writer = "ffmpeg", fps= 20)
"""


# Window Declarations
window = tk.Tk()
window.title("Interactive Ozone Analysis")
window.resizable(width=True,height=True)
window.columnconfigure([0,1,2,3],minsize=250)
window.rowconfigure([0,1,2,3], minsize=100)

# Buttons
generate_button = tk.Button(text="Generate")
animate_button = tk.Button(text="Animate")

# Checkboxes
var1=tk.IntVar()
save_checkbox = tk.Checkbutton(window, text = "Save to File", variable=var1, onvalue=1, offvalue=0, command=save_to_file)
save_checkbox.grid(row=1, column=3)

# Textboxes
output_path = tk.Entry(window)
string_prefix = tk.Entry(window)

#GUI Manager
animate_button.grid(row=2, column=3, sticky="nsew")
generate_button.grid(row=3, column=3, sticky = "nsew")
output_path.grid(row=0, column=3)
string_prefix.grid(row=1,column=3)

# Main Window Call
window.mainloop()
