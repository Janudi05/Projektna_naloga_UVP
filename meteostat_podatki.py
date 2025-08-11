import os
from datetime import datetime
import pandas as pd
from meteostat import Point, Daily
from tqdm import tqdm

OSNOVNA_MAPA = "Podatki"
MAPA_NEOPREDELANI = os.path.join(OSNOVNA_MAPA, "ne_predelani")

def ustvari_mapo(pot):
    os.makedirs(pot, exist_ok=True)

def shrani_podatke(df, lokacija_ime, leto):
    pot = os.path.join(MAPA_NEOPREDELANI, lokacija_ime)
    ustvari_mapo(pot)
    datoteka = os.path.join(pot, f"{lokacija_ime}_{leto}_temperature.csv")
    df.to_csv(datoteka)

def pridobi_podatke_za_lokacije(lokacije, zacetek, konec):
    uspeh = 0
    neuspeh = 0
    
    for lokacija in tqdm(lokacije, desc="Pridobivanje podatkov"):
        tocka = Point(lokacija['lat'], lokacija['lon'])
        podatki = Daily(tocka, zacetek, konec)
        df = podatki.fetch()
        
        if df.empty:
            neuspeh += 1
            continue
        
        df = df.reset_index()
        df['temperatura_avg'] = df['tavg']
        df = df[['time', 'temperatura_avg']]
        
        for leto in df['time'].dt.year.unique():
            df_leto = df[df['time'].dt.year == leto]
            shrani_podatke(df_leto, lokacija['ime'], leto)
        
        uspeh += 1
    
    return uspeh, neuspeh
