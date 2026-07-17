with open("notes.txt", "w") as file:
    file.write("This is my first note file.")
with open("notes.txt", "r") as file:
    content = file.read()
    print(content)    
try:
    with open("ghost.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("الملف مش موجود")
    