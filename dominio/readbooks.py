for id in favs:
    ids.append(id[0])
librosfavs = BooksRepository.get_books_by_ids(ids)  # Tenemos los libros favoritos del usuario
counter = 0
varpos = 0
varps = 0
for librofav in librosfavs:
    if counter < 4:
        self.librofav = tk.Label(self.seccion_favoritos, text=f"{librofav[0]}", font=('Trebuchet MS', 14))
        self.librofav.pack(pady=1)
    elif 4 <= counter < 8:
        self.librofav = tk.Label(self.seccion_favoritos, text=f"{librofav[0]}", font=('Trebuchet MS', 14))
        self.librofav.place(x=10, y=33 + varpos)
        varpos += 40
    elif counter >= 8:
        self.librofav = tk.Label(self.seccion_favoritos, text=f"{librofav[0]}", font=('Trebuchet MS', 14))
        self.librofav.place(x=800, y=33 + varps)
        varps += 40

    counter += 1