def main():
    mass = int(input("m: "))
    print(convert_mass(mass))

def convert_mass(m: int):
    e = m * 300000000 ** 2
    return e

main()
