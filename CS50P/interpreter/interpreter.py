def main():
    expression = input("Expression: ")
    print(calculator(expression))

def calculator(e: str):
    x, y, z = e.split(" ")
    if y == "+":
        return float(x) + float(z)
    elif y == "-":
        return float(x) - float(z)
    elif y == "*":
        return float(x) * float(z)
    else:
        return float(x) / float(z)


main()
