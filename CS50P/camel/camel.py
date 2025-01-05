def main():
    camel = input("camelCase: ")
    print(camel_to_snake(camel))

def camel_to_snake(camel: str) -> str:
    snake = ""
    for case in camel:
        if case.isupper():
            snake += f"_{case.lower()}"
        else:
            snake += case
    return snake

if __name__ == "__main__":
    main()
