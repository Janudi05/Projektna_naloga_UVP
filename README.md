# Analiza globalnih temperaturnih trendov
 V tej projektni nalogi sem pridobil in analiziral podnebne podatke za različne lokacije po svetu med letoma 1950 in 2024. Sestavljata jo dva glavna dela:

 1. **Pridobivanje podatkov**: Datoteka Pridobivanje_podatkov.ipynb je program, za pridobivanje podatkov s pomočjo Meteostat API, ki ima vgrajeno python knjižnico.
 Program jih nato shrani glede na lokacijo in po letih.
 (Glej strukturo projekta spodaj)

 2. **Analiza podatkov**:
 Analiza se osredotoča na tri glavne metrike:
 temperaturne trende, ekstreme izmed temperaturnih podatkov in spremembe v količinah padavin.

## Cilj projekta
1. Analizirati dolgoročne (75 let) trende povprečnih letnih temperatur
2. Preučiti pojavnost ekstremno toplih in hladnih dni
3. Raziskati spremembe v količini in distribuciji padavin
4. Primerjati podnebne spremembe med različnimi geografskimi regijami

## Struktura projekta
```
Projektna_naloga_UVP/  
    │  
    ├── Podatki/ 
    │    ├── ne_predelani/  
    │    │   └── Tokyo/  
    │    │   │   ├── Tokyo_1950_temperature.csv  
    │    │   │   ├── Tokyo_1951_temperature.csv
    │    │   │   └── ...  
    │    │   └── Sydney/
    │    │       └── ... 
    │    └── rezultati/  
    │        ├── povprecne_padavine.png
    │        └── ...
    │
    ├── Analiza_podatkov.ipynb  
    ├── zahteve_namestitev.py  
    ├── Pridobivanje_podatkov.ipynb
    ├── globus.gif
    ├── Globus.py
    ├── .gitignore
    └── README.md  
```

## Viri podatkov
- Open-Meteo API za zgodovinske vremenske podatke:

    https://dev.meteostat.net/python/#installation

- Tehnike analize klimatskih podatkov:

    https://climatedataguide.ucar.edu/climate-tools

## Navodila za uporabo in zagon projekta

 1. Klonirajte repozitorij `Projektna_naloga_UVP`.
 
 2. Zaženite notebook: `jupyter notebook Analiza.ipynb`

 3. Kliknite Run All ( ob zagonu bi se vam morale naložiti vse potrebne knjižnice - Prvi Code cell)

 4. Rezultati bodo shranjeni v mapo `Podatki/rezultati/` in posredovani kot Markdown outputi.
