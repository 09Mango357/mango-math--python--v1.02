print("mango math menu v1.02 (python edition)")
print("options = 1.addition 2.subtraction 3.multiplication 4.division")
type = int(input("selected option: "))
if type == 1:
    print("--addition--")
    a = int(input("intiger one: "))
    b = int(input("intiger two: "))
    print(a + b)
if type == 2:
    print("--subtraction--")
    a = int(input("intiger one: "))
    b = int(input("intiger two: "))
    print(a - b)
if type == 3:
    print("--multiplication--")
    a = int(input("intiger one: "))
    b = int(input("intiger two: "))
    print(a * b)
if type == 4:
    print("--division--")
    a = int(input("intiger one: "))
    b = int(input("intiger two: "))
    print(a / b)