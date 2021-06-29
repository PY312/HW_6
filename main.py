from university.library import Library
from university.students import Students
import cowsay
import requests
import django


a = Students("Саша")
b = Students("Петя")
print(Library.books_list())

a.get_book(Library, "Жамиля")
print(Library.books_list())

b.get_book(Library, "Белый пароход")
print(Library.books_list())

a.retern_book(Library, "Жамиля")
print(Library.books_list())

b.get_book(Library, "Жамиля")
print(Library.books_list())


cowsay.tux("Well Done")


