# ============================================================================
# Week 2 Mini-Project: Guessing Game (Le Jeu du Nombre Mystère)
# ============================================================================

import random

def guessing_game():
    """
    Jeu du nombre mystère:
    - L'ordinateur pense à un nombre aléatoire entre 1 et 100
    - L'utilisateur essaie de le deviner
    - L'ordi guide avec "C'est plus haut" ou "C'est plus bas"
    - Le jeu compte les tentatives
    - À la fin, il affiche le score
    """
    
    print("\n" + "="*60)
    print("🎮 BIENVENUE AU JEU DU NOMBRE MYSTÈRE!")
    print("="*60)
    print("\nL'ordinateur pense à un nombre entre 1 et 100.")
    print("À vous de le deviner! 🔮\n")
    
    # Générer le nombre mystère
    secret_number = random.randint(1, 100)
    guess = None
    attempts = 0
    
    # Boucle principale
    while guess != secret_number:
        try:
            # Demander à l'utilisateur de deviner
            guess = int(input("Entrez votre nombre: "))
            attempts += 1
            
            # Vérifier si le nombre est dans la plage valide
            if guess < 1 or guess > 100:
                print("⚠️  Veuillez entrer un nombre entre 1 et 100!")
                continue
            
            # Comparer et donner un indice
            if guess < secret_number:
                print(f"📈 C'est plus HAUT que {guess}!")
            elif guess > secret_number:
                print(f"📉 C'est plus BAS que {guess}!")
            else:
                print(f"\n🎉 BRAVO! Vous avez trouvé {secret_number}!")
                print(f"✅ Nombre de tentatives: {attempts}")
                
                # Évaluer la performance
                if attempts <= 5:
                    print("⭐⭐⭐ Performance: EXCEPTIONNELLE!")
                elif attempts <= 10:
                    print("⭐⭐ Performance: TRÈS BIEN!")
                elif attempts <= 20:
                    print("⭐ Performance: BON!")
                else:
                    print("Performance: À améliorer...")
                
        except ValueError:
            print("❌ Erreur: Veuillez entrer un nombre valide!")
    
    print("="*60 + "\n")


def play_again():
    """
    Demande si l'utilisateur veut rejouer
    """
    while True:
        response = input("Voulez-vous rejouer? (oui/non): ").lower().strip()
        
        if response in ["oui", "o", "yes", "y"]:
            return True
        elif response in ["non", "n", "no"]:
            return False
        else:
            print("⚠️  Veuillez répondre par 'oui' ou 'non'!")


def main():
    """
    Fonction principale - lance le jeu
    """
    playing = True
    
    while playing:
        guessing_game()
        playing = play_again()
    
    print("\n👋 Merci d'avoir joué! À bientôt!")


# Point d'entrée du programme
if __name__ == "__main__":
    main()
