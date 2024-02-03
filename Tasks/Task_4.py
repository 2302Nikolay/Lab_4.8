#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tkinter as tk


class LandscapeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Пейзаж")

        self.canvas = tk.Canvas(root, width=400, height=300, bg="skyblue")
        self.canvas.pack()

        # Рисуем траву
        self.draw_grass()

        # Рисуем силуэт домика
        self.draw_house()

        # Рисуем солнце
        self.draw_sun()

    def draw_grass(self):
        grass_color = "green"

        # Рисуем траву в виде зеленых пучков
        for x in range(0, 400, 40):
            self.canvas.create_polygon(
                x, 200, x + 20, 180, x + 40, 200, fill=grass_color, outline=grass_color
            )

    def draw_house(self):
        house_color = "lightyellow"
        roof_color = "brown"

        # Рисуем стены домика
        self.canvas.create_rectangle(100, 100, 300, 200, fill=house_color)

        # Рисуем крышу домика
        self.canvas.create_polygon(100, 100, 200, 50, 300, 100, fill=roof_color)

    def draw_sun(self):
        sun_color = "yellow"
        sun_radius = 30
        sun_center = (370, 30)

        # Рисуем круг (солнце)
        self.canvas.create_oval(
            sun_center[0] - sun_radius,
            sun_center[1] - sun_radius,
            sun_center[0] + sun_radius,
            sun_center[1] + sun_radius,
            fill=sun_color,
        )


if __name__ == "__main__":
    root = tk.Tk()
    app = LandscapeApp(root)
    root.mainloop()
