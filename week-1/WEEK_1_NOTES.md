# Week 1 — Language Basics

## Learning Objectives

- [ ] Understand variables and data types (`int`, `float`, `str`, `bool`)
- [ ] Master basic operators (arithmetic, comparison, logical)
- [ ] Use `print()`, `input()`, and f-strings effectively
- [ ] Write and run a simple Python script

## Key Concepts

### Variables and Types

```python
# Variables store data
name = "Alice"          # string
age = 25                # int
height = 1.75           # float
is_student = True       # bool
```

### Operators

**Arithmetic:** `+`, `-`, `*`, `/`, `//` (floor division), `%` (modulo), `**` (power)

**Comparison:** `==`, `!=`, `<`, `>`, `<=`, `>=`

**Logical:** `and`, `or`, `not`

### Type Conversion

```python
num_str = "42"
num_int = int(num_str)      # "42" → 42
num_float = float(num_int)  # 42 → 42.0
num_back_to_str = str(num_int)  # 42 → "42"
```

### String Formatting (f-strings)

```python
name = "Bob"
age = 30
print(f"Hello {name}, you are {age} years old")
print(f"In 10 years: {age + 10}")
print(f"Price: ${19.99:.2f}")  # Format to 2 decimals
```

### Input and Output

```python
name = input("What's your name? ")  # Always returns a string
age = int(input("How old are you? "))  # Convert if needed
print(f"Hello {name}, age {age}")
```

## Exercises to Complete

1. **week_1_exercises.py** — 6 mini-exercises on basics
2. **unit_converter.py** — Mini-project combining all concepts

## Project: Unit Converter

**What it does:**
- Converts between temperature, distance, and currency
- Uses functions for each conversion
- Menu-based CLI interface

**How to run:**
```bash
python unit_converter.py
```

**Key concepts practiced:**
- Functions with parameters and return values
- User input (`input()`)
- Arithmetic operations
- String formatting (f-strings)
- Conditionals (`if/elif/else`)
- Loops (`while`)

## Common Mistakes to Avoid

- ❌ Forgetting to convert `input()` to the right type (always returns `str`)
- ❌ Mixing up `=` (assignment) and `==` (comparison)
- ❌ Not indenting code blocks properly
- ❌ Using wrong variable names (Python is case-sensitive)

## Tips

1. Always run your code to see if it works
2. Read error messages carefully — they tell you what's wrong
3. Use `print()` to debug: print variables to see their values
4. Test with different inputs

## Next Week Preview

Week 2 covers **Conditions and Loops** — we'll make that Unit Converter even better by adding validation and error handling!

---

**Reflection Question:** What did you find easiest? What was hardest?