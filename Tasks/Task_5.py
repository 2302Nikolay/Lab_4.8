#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *

def move_towards_target():
    current_coords = c.coords(star)
    target_x, target_y = target_coords

    # Рассчитываем расстояние между текущим положением и целевой точкой
    distance_x = target_x - current_coords[0]
    distance_y = target_y - current_coords[1]

    # Определяем угловой коэффициент наклона прямой
    slope = distance_y / distance_x if distance_x != 0 else 0

    # Определяем шаг перемещения по x и y
    step_x = 1 if distance_x > 0 else -1
    step_y = int(slope * step_x)

    # Перемещаем звезду
    c.move(star, step_x, step_y)

    # Если не достигли целевой точки, продолжаем анимацию
    if c.coords(star)[0] != target_x or c.coords(star)[1] != target_y:
        root.after(10, move_towards_target)

def on_click(event):
    global target_coords
    target_coords = (event.x, event.y)
    move_towards_target()

root = Tk()
c = Canvas(root, width=300, height=200, bg="white")
c.pack()

# Создаем звезду (пятиконечную)
star = c.create_polygon(
    50, 50, 70, 10, 90, 50, 60, 30, 80, 30,
    fill="gold", outline="black"
)

# Привязываем событие клика к функции
c.bind("<Button-1>", on_click)

root.mainloop()
