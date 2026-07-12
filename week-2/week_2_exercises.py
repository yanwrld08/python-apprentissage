# ============================================================================
# Week 2 Exercises — Conditions et Boucles
# ============================================================================

print("\n" + "="*70)
print("WEEK 2 — CONDITIONS ET BOUCLES")
print("="*70)

# ============================================================================
# Exercise 1: Simple if/else
# ============================================================================

print("\n=== Exercise 1: Age Checker ===")
age = 20

if age >= 18:
    print(f"Age: {age} → Vous êtes majeur")
else:
    print(f"Age: {age} → Vous êtes mineur")


# ============================================================================
# Exercise 2: if/elif/else with grades
# ============================================================================

print("\n=== Exercise 2: Grade Classification ===")
score = 85

if score >= 90:
    grade = "A (Excellent)"
elif score >= 80:
    grade = "B (Très bien)"
elif score >= 70:
    grade = "C (Bien)"
elif score >= 60:
    grade = "D (Passable)"
else:
    grade = "F (Échoué)"

print(f"Score: {score}/100 → Note: {grade}")


# ============================================================================
# Exercise 3: Logical operators (and, or, not)
# ============================================================================

print("\n=== Exercise 3: Logical Operators ===")

# AND example
age = 25
has_license = True

if age >= 18 and has_license:
    print(f"✓ Vous pouvez conduire (age: {age}, license: {has_license})")
else:
    print(f"✗ Vous ne pouvez pas conduire")

# OR example
day = "samedi"

if day == "samedi" or day == "dimanche":
    print(f"✓ {day.capitalize()} c'est le week-end!")
else:
    print(f"✗ {day.capitalize()} c'est un jour de semaine")

# NOT example
is_raining = False

if not is_raining:
    print(f"✓ Pas de pluie, on peut sortir!")
else:
    print(f"✗ Il pleut")


# ============================================================================
# Exercise 4: for loop with range()
# ============================================================================

print("\n=== Exercise 4: Multiplication Table (for loop) ===")
number = 7

print(f"Table de {number}:")
for i in range(1, 11):
    result = number * i
    print(f"  {number} × {i} = {result}")


# ============================================================================
# Exercise 5: for loop with list
# ============================================================================

print("\n=== Exercise 5: Iterate over a List ===")
fruits = ["pomme", "banane", "orange", "raisin", "fraise"]

print("Fruits disponibles:")
for i, fruit in enumerate(fruits, 1):
    print(f"  {i}. {fruit.capitalize()}")


# ============================================================================
# Exercise 6: while loop (counting)
# ============================================================================

print("\n=== Exercise 6: While Loop (Countdown) ===")
count = 5

print("Compte à rebours:")
while count > 0:
    print(f"  {count}...")
    count -= 1  # Abréviation pour count = count - 1

print("  Décollage! 🚀")


# ============================================================================
# Exercise 7: while loop (user input)
# ============================================================================

print("\n=== Exercise 7: Password Validation ===")
correct_password = "python123"
attempt = ""
attempts = 0

while attempt != correct_password:
    attempt = input("Entrez le mot de passe: ")
    attempts += 1
    
    if attempt == correct_password:
        print(f"✓ Accès accordé! (Tentatives: {attempts})")
    else:
        print("✗ Mauvais mot de passe, réessayez.")


# ============================================================================
# Exercise 8: break and continue
# ============================================================================

print("\n=== Exercise 8: Break and Continue ===")

print("Nombres de 1 à 10 (sauf 5, arrêt à 8):")
for i in range(1, 11):
    if i == 5:
        continue  # Saute 5
    if i == 8:
        break  # Arrête à 8
    print(f"  {i}")


# ============================================================================
# Exercise 9: FizzBuzz
# ============================================================================

print("\n=== Exercise 9: FizzBuzz (1 to 30) ===")

for i in range(1, 31):
    output = ""
    
    if i % 3 == 0:
        output += "Fizz"
    if i % 5 == 0:
        output += "Buzz"
    if output == "":
        output = str(i)
    
    print(output, end="  ")

print("\n")


# ============================================================================
# Exercise 10: Nested loops (multiplication table grid)
# ============================================================================

print("\n=== Exercise 10: Multiplication Table Grid ===")

print("     ", end="")
for i in range(1, 6):
    print(f"{i:4}", end="")
print()
print("   " + "-" * 20)

for i in range(1, 6):
    print(f"{i} | ", end="")
    for j in range(1, 6):
        result = i * j
        print(f"{result:4}", end="")
    print()


print("\n" + "="*70)
print("Fin des exercices!")
print("="*70 + "\n")
