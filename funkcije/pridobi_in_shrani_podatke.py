# Uvoz potrebnih knjižnic
import requests  # Za pošiljanje HTTP zahtev do API-ja
import pandas as pd  # Za tabele
import os  # Za ustvarjanje map
from datetime import datetime  # Za datume
from tqdm import tqdm  # Za progress bar



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

def pridobi_podatke(latitude, longitude, start_date, end_date):

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
    elif odgovor.status_code == 429:
        
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
