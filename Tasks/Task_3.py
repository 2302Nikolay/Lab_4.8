#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tkinter as tk


class ResizableTextApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Размеризуемый текст")

        # Переменные для хранения размеров текстового поля
        self.width_var = tk.StringVar()
        self.height_var = tk.StringVar()

        # Многострочное текстовое поле
        self.text_widget = tk.Text(root, wrap=tk.WORD, bg="lightgrey")
        self.text_widget.pack(expand=True, fill=tk.BOTH)

        # Полосы прокрутки для текстового поля
        scroll_y = tk.Scrollbar(root, command=self.text_widget.yview)
        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
        self.text_widget.config(yscrollcommand=scroll_y.set)

        # Создаем однострочные текстовые поля для ввода размеров
        self.width_entry = tk.Entry(root, textvariable=self.width_var)
        self.width_entry.pack(side=tk.LEFT, padx=10)
        self.width_entry.bind("<Return>", self.resize_text)

        self.height_entry = tk.Entry(root, textvariable=self.height_var)
        self.height_entry.pack(side=tk.LEFT, padx=10)
        self.height_entry.bind("<Return>", self.resize_text)

        # Кнопка для изменения размера текстового поля
        self.resize_button = tk.Button(
            root, text="Изменить размер", command=self.resize_text
        )
        self.resize_button.pack(side=tk.LEFT, padx=10)

        # Привязываем события фокуса для изменения цвета фона
        self.text_widget.bind("<FocusIn>", self.on_focus_in)
        self.text_widget.bind("<FocusOut>", self.on_focus_out)

    def resize_text(self, event=None):
        try:
            width = int(self.width_var.get())
            height = int(self.height_var.get())
            self.text_widget.config(width=width, height=height)
        except ValueError:
            pass

    def on_focus_in(self, event):
        self.text_widget.config(bg="white")

    def on_focus_out(self, event):
        self.text_widget.config(bg="lightgrey")


if __name__ == "__main__":
    root = tk.Tk()
    app = ResizableTextApp(root)
    root.mainloop()
