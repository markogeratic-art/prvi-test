a = "Pozdravljen"
b = input("vpiši ime")

print(a + " " + b + "!")

def vprasaj():
    ime = input("Vpiši svoje ime: ")
    return f"Pozdravljen, {ime}!"

if __name__ == '__main__':
    print(vprasaj())

