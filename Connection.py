from tkinter import W
from DBHelperClass import *

print(all.allcategories())

b = ["'Fantasy'", "'Romance'", "'stark'"]
search.tags(b)

c = ["'Serifen'"]
stringify = ' OR '.join(c)
print(stringify)
search.category(c)