# Pobranie od użytkownika drogi pokonanej przez samochód oraz średniego spalania
droga = float(input("Podaj drogę pokonaną przez samochód (w km): "))
spalanie = float(input("Podaj średnie spalanie samochodu (w litrach na 100 km): "))

# Obliczenie zużycia paliwa
zużycie_paliwa = (droga / 100) * spalanie

# Koszt paliwa
cena_paliwa = 6.5  # Cena paliwa za litr
koszt_podróży = zużycie_paliwa * cena_paliwa

# Wyświetlenie informacji o przewidywanym zużyciu paliwa i kosztach podróży
print("Przewidywane zużycie paliwa: {:.2f} litrów".format(zużycie_paliwa))
print("Szacowane koszty podróży: {:.2f} zł".format(koszt_podróży))