profile = {
    "name": "Ahmed",
    "age": 22,
    "job": "AI Engineering"
}

print(profile["name"])
print(profile["age"])
print(profile["job"])

profile["city"] = "Alexandria"
profile["age"] = 23

print(profile)
for key, value in profile.items():
    print(key, ":", value)

print("job" in profile)