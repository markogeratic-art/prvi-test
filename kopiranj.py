#
# Vsebino tabele b skopira v tabelo a.
#

def kopiraj (a, b):
    a[:] = b


t = [10, 20, 30, 40]
u = [7, 6, 5, 4]

kopiraj(t, u)

print(t)
print(u)