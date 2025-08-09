# Analiza temperatur v Sloveniji

Ta projekt izvaja zajem in obdelavo temperaturnih podatkov za 10 slovenskih mest s pomočjo Open-Meteo API-ja. Cilj je analizirati temperaturno zgodovino (2000-2025) po mestih, letnih časih in regijah ter identificirati podnebne trende.

Projektna naloga zajema:
- Pridobivanje zgodovinskih podatkov o temperaturah iz Open-Meteo API-ja
- Shranjevanje podatkov za zadnjih 25 let za 10 slovenskih mest
- Organizacija podatkov v mapah za nadaljno analizo

## Viri podatkov
- Open-Meteo API za zgodovinske vremenske podatke
- Geodetska uprava RS za koordinate mest
- ARSO za validacijo podatkov

## Cilj projekta
Analizirati temperaturno zgodovino (2000-2025) po mestih, letnih časih in regijah ter identificirati podnebne trende.

## Struktura projekta

Projektna_naloga_UVP/  
    │ 
    ├── pridobi_podatke/  
    │   ├── __init__.py  
    │   ├── api_klice.py  
    │   ├── obdelava_podatkov.py  
    │   └── shranjevanje.py  
    ├── podatki/  
    │   ├── Koper/  
    │   │   ├── 2020/  
    │   │   │   ├── 01.csv  
    │   │   │   └── ...  
    │   │   └── ...  
    │   ├── Ljubljana/  
    │   └── ...  
    ├── vizualizacije/  
    │   ├── letni_trendi.png  
    │   ├── mesecne_razlike.png  
    │   └── ...  
    ├── analiza.ipynb  
    ├── config.py  
    ├── main.py  
    ├── .gitignore
    └── README.md  

## Uporabljene knjižnice

Uporabnik za zagon programa mora imeti nameščene knjižnice:  

- requests         # Za komunikacijo z API
- pandas           # Za delo s podatki
- os               # Za datoteke
- datetime         # Za datume
- tqdm             # Za progress bar

## Zagon projekta
