import random

# Heittää viisi noppaa ja palauttaa ne listana
def heita_nopat():
    nopat = []
    for _ in range(5):
        nopat.append(random.randint(1, 6))
    return nopat

# Näyttää nopat käyttäjälle
def nayta_nopat(nopat):
    print("Nopat:")
    for i, noppa in enumerate(nopat, start=1):
        print(f"Noppa {i}: {noppa}")
    print()

# Laskee noppien summan
def laske_pisteet(nopat):
    return sum(nopat)

# Pääohjelma
def main():
    print("🎲 Tervetuloa Yatzy-peliin!\n")

    nopat = heita_nopat()

    while True:
        nayta_nopat(nopat)

        print("Valitse toiminto:")
        print("1. Heitä nopat uudelleen")
        print("2. Laske pisteet")
        print("3. Lopeta peli")

        valinta = input("Valintasi (1-3): ")

        if valinta == "1":
            nopat = heita_nopat()
        elif valinta == "2":
            pisteet = laske_pisteet(nopat)
            print(f"Noppien summa on: {pisteet}\n")
        elif valinta == "3":
            print("Kiitos pelaamisesta!")
            break
        else:
            print("Virheellinen valinta.\n")

if __name__ == "__main__":
    main()