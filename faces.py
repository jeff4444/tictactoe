def convert(text: str):
    text = text.replace(":(", "🙁")
    text = text.replace(":)", "🙂")
    return text

def main():
    text = input("Enter text: ")
    print(convert(text))


if __name__ == "__main__":
    main()