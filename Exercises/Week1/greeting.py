name = input("what is your name?").strip()
age_text = input("how old are you?").strip()
age = int(age_text) 
print("Hello " + name + "," + " in 5 years you will be " + str(age + 5) + " years old.")