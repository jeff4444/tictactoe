def main():
    fraction = input("Fraction: ")
    percent = percentage(fraction)
    print(percent)
    if percent <= 1:
        print("E")
    elif percent >= 99:
        print("F")

def percentage(fraction):
    x, y = fraction.split("/")
    x = int(x)
    y = int(y)
    return ((x/y)*100)