"""
Program za pridobivanje podatkov o temperaturah za slovenske kraje

Pridobi zgodovinske podatke o temperaturah iz Open-Meteo API-ja
za 10 slovenskih mest in jih shrani po letih in mesecih.
"""

# Uvoz potrebnih knjižnic
import requests  # Za pošiljanje HTTP zahtev do API-ja
import pandas as pd  # Za tabele
import os  # Za ustvarjanje map
from datetime import datetime  # Za datume
from tqdm import tqdm  # Za progress bar

# Nastavimo konstante
API_NASLOV = "https://archive-api.open-meteo.com/v1/archive"
STEVILO_LET = 25
CASOVNI_PAS = "Europe/Berlin"
IMENIK_PODATKOV = "podatki"
MAX_CAKANJE = 15  # sekund

# Slovenski kraji z njihovimi koordinatami (zemljepisna širina in dolžina)
# Izbranih je 10 reprezentativnih mest iz različnih delov Slovenije
kraji = {
    "Koper": (45.5481, 13.7302),      # Primorska regija
    "Ljubljana": (46.0569, 14.5058),  # Osrednja Slovenija
    "Maribor": (46.5547, 15.6459),    # Podravje (Štajerska)
    "Bled": (46.3692, 14.1136),       # Gorenjska regija
    "Novo_mesto": (45.8000, 15.1667), # Dolenjska regija
    "Murska_Sobota": (46.6586, 16.1594), # Pomurska regija
    "Celje": (46.2309, 15.2604),      # Savinjska regija
    "Nova_Gorica": (45.9558, 13.6433), # Goriška regija
    "Krško": (45.9500, 15.4833),      # Posavje
    "Slovenj_Gradec": (46.5100, 15.0800) # Koroška regija
}

def pridobi_podatke(latitude, longitude, start_date, end_date):
    """
    Funkcija za pridobivanje podatkov iz Open-Meteo API-ja.
    
    Parametri:
    lat : Zemljepisna širina kraja
    lon : Zemljepisna dolžina kraja
    start_date : Začetni datum
    end_date : Končni datum
    """
    url = "https://archive-api.open-meteo.com/v1/archive"  # URL API-ja
    # Parametri za API zahtevo
    parametri = {
        "latitude": latitude,
        "longitude": longitude,
        "start_date": start_date,
        "end_date": end_date,
        "daily": "temperature_2m_mean",  # Povprečna dnevna temperatura
        "timezone": "Europe/Berlin"  # Časovni pas
    }
    
    # Pošljemo zahtevo na API in preverimo uspešnost:
    odgovor = requests.get(url, params=parametri)
    
    if odgovor.status_code == 200:  # Uspešna zahteva
        return odgovor.json() 
    else:
        # Neuspešna
        print(f"Napaka pri pridobivanju podatkov: {odgovor.status_code}")
        return None

def shrani_podatke(kraj, podatki):
    """
    Funkcija za shranjevanje podatkov v CSV datoteke po letih in mesecih.
    
    Parametri:
    kraj : Ime kraja
    podatki : Podatki pridobljeni iz API-ja
    """
    try:
        # Ustvarimo DataFrame
        df = pd.DataFrame({
            "datum": podatki["daily"]["time"],
            "temperatura": podatki["daily"]["temperature_2m_mean"]
        })
        
        # Pretvorba datuma v datetime
        df['datum'] = pd.to_datetime(df['datum'])
        # Stolpca za leto in mesec
        df['leto'] = df['datum'].dt.year
        df['mesec'] = df['datum'].dt.month
        
        # Ustvarimo mapo za kraj
        os.makedirs(f"podatki/{kraj}", exist_ok=True)
        
        # Podatki razvrščeni po letih in mesecih
        for (leto, mesec), skupina in df.groupby(['leto', 'mesec']):
            # Ustvarimo mapo za leto
            leto_mapa = f"podatki/{kraj}/{leto}"
            os.makedirs(leto_mapa, exist_ok=True)
            
            # Shranimo podatke za mesec v CSV datoteko
            skupina.to_csv(f"{leto_mapa}/{mesec:02d}.csv", index=False)
            
    except Exception as e:
        pass

def main():
    """
    Glavna funkcija, ki koordinira pridobivanje in shranjevanje podatkov.
    """
    # Ustvarimo glavno mapo
    os.makedirs("podatki", exist_ok=True)
    
    # Časovno obdobje (zadnjih 25 let)
    danes = datetime.now()
    end_date = danes.strftime("%Y-%m-%d")
    start_date = (danes.replace(year=danes.year - 25)).strftime("%Y-%m-%d")
    
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
    {'- Časovno obdobje:':<25} {STEVILO_LET} let{'':<18}
    {'- Lokacija shranjevanja:':<25} {IMENIK_PODATKOV:<23}
    """
    print(sporocilo)

# Zagotovimo, da se glavna funkcija izvede samo, če skripto poženemo neposredno
if __name__ == "__main__":
    main()