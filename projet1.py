
print(f"--- RÉSUMÉ DU PAIEMENT ---")

bill_total_str = input("Entrer le montant total de la facture: ")
bill_total = float(bill_total_str)
tip_percentage_str = input("Quel est le pourcentage de pourboire: ")
tip_percentage = int(tip_percentage_str)
num_people = int(input("Quel est le nombre de personne: "))

#calcule du montant total du pourboire

tip_amount = bill_total * (tip_percentage/100)
print(f"Le montant total du pourboire:{tip_amount}$")

total_with_tip = bill_total + tip_amount
print(f"Le montant total:{total_with_tip}$")

amount_per_person = total_with_tip / num_people
print(f"Le montant de chaque personne:${amount_per_person}")

final_amount_per_person = round(amount_per_person, 2)
print(f"Le montant arrondi final:${final_amount_per_person}")

print(f"Base des faits reel avec une facture de :${total_with_tip} \n Avec un pourboire de:${tip_amount}\n Partage avec:{num_people}personnes ")