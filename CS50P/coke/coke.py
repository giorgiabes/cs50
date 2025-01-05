def main():
    amount_due = 50
    change_owed = -50
    accepted_denominations = [5, 10, 25]
    while amount_due > 0:
        print(f"Amount Due: {amount_due}")
        coin = int(input("Insert coin: "))
        if coin in accepted_denominations:
            amount_due -= coin
            change_owed += coin

    print(f"Change Owed: {change_owed}")


if __name__ == "__main__":
    main()
