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


V glavni mapi Projektna naloga so mapi izlusci_podatke in podatki.
V mapi izlusci_podatke se nahajajo .py datoteke. V teh datotekah smo zajeli podatke sa spleta.
Tudi smo na ta način ostvarili nove .csv in .html datoteke, ki so v mapi podatki. Z uporabo teh, podatke bomo analizirali.
V glavni mapi imamo še štiri datoteke. Ena izmed njih je README.md in v njej so navodila za zagon programa.
Druga je analiticne_funkcije.py. V njej so vse funkcije, ki jih potrebujemo za analizu znotraj datoteke analiza_podatkov.ipynb.
Tretja je analiza_podatkov.ipynb, kjer smo z pomočjo Jupyter Notebooka analizirali podatke.
Četrta je main.py, z pomočjo nje poženemo program.  

## Uporabljene knjižnice

Uporabnik za zagon programa mora imeti nameščene knjižnice:  

- requests         # Za komunikacijo z API
- pandas           # Za delo s podatki
- os               # Za datoteke
- datetime         # Za datume
- tqdm             # Za progress bar

## Zagon projekta

Uporabnik naj požene main.py, ki bo ustvaril vse potrebne datoteke.
Tiste bodo shranjene v mapi /podatki.
Na koncu odpremo analiza_podatkov.ipynb in izvedemo analizo.