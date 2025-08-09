import os
import pandas as pd
from tqdm import tqdm

def nalozi_vse_podatke(pot='podatki'):
    """
    Nalaga vse temperaturno podatke iz hierarhične strukture:
    podatki/[kraj]/[leto]/[mesec].csv
    
    Vrne: DataFrame z vsemi podatki
    """
    vsi_podatki = []
    kraji = [k for k in os.listdir(pot) if os.path.isdir(os.path.join(pot, k))]
    
    for kraj in tqdm(kraji, desc="Kraji"):
        kraj_pot = os.path.join(pot, kraj)
        leta = [l for l in os.listdir(kraj_pot) if os.path.isdir(os.path.join(kraj_pot, l))]
        
        for leto in leta:
            leto_pot = os.path.join(kraj_pot, leto)
            meseci = [m for m in os.listdir(leto_pot) if m.endswith('.csv')]
            
            for mesec_dat in meseci:
                try:
                    df = pd.read_csv(os.path.join(leto_pot, mesec_dat))
                    df['kraj'] = kraj
                    df['leto'] = int(leto)
                    df['mesec'] = int(mesec_dat.replace('.csv', ''))
                    vsi_podatki.append(df)
                except Exception as e:
                    print(f"Napaka pri branju {kraj}/{leto}/{mesec_dat}: {str(e)}")
    
    if not vsi_podatki:
        raise ValueError("Ni bilo mogoče naložiti podatkov - mapa je prazna ali struktura ne ustreza")
    
    df = pd.concat(vsi_podatki, ignore_index=True)
    df['datum'] = pd.to_datetime(df['datum'])
    return df