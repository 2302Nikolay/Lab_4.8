#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *


def move_towards_target():
    current_coords = c.coords(ball)
    target_x, target_y = target_coords

    # Рассчитываем расстояние между текущим положением и целевой точкой
    distance_x = target_x - current_coords[0]
    distance_y = target_y - current_coords[1]

    # Определяем шаг перемещения
    step_x = 1 if distance_x > 0 else -1
    step_y = 1 if distance_y > 0 else -1

    # Перемещаем круг
    c.move(ball, step_x, step_y)

    # Если не достигли целевой точки, продолжаем анимацию
    if c.coords(ball)[0] != target_x or c.coords(ball)[1] != target_y:
        root.after(10, move_towards_target)


def on_click(event):
    global target_coords
    target_coords = (event.x, event.y)
    move_towards_target()


root = Tk()
c = Canvas(root, width=300, height=200, bg="white")
c.pack()

ball = c.create_oval(0, 100, 40, 140, fill="green")

# Привязываем событие клика к функции
c.bind("<Button-1>", on_click)

root.mainloop()
