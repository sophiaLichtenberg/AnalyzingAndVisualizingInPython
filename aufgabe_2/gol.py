#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Tkinter as Tk
import tkMessageBox
from PIL import Image, ImageTk, ImageDraw
import numpy as np
import golalgo as golalgo


class NimGui(object):
    def __init__(self, root):
        self.root = root
        self.root.title("Ameisensimulator (Conway's Game of Life)")
        self.image_size = 100, 50
        self.root.minsize(width=500, height=300)
        self.animation_started = False
        self.animation_speed = 100
        self.rules = Tk.IntVar()
        self.rules.set(0)
        self.menubar()
        self.life_image = Image.new("RGB", (self.image_size[0], self.image_size[1]), "white")
        self.resized_image = None
        self.draw = ImageDraw.Draw(self.life_image)
        self.life_photoimage = ImageTk.PhotoImage(self.life_image)
        self.life_image_label = Tk.Label(root, image=self.life_photoimage, borderwidth=0, cursor="cross")
        self.life_image_label.bind("<B1-Motion>", self.mouse_move)
        self.life_image_label.bind("<ButtonPress-1>", self.mouse_down)
        self.life_image_label.bind("<ButtonRelease-1>", self.mouse_up)
        self.life_image_label.bind("<Configure>", lambda (e): self.show_image())
        self.life_image_label.pack(side="top", fill="both", expand=True)
        self.mouse_x, self.mouse_y = 0, 0
        self.pen_color = (0, 0, 0)

    @property
    def screen_size(self):
        return self.life_image_label.winfo_width(), self.life_image_label.winfo_height()

    def mouse_position(self, event):
        current_screen_size = self.screen_size
        return (event.x * self.image_size[0] / current_screen_size[0],
                event.y * self.image_size[1] / current_screen_size[1])

    def mouse_down(self, event):
        self.mouse_x, self.mouse_y = self.mouse_position(event)
        if self.life_image.getpixel((self.mouse_x, self.mouse_y)) != (0, 0, 0):
            self.pen_color = (0, 0, 0)
        else:
            self.pen_color = (255, 255, 255)
        self.draw.line((self.mouse_x, self.mouse_y, self.mouse_x, self.mouse_y), fill=self.pen_color)
        self.show_image()

    def mouse_up(self, event):
        self.mouse_x, self.mouse_y = -1, -1

    def mouse_move(self, event):
        current_mouse_position = self.mouse_position(event)
        if current_mouse_position != (self.mouse_x, self.mouse_y):
            self.draw.line((self.mouse_x, self.mouse_y, current_mouse_position[0], current_mouse_position[1]),
                           fill=self.pen_color)
            self.mouse_x, self.mouse_y = current_mouse_position
            self.show_image()

    def show_image(self):
        self.resized_image = self.life_image.resize(self.screen_size, Image.NEAREST)
        self.life_photoimage = ImageTk.PhotoImage(self.resized_image)
        self.life_image_label.config(image=self.life_photoimage)

    def start(self):
        if not self.animation_started:
            self.root.after(self.animation_speed, self.animate)
        self.animation_started = True

    def stop(self):
        self.animation_started = False

    def step(self):
        self.animation_started = False
        self.update_image()

    def update_image(self):
        ants_as_list = np.array(self.life_image).tolist()
        if self.rules.get() == 1:
            mutated_ants = golalgo.multicolor_ants(ants_as_list)
        else:
            mutated_ants = golalgo.simple_gol(ants_as_list)
        numpy_image = np.array(mutated_ants).astype('uint8')
        self.life_image = Image.fromarray(numpy_image)
        self.draw = ImageDraw.Draw(self.life_image)
        self.show_image()

    def animate(self):
        if self.animation_started:
            self.update_image()
            self.root.after(self.animation_speed, self.animate)

    def set_image_size(self, size):
        self.image_size = size
        self.life_image = Image.new("RGB", (self.image_size[0], self.image_size[1]), "white")
        self.draw = ImageDraw.Draw(self.life_image)
        self.show_image()

    def menubar(self):
        menu_main = Tk.Menu(self.root)
        menu_neu = Tk.Menu(menu_main, tearoff=0)
        menu_start = Tk.Menu(menu_main, tearoff=0)
        menu_options = Tk.Menu(menu_main, tearoff=0)
        menu_options.add_radiobutton(label="Klassische Regeln (Aufgabenteil a)", value=0, variable=self.rules)
        menu_options.add_radiobutton(label="Bunte Ameisen (Aufgabenteil b)", value=1, variable=self.rules)
        menu_neu.add_command(label="100x50", underline=0, command=lambda: self.set_image_size((100, 50)))
        menu_neu.add_command(label="150x100", underline=1, command=lambda: self.set_image_size((150, 100)))
        menu_neu.add_command(label="200x150", underline=1, command=lambda: self.set_image_size((200, 150)))
        menu_help = Tk.Menu(menu_main, tearoff=0)
        help_text = ("Conway's Game of Life\n"
                     "Analysieren und Visualisieren mit Python WS1819\n"
                     "Informationswissenschaft\n"
                     "Uni Regensburg")
        menu_help.add_command(label="Über", underline=0, command=lambda: tkMessageBox.showinfo("GOL", help_text))
        menu_main.add_cascade(label="Neu", underline=0, menu=menu_neu)
        menu_main.add_cascade(label="Start", underline=0, menu=menu_start)
        menu_start.add_command(label="Start", underline=0, command=self.start)
        menu_start.add_command(label="Stop", underline=1, command=self.stop)
        menu_start.add_command(label="1 Schritt", underline=1, command=self.step)
        menu_main.add_cascade(label="Optionen", underline=0, menu=menu_options)
        menu_main.add_cascade(label="Hilfe", underline=0, menu=menu_help)
        self.root.config(menu=menu_main)


r = Tk.Tk()
mainWindow = NimGui(r)
r.mainloop()
