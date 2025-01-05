def main():
    text = input()
    print(convert(text))


def convert(input: str):
    return input.replace(":)", "🙂").replace(":(", "🙁")


main()
