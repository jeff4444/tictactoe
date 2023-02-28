def calculate(expr: str):
    a, b, c = expr.split(" ")
    a = int(a)
    c = int(c)
    if b == "+":
        ans = a+c
    elif b == "-":
        ans = a-c
    elif b == "*":
        ans = a*c
    elif b == "/":
        if c == 0:
            print("Division by Zero error!")
            return "infinity"
        else:
            ans = a/c
    else:
        ans = "invalid format"
    return ans

def main():
    expression = input("Enter ur espression: ")
    print(expression, "=", calculate(expression))

if __name__ == "__main__":
    main()