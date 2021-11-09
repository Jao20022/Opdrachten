def convert(celsius):
    fahrenheit = celsius * 1.8 + 32
    return fahrenheit


def table():
    print("{2:3}{1:7}{0:}".format("C","F",''))
    for celsius in range(-30, 41, 10):
        print(f"{celsius:5} {convert(celsius):7}")



table()
