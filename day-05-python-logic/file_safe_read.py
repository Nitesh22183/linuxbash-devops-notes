try:
    with open("same.txt","r") as file:
        content = file.read()
        print(content)
        print("File Content:")
except FileNotFoundError:
    print("File does not Exist")
