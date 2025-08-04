# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 22:41:42 2020

@author: Lenovo
"""

import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()

background = Image.open('Asean.jpg')
foreground = Image.open('mask.jpg')
tk_image = ImageTk.PhotoImage(background)

#background.show()

#back_im = image.copy()
#back_im.paste(image2, (5, 5))
#back_im.save('scubaB.png', quality=95)

#image3 = Image.open('scubaB.png')
#bk_image = ImageTk.PhotoImage(image3)


label1 = tk.Label(root, text='Some Plain Text', image=tk_image, compound='center')


label2 = tk.Label(root, text='Another Plain Text', image=tk_image, compound='left')
label1.pack()

root.mainloop()