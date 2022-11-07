with open("file.txt") as file:
    content = file.read()
    print(content)

#if no file is present, it will create new file from scratch
with open("file.txt",mode="w") as file:
    file.write("updated content")