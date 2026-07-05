number = int(input("write a number from 1 to 100: ").strip())
if number < 50:
    print("Low number")
elif number == 50:
    print("Exactly 50")
else:
    print("High number")