def main():
    file = input("File name: ")
    print(media_type(file))


def media_type(f: str):
    extension = f.split(".")[-1].lower().strip()

    match extension:
        case "gif" | "png":
            return f"image/{extension}"
        case "jpeg" | "jpg":
            return "image/jpeg"
        case "zip" | "pdf":
            return f"application/{extension}"
        case "txt":
            return "text/plain"
        case "bin":
            return "application/octet-stream"
        case _:
            return "application/octet-stream"


main()
