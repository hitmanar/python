print(f"'--- RAPPORT DE FORCE DU MOT DE PASSE ---")
print(f"Longueur d'au moins 8 caractères : ✅' ou '... : ❌")

password = input("Entrer le mot de passe:  ")
password_length = len(password)
has_digit  = any(char.isdigit() for char in password)
print(has_digit)

is_long_enough = True
is_long_enough = password_length >= 8

is_strong = is_long_enough and has_digit
if is_strong:
    print(f"Votre mot de passe est considéré comme fort !")
else:
    print(f" Votre mot de passe peut être amélioré.'.")

