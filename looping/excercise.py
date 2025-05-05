data = [
    {"name": "Nugraha", "birtdate": "1989-09-13"},
    {"name": "John", "birtdate": "1990-01-01"},
    {"name": "Jane", "birtdate": "1992-02-02"},
    {"name": "Doe", "birtdate": "1994-03-03"}
]

# Print the name and age into table using python

print("No\t| Name\t\t| Age |")
for i, data in enumerate(data):
    age = 2025 - int(data["birtdate"].split("-")[0])
    print((i+1), "\t| ", data["name"], "\t\t| " if len(data["name"]) < 5 else "\t| ", age, " |",sep="")


