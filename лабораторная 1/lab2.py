diskette_size_mb = 1.44  # Информационный объем дискеты в Мб
book_pages = 100
lines_per_page = 50
characters_per_line = 25
bytes_per_character = 4

characters_per_page = lines_per_page * characters_per_line
book_size_bytes = book_pages * characters_per_page * bytes_per_character
diskette_size_bytes = diskette_size_mb * 1024 * 1024
books_on_diskette = int(diskette_size_bytes // book_size_bytes)

print("Количество книг, помещающихся на дискету:", books_on_diskette)
