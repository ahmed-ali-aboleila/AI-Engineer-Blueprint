with open("Exercises/Week4/notes.txt", "w") as file:    file.write("This is my first note file.")
with open("Exercises/Week4/notes.txt", "r") as file:
    content = file.read()
    print(content)    
try:
    with open("Exercises/Week4/ghost.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("الملف مش موجود")
