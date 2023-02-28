def main():
    fileName = input("File Name: ").lower()
    name, extension = fileName.split(".")
    extensions(extension)

def extensions(extension: str):
    match extension:
        case "txt":
            print("document/txt")
        case "pdf":
            print("document/pdf")
        case "gif":
            print("image/gif")
        case "jpg":
            print("image/jpg")
        case "jpeg":
            print("image/jpeg")
        case "png":
            print("image/png")
        case "zip":
            print("compressed/zip")
        case _:
            print("application/octet-stream")


main()