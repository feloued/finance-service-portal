def calculate_fee(amount):
    return amount * 0.02


if __name__ == "__main__":
    amount = 1000

    fee = calculate_fee(amount)

    print("Finance Service Portal")
    print("--------------------------")
    print("Transaction Amount:", amount)
    print("Processing Fee:", fee)
