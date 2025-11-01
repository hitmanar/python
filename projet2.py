
print(f"--- BUDGET CARBURANT ESTIMÉ ---")

distance_km_str = float(input("Entrer la distance du voyage aller et retour em kilometre: "))
efficiency_str = float(input("Entrer la consommation de carburant en litre pour 100km: "))
price_per_litres_str = float(input("Etrer le prix actuelle du carburant: "))

fuel_needed = (distance_km_str/100) * efficiency_str
total_cost = round(fuel_needed * price_per_litres_str,2)

print(f"la distance total du voyage est de : {distance_km_str}km")
print(f"Le prix total du carburant pour ce voyage est de:{total_cost}$")
print(f"Le nombres total de litres necessaires:{fuel_needed}L")