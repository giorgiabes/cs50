def main():
    time = input("What time is it? ")
    if 7 <= convert(time) <= 8:
        print("breakfast time")
    elif 12 <= convert(time) <= 13:
        print("lunch time")
    elif 18 <= convert(time) <= 19:
        print("dinner time")

def convert(t: str) -> float:
    hours, minutes = t.split(":")
    return float(hours) + float(minutes) / 60

if __name__=="__main__":
    main()