import random

# Generowanie losowej długości drogi
droga = random.randint(1, 100000)

# Pobranie od użytkownika średniego spalania
spalanie = float(input("Podaj średnie spalanie samochodu (w litrach na 100 km): "))

# Obliczenie zużycia paliwa
zużycie_paliwa = (droga / 100) * spalanie

# Koszt paliwa
cena_paliwa = 6.5  # Cena paliwa za litr
koszt_podróży = zużycie_paliwa * cena_paliwa

# Wyświetlenie informacji o przewidywanym zużyciu paliwa i kosztach podróży
print(f"Przejechana droga: {droga} km")
print(f"Przewidywane zużycie paliwa: {zużycie_paliwa:.2f} litrów")
print(f"Szacowane koszty podróży: {koszt_podróży:.2f} zł")