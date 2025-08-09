# Uvoz potrebnih knjižnic
import pandas as pd  # Za tabele
import os  # Za ustvarjanje map
from datetime import datetime  # Za datume
from tqdm import tqdm  # Za progress bar
import sys
from pathlib import Path

import os
import sys
from pathlib import Path

# 1. Nastavitev poti (že deluje)
current_dir = Path(__file__).parent
functions_dir = current_dir / "funkcije"
sys.path.insert(0, str(functions_dir))
# 2. Dodajanje poti v sys.path
sys.path.insert(0, str(current_dir))
sys.path.insert(0, str(functions_dir))


from pridobi_in_shrani_podatke import pridobi_podatke, shrani_podatke
from nalaganje import nalozi_vse_podatke
    

# Slovenski kraji z njihovimi koordinatami (zemljepisna širina in dolžina)
# Izbranih je 10 reprezentativnih mest iz različnih delov Slovenije
kraji = {
    "Koper": (45.5481, 13.7302),      # Primorska
    "Ljubljana": (46.0569, 14.5058),  # Osrednja Slovenija
    "Maribor": (46.5547, 15.6459),    # Štajerska
    "Bled": (46.3692, 14.1136),       # Gorenjska
    "Novo_mesto": (45.8000, 15.1667), # Dolenjska
    "Murska_Sobota": (46.6586, 16.1594), # Pomurska
    "Celje": (46.2309, 15.2604),      # Savinjska
    "Nova_Gorica": (45.9558, 13.6433), # Goriška
    "Krško": (45.9500, 15.4833),      # Posavje
    "Slovenj_Gradec": (46.5100, 15.0800) # Koroška
}

def main():
    """
    Glavna funkcija, ki koordinira pridobivanje in shranjevanje podatkov.
    """
    # Ustvarimo glavno mapo
    os.makedirs("podatki", exist_ok=True)
    
    # Časovno obdobje (zadnjih 25 let)
    danes = datetime.now()
    end_date = danes.strftime("2024-12-31")
    start_date = ("2000-01-01")
    
    # Progress bar:
    with tqdm(kraji.items(), desc="Pridobivanje podatkov") as pbar:
        for kraj, (lat, lon) in pbar:
            # Posodobimo opis v napredku s trenutnim krajem
            pbar.set_postfix_str(kraj)
            # Pridobimo podatke za trenutni kraj
            podatki = pridobi_podatke(lat, lon, start_date, end_date)
            # Shranimo podatke
            if podatki:
                shrani_podatke(kraj, podatki)
            # Refresh
            pbar.update()
    # Ob zaključku pošljemo sporočilo
    sporocilo = f"""
    Uspešno shranjeni podatki:
    {'- Obdelanih krajev:':<25} {len(kraji):<23}
    {'- Časovno obdobje:':<25} {25} let{'':<18}
    {'- Lokacija shranjevanja:':<25} {"podatki":<23}
    """
    print(sporocilo)


# Zagotovimo, da se glavna funkcija izvede samo, če skripto poženemo neposredno
if __name__ == "__main__":
    main()