# 📝 Week 2 — Conditions et Boucles

## 🎯 Objectif de la semaine

Maîtriser le **contrôle de flux** : faire des choix (`if/elif/else`) et répéter du code (`for`, `while`).

À la fin, vous saurez écrire du code qui prend des décisions et qui itère.

---

## 1️⃣ Les Conditions (`if`, `elif`, `else`)

### Syntaxe de base

```python
if condition:
    # Code exécuté si condition est True
    print("Condition vraie")
else:
    # Code exécuté si condition est False
    print("Condition fausse")
```

### Exemple pratique

```python
age = 15

if age >= 18:
    print("Vous êtes majeur")
else:
    print("Vous êtes mineur")
```

**Résultat :** `Vous êtes mineur`

---

### `elif` (else if) — Plusieurs conditions

```python
score = 75

if score >= 90:
    print("A - Excellent")
elif score >= 80:
    print("B - Très bien")
elif score >= 70:
    print("C - Bien")
else:
    print("D - À améliorer")
```

**Résultat :** `C - Bien`

⚠️ **Important :** Python teste **de haut en bas** et s'arrête à la première condition vraie. Les autres ne sont pas testées.

---

## 2️⃣ Opérateurs de Comparaison

```python
# Égal
5 == 5  # True
5 == 3  # False

# Différent
5 != 3  # True
5 != 5  # False

# Supérieur / Inférieur
5 > 3   # True
5 < 10  # True
5 >= 5  # True
5 <= 4  # False
```

---

## 3️⃣ Opérateurs Logiques

### `and` (ET)

```python
age = 20
has_license = True

if age >= 18 and has_license:
    print("Vous pouvez conduire")
else:
    print("Vous ne pouvez pas conduire")
```

**Résultat :** `Vous pouvez conduire` (les deux conditions sont vraies)

---

### `or` (OU)

```python
day = "samedi"

if day == "samedi" or day == "dimanche":
    print("C'est le week-end!")
else:
    print("C'est un jour de semaine")
```

**Résultat :** `C'est le week-end!`

---

### `not` (NON)

```python
is_raining = False

if not is_raining:
    print("Pas de pluie, on peut sortir!")
else:
    print("Il pleut, restez à l'intérieur")
```

**Résultat :** `Pas de pluie, on peut sortir!`

---

## 4️⃣ Les Boucles `for`

### Itérer sur une plage de nombres

```python
for i in range(1, 6):
    print(i)
```

**Résultat :**
```
1
2
3
4
5
```

**`range(1, 6)` :** de 1 à 5 (6 non inclus)

---

### Itérer sur une liste

```python
fruits = ["pomme", "banane", "orange"]

for fruit in fruits:
    print(f"J'aime les {fruit}s")
```

**Résultat :**
```
J'aime les pommes
J'aime les bananes
J'aime les oranges
```

---

### Table de multiplication avec `for`

```python
number = 5

for i in range(1, 11):
    result = number * i
    print(f"{number} × {i} = {result}")
```

**Résultat :**
```
5 × 1 = 5
5 × 2 = 10
...
5 × 10 = 50
```

---

## 5️⃣ Les Boucles `while`

### Syntaxe de base

```python
while condition:
    # Code répété tant que condition est True
    print("Continuez...")
```

---

### Exemple : Compter jusqu'à 5

```python
count = 1

while count <= 5:
    print(count)
    count += 1  # Abréviation pour count = count + 1
```

**Résultat :**
```
1
2
3
4
5
```

⚠️ **Attention :** Oubliez le `count += 1` et vous êtes en **boucle infinie** ! (Ctrl+C pour arrêter)

---

### `while` vs `for` : Quand utiliser quoi ?

- **`for`** : quand tu sais combien de fois itérer (listes, range)
- **`while`** : quand tu itères jusqu'à une condition (ex: "tant que l'utilisateur ne dit pas 'quit'")

---

## 6️⃣ `break` et `continue`

### `break` — Sortir de la boucle

```python
for i in range(1, 11):
    if i == 5:
        break  # Arrête la boucle
    print(i)
```

**Résultat :**
```
1
2
3
4
```

---

### `continue` — Passer à l'itération suivante

```python
for i in range(1, 6):
    if i == 3:
        continue  # Saute cette itération
    print(i)
```

**Résultat :**
```
1
2
4
5
```

(3 est sauté)

---

## 7️⃣ Exercices Clés

### FizzBuzz

Afficher les nombres de 1 à 100, mais :
- Si divisible par 3 : afficher "Fizz"
- Si divisible par 5 : afficher "Buzz"
- Si divisible par 3 ET 5 : afficher "FizzBuzz"
- Sinon : afficher le nombre

**Astuce :** `i % 3 == 0` veut dire "divisible par 3"

---

### Validation de mot de passe

Demander à l'utilisateur un mot de passe tant qu'il ne tape pas le bon :

```python
correct_password = "python123"
attempt = ""

while attempt != correct_password:
    attempt = input("Entrez le mot de passe: ")
    if attempt == correct_password:
        print("Accès accordé!")
    else:
        print("Mauvais mot de passe, réessayez.")
```

---

## 8️⃣ Résumé des Concepts

| Concept | Utilité |
|---------|---------|
| `if/elif/else` | Faire des choix |
| `and`, `or`, `not` | Combiner des conditions |
| `for` | Itérer un nombre connu de fois |
| `while` | Itérer jusqu'à une condition |
| `break` | Sortir d'une boucle |
| `continue` | Passer à l'itération suivante |

---

## 🎯 Mini-projet : Jeu du nombre mystère

Vous allez créer un jeu où :
1. L'ordinateur pense à un nombre aléatoire entre 1 et 100
2. L'utilisateur essaie de le deviner
3. Après chaque tentative, l'ordi dit "C'est plus haut" ou "C'est plus bas"
4. Le jeu compte les tentatives
5. À la fin, il affiche le score (moins de tentatives = mieux)

**Concepts utilisés :**
- Boucle `while` (tant que pas trouvé)
- Conditions `if/elif/else` (plus haut/bas/trouvé)
- `input()` et conversion de types
- Module `random` pour générer un nombre aléatoire

Vous allez l'implémenter vous-même ! 💪

---

## 📚 Ressources

- [Documentation Python : if statements](https://docs.python.org/3/tutorial/controlflow.html)
- [W3Schools : Python Loops](https://www.w3schools.com/python/python_for_loops.asp)
