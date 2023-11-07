def main ():
    file_name = input("Filename: ").lower().replace(" ","")
    ext = file_name.rsplit(".",1) [-1]

    match ext:
        case "jpg" | "jpeg":
            print ("image/jpeg")
        case "gif" | "png" :
            print (f"image/{ext}")
        case "pdf"| "zip":
            print (f"application/{ext}")
        case "txt":
            print ("text/plain")
        case _:
            print("application/octet-stream")

main()