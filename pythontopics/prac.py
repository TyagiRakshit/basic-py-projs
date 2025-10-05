pets = []
for i in range (3):
    rec = {}
    rec['name'] = input("Enter pet name: ")
    rec['age'] = int(input("Enter pet age: "))
    pets.append(rec)
    
print(pets)
for pet in pets:
    for i in pet:
        print(f"{i}: {pet[i]}")