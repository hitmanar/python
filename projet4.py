
print(f"--- RECETTE AJUSTÉE ---")

original_amount_str = float(input("Entrer la quantite d'ingredient: "))
original_servings_str = int(input("Pour combien de personne est cette recette: "))
desired_servings_str = int(input("Pour combien de personne est ce repas: "))

scaling_factor = desired_servings_str/original_servings_str
new_amount = round(original_amount_str * scaling_factor, 1)

print(f"La recette originale est pour {original_servings_str} personnes.")
print(f"'Pour cuisiner pour {desired_servings_str} personnes, vous aurez besoin de {new_amount} unités de votre ingrédient.")
