import tkinter as tk
from tkinter import messagebox

class BookManagerApp:
    def __init__(self):
        self.master = tk.Tk()
        self.master.title('Gestor de libros personal')

        self.books = []

        # Etiqueta y entrada para el título del libro
        tk.Label(self.master, text='Título del libro:').grid(row=0, column=0)
        self.title_entry = tk.Entry(self.master)
        self.title_entry.grid(row=0, column=1)

        # Etiqueta y entrada para la nota del libro
        tk.Label(self.master, text='Nota del libro:').grid(row=1, column=0)
        self.rating_entry = tk.Entry(self.master)
        self.rating_entry.grid(row=1, column=1)

        # Botón para agregar un libro
        self.add_button = tk.Button(self.master, text='Agregar libro', command=self.add_book)
        self.add_button.grid(row=2, column=0, columnspan=2, pady=10)

        # Lista de libros
        self.book_listbox = tk.Listbox(self.master, width=50)
        self.book_listbox.grid(row=3, column=0, columnspan=2, pady=10)

    def add_book(self):
        title = self.title_entry.get()
        rating = self.rating_entry.get()
        if title and rating:
            self.books.append((title, rating))
            self.update_book_list()
            self.title_entry.delete(0, tk.END)
            self.rating_entry.delete(0, tk.END)
        else:
            messagebox.showwarning('Advertencia', 'Por favor, ingresa el título y la nota del libro')

    def update_book_list(self):
        self.book_listbox.delete(0, tk.END)
        for book in self.books:
            self.book_listbox.insert(tk.END, f'Título: {book[0]}, Nota: {book[1]}')

    def run(self): # Método ejecutar bucle principal interfaz
        self.master.mainloop()

def main():
    app = BookManagerApp()
    app.run()

if __name__ == '__main__':
    main()