from datetime import datetime
from meteostat_podatki import pridobi_podatke_za_lokacije

def main():
    lokacije = [
        {'ime': 'Ljubljana', 'lat': 46.05, 'lon': 14.51},
        {'ime': 'Reykjavik', 'lat': 64.13, 'lon': -21.82},
        {'ime': 'Singapore', 'lat': 1.35, 'lon': 103.86},
        {'ime': 'Sydney', 'lat': -33.87, 'lon': 151.21},
        {'ime': 'Tokyo', 'lat': 35.68, 'lon': 139.77},
        {'ime': 'Barrow', 'lat': 71.29, 'lon': -156.79},
        {'ime': 'Cairo', 'lat': 30.04, 'lon': 31.24},
        {'ime': 'Buenos_Aires', 'lat': -34.60, 'lon': -58.38},
        {'ime': 'Cape_Town', 'lat': -33.92, 'lon': 18.42},
        {'ime': 'Mumbai', 'lat': 19.08, 'lon': 72.88}
    ]

    zacetek = datetime(1950, 1, 1)
    konec = datetime(2023, 12, 31)

    uspeh, neuspeh = pridobi_podatke_za_lokacije(lokacije, zacetek, konec)

    print(f"\n Uspešno: {uspeh} lokacij.")
    print(f" Neuspešno: {neuspeh} lokacij.")
    print("Končano")

if __name__ == "__main__":
    main()
