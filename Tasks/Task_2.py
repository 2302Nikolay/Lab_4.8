#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tkinter as tk


class TextListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Текст и список")

        # Создаем однострочное текстовое поле
        self.text_entry = tk.Entry(root)
        self.text_entry.pack(pady=10)
        self.text_entry.bind("<Return>", self.add_to_list)

        # Создаем список
        self.text_listbox = tk.Listbox(root)
        self.text_listbox.pack(expand=True, fill=tk.BOTH)
        self.text_listbox.bind("<Double-Button-1>", self.copy_to_text_entry)

    def add_to_list(self, event):
        text = self.text_entry.get()
        if text:
            self.text_listbox.insert(tk.END, text)
            self.text_entry.delete(0, tk.END)

    def copy_to_text_entry(self, event):
        selected_index = self.text_listbox.curselection()
        if selected_index:
            selected_text = self.text_listbox.get(selected_index)
            self.text_entry.delete(0, tk.END)
            self.text_entry.insert(0, selected_text)


if __name__ == "__main__":
    root = tk.Tk()
    app = TextListApp(root)
    root.mainloop()
