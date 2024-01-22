#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tkinter as tk


class ShoppingListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Список покупок")

        # Создаем два списковых виджета
        self.available_items_listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)
        self.available_items_listbox.pack(side=tk.LEFT, padx=10)

        self.shopping_listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)
        self.shopping_listbox.pack(side=tk.RIGHT, padx=10)

        # Наполняем первый список товарами
        available_items = ["Хлеб", "Молоко", "Яйца", "Фрукты", "Овощи", "Мясо"]
        for item in available_items:
            self.available_items_listbox.insert(tk.END, item)

        # Создаем кнопки для перемещения товаров
        self.add_button = tk.Button(
            root, text="Добавить в список", command=self.add_to_shopping_list
        )
        self.add_button.pack(pady=10)

        self.remove_button = tk.Button(
            root, text="Убрать из списка", command=self.remove_from_shopping_list
        )
        self.remove_button.pack(pady=10)

    def add_to_shopping_list(self):
        selected_items = self.available_items_listbox.curselection()
        for index in selected_items[
            ::-1
        ]:  # Перебираем в обратном порядке, чтобы удаление не нарушало индексы
            item = self.available_items_listbox.get(index)
            self.shopping_listbox.insert(tk.END, item)
            self.available_items_listbox.delete(index)

    def remove_from_shopping_list(self):
        selected_items = self.shopping_listbox.curselection()
        for index in selected_items[::-1]:
            item = self.shopping_listbox.get(index)
            self.available_items_listbox.insert(tk.END, item)
            self.shopping_listbox.delete(index)


if __name__ == "__main__":
    root = tk.Tk()
    app = ShoppingListApp(root)
    root.mainloop()
