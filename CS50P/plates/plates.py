def main():
    plate = input("Plate: ")
    if is_valid(plate.upper()):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if (
        s.isalnum()
        and check_length(s)
        and check_first_two_letters(s)
        and check_numbers(s)
    ):
        return True
    else:
        return False


def check_numbers(s):
    index = get_intedx(s)
    if not index:
        return True
    if s[index] != "0" and s[index:].isdigit():
        return True
    else:
        return False


def get_intedx(s):
    for c in s:
        if c.isdigit():
            return s.index(c)


def check_first_two_letters(s):
    if s[:2].isalpha():
        return True
    else:
        return False


def check_length(s):
    if len(s) >= 2 and len(s) <= 6:
        return True
    else:
        return False


main()
