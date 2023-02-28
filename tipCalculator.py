def main():
    dollars = dollars_to_float(input("What is the cost of ur meal? "))
    percent = percent_to_float(input("What is the percent u will like to tip? "))
    tip = dollars * percent
    print(f'Leave ${tip:.2f}')


def dollars_to_float(value: str):
    value = float(value)
    return value

def percent_to_float(value: str):
    value = float(value)
    value = value/100
    return value

if __name__ == "__main__":
    main()