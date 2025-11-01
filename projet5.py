print(f"*** NIVEAU TERMINÉ ! ***")
base_score = 1000

coins_collected_str = int(input("Entrer le nombre de pieces collecte: "))
reponse = input("As-tu terminé le niveau sans subir de dégâts ? (oui/non) : ")

no_damage_bonus = (reponse.lower() == "oui")
print(no_damage_bonus)

coin_bonus = coins_collected_str * 50
if no_damage_bonus:
    damage_multiplier = 2
else:
    damage_multiplier = 1

print(damage_multiplier)

final_score = (base_score + coin_bonus) * damage_multiplier

print(f"score de base {base_score}")
print(f"Bonus {coin_bonus}")
print(f"Multiplicaeur sans degats {damage_multiplier}")
print(f"Le score final est de {final_score}")
