def main():
    greeting = input("Greeting: ")
    print(say_hello(greeting))

def say_hello(s: str):
    s = s.strip().lower()
    first_word = s.split(" ")[0]
    if first_word == "hello" or first_word == "hello,":
        return "$0"
    elif first_word[0] == "h":
        return "$20"
    else:
        return "$100"

main()
