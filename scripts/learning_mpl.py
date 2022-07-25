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


"""
MatPlotLib stuff
"""

fig = plt.figure()

axis = plt.axes(xlim=(0,140),
                ylim=(0,300))

x = np.linspace(0,59,20)

bars = plt.bar(x, x)
bars[2].set_color('orange')

line, = axis.plot([],[], lw=3)


plt.axvline(x=71, color="red", linestyle="dashed")

plt.title("Houston Area Ozone Levels")
plt.xlabel("Maximum Daily 8 Hour Ozone (ppb)")
plt.ylabel("Number of Days in Sample")

def bin_maker(xy, height):
    rect = matplotlib.patches.Rectangle(xy, 3, height, angle=0.0)
    return(True)

a = bin_maker((0,0), 0)
b = bin_maker((1,0), 1)
c = bin_maker((2,0), 2)
d = bin_maker((3,0), 3)
e = bin_maker((4,0), 2)

barcontainer = matplotlib.container.BarContainer((a,b,c,d,e))

plt.show()

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

This stuff is for saving animations of generated files.

anim = animation.FuncAnimation(fig, animate, init_func = init,
                    frames = 400, interval = 5, blit = True)

anim.save('continuousSineWave.gif',
          writer = "ffmpeg", fps= 20)
"""

"""
All of this is GUI stuff and it all works. Commenting out for now so I can work on the histogram.
# Window Declarations
window = tk.Tk()
window.title("Interactive Ozone Analysis")
window.resizable(width=True,height=True)
window.columnconfigure([0,1,2,3],minsize=250)
window.rowconfigure([0,1,2,3], minsize=100)

# Labels
path_label = tk.Label(window, text = "Output Path")
stringprefix_label = tk.Label(window, text="String Prefix")

# Buttons
generate_button = tk.Button(text="Generate")
animate_button = tk.Button(text="Animate")

# Checkboxes
var1=tk.IntVar()
save_checkbox = tk.Checkbutton(window, text = "Save to File", variable=var1, onvalue=1, offvalue=0, command=save_to_file)
year_checkbox = "year_placeholder"
month_checkbox = "month_placeholder"


# Textboxes
output_path = tk.Entry(window)
string_prefix = tk.Entry(window)

#GUI Manager
animate_button.grid(row=2, column=3, sticky="nsew")
generate_button.grid(row=3, column=3, sticky = "nsew")
save_checkbox.grid(row=3, column=2, sticky="se")
output_path.grid(row=0, column=3, sticky = "ew")
string_prefix.grid(row=1,column=3, sticky = "ew")
path_label.grid(row=0, column=2, sticky = "e")
stringprefix_label.grid(row=1, column=2, sticky="e")

# Main Window Call
window.mainloop()
"""