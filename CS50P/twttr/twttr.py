def main():
    s = input("Input: ")
    pop_vowels(s)


def pop_vowels(s):
    vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    for c in s:
        if c in vowels:
            c = ""
        else:
            print(c, end="")
    print()


if __name__ == "__main__":
    main()
