# Analiza globalnih temperaturnih trendov

Ta projekt pridobiva in analizira zgodovinske (1950 - 2024) podnebne podatke za različna mesta po svetu. 
Glavni cilj je analizirati trende segrevanja v različnih klimatskih pasovih ter vizualizirati rezultate.

### Projektna naloga zajema:
  -  Pridobivanje podatkov: Skripti za pridobivanje podatkov iz Meteostat API.

  -  Analiza podatkov: Obdelava in statistična analiza podnebnih podatkov.

  -  Vizualizacija: Grafični prikaz rezultatov analize.

### Cilj projekta
Analizirati temperaturno zgodovino (1950 - 2024) po mestih, letnih časih in regijah ter identificirati podnebne trende.

### Struktura projekta
```
Projektna_naloga_UVP/  
    │  
    ├── Podatki/ 
    │    ├── ne_predelani/  
    │    │   └── Tokyo/  
    │    │   │   ├── Tokyo_1950_temperature.csv  
    │    │   │   ├── Tokyo_1951_temperature.csv
    │    │   │   └── ...  
    │    │   └── Ljubljana/
    │    │       └── ... 
    │    └── rezultati/  
    │        └── ...  
    ├── __pycache__/
    │        └── ... 
    ├── Analiza_podatkov.ipynb  
    ├── zahteve_namestitev.py  
    ├── meteostat_podatki.py 
    ├── requirements.txt
    ├── main.py  
    ├── .gitignore
    └── README.md  
```

### Viri podatkov
- Open-Meteo API za zgodovinske vremenske podatke:

    https://dev.meteostat.net/python/#installation

- Tehnike analize klimatskih podatkov:

    https://climatedataguide.ucar.edu/climate-tools

 ### Navodila za uporabo in zagon projekta

 1. Zaženite notebook: `jupyter notebook Analiza.ipynb`
 
 2. Namestite vse zahtevane knjižnice: `pip install -r requirements.txt`
    ali zaženite vse celice (Run All) v notebooku

 3. Run All

 4. Rezultati bodo shranjeni v mapo `Podatki/rezultati/`
