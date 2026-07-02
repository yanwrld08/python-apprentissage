"""
Week 1 Mini-Project: Unit Converter

A simple command-line tool to convert between different units:
- Temperature (Celsius ↔ Fahrenheit)
- Distance (km ↔ miles)
- Currency (USD ↔ EUR with fixed rates)

Concepts practiced:
- Variables and types
- User input with input()
- Arithmetic operations
- String formatting (f-strings)
- print() and basic output
"""

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32


def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9


def km_to_miles(km):
    """Convert kilometers to miles."""
    return km * 0.621371


def miles_to_km(miles):
    """Convert miles to kilometers."""
    return miles * 1.60934


def usd_to_eur(usd):
    """Convert USD to EUR (fixed rate for this example)."""
    return usd * 0.92


def eur_to_usd(eur):
    """Convert EUR to USD (fixed rate for this example)."""
    return eur / 0.92


def display_menu():
    """Display the main menu options."""
    print("\n=== Unit Converter ===")
    print("1. Temperature (°C ↔ °F)")
    print("2. Distance (km ↔ miles)")
    print("3. Currency (USD ↔ EUR)")
    print("4. Exit")
    print("=====================")


def temperature_converter():
    """Handle temperature conversion."""
    print("\n--- Temperature Conversion ---")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    
    choice = input("Choose (1 or 2): ")
    
    if choice == "1":
        celsius = float(input("Enter temperature in Celsius: "))
        result = celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C = {result:.2f}°F")
    elif choice == "2":
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        result = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F = {result:.2f}°C")
    else:
        print("Invalid choice!")


def distance_converter():
    """Handle distance conversion."""
    print("\n--- Distance Conversion ---")
    print("1. Kilometers to Miles")
    print("2. Miles to Kilometers")
    
    choice = input("Choose (1 or 2): ")
    
    if choice == "1":
        km = float(input("Enter distance in km: "))
        result = km_to_miles(km)
        print(f"{km} km = {result:.2f} miles")
    elif choice == "2":
        miles = float(input("Enter distance in miles: "))
        result = miles_to_km(miles)
        print(f"{miles} miles = {result:.2f} km")
    else:
        print("Invalid choice!")


def currency_converter():
    """Handle currency conversion."""
    print("\n--- Currency Conversion ---")
    print("1. USD to EUR")
    print("2. EUR to USD")
    
    choice = input("Choose (1 or 2): ")
    
    if choice == "1":
        usd = float(input("Enter amount in USD: "))
        result = usd_to_eur(usd)
        print(f"${usd} = €{result:.2f}")
    elif choice == "2":
        eur = float(input("Enter amount in EUR: "))
        result = eur_to_usd(eur)
        print(f"€{eur} = ${result:.2f}")
    else:
        print("Invalid choice!")


def main():
    """Main program loop."""
    print("Welcome to the Unit Converter!")
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            temperature_converter()
        elif choice == "2":
            distance_converter()
        elif choice == "3":
            currency_converter()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()