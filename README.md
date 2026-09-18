# Order Report

Det här projektet går ut på att förbättra ett befintligt Pythonprogram som läser in orderdata från en CSV-fil och skapar olika rapporter.

Originalprogrammet fungerade, men nästan all kod låg i samma fil. Jag har därför delat upp programmet i flera mindre delar för att göra koden tydligare, lättare att testa och enklare att ändra i framtiden.

Jag har försökt behålla samma beräkningar och resultat som i originalprogrammet.

## Vad programmet gör

Programmet läser orderdata från data/orders.csv.

Datan kontrolleras och rensas innan några beräkningar görs. Programmet räknar bland annat ut ordervärde och värde efter rabatt.

Sedan skapas rapporter för:

- total försäljning och antal ordrar
- försäljning per produktkategori
- försäljning per region
- returer per produktkategori

Rapporterna sparas som CSV-filer i mappen output.

## Installation

Projektet använder pandas och pytest.

Installera det som behövs med:

```bash
pip install -r requirements.txt
```

## Köra programmet

Programmet körs från projektets huvudmapp med:

```bash
python -m src.order_report.main
```

När programmet är klart sparas rapporterna i output-mappen.

## Köra tester

För att köra testerna använder man:

```bash
python -m pytest
```

Testerna kontrollerar bland annat beräkningar, rapporter och att programmet reagerar på felaktig eller tom data.

## Projektstruktur

```text
Order report UPPG1/
├── data/
│   └── orders.csv
├── output/
├── src/
│   └── order_report/
│       ├── __init__.py
│       ├── config.py
│       ├── loading.py
│       ├── main.py
│       ├── processing.py
│       ├── reporting.py
│       └── validation.py
├── tests/
│   ├── test_processing.py
│   └── test_validation.py
├── code_review.md
├── order_report.py
├── README.md
└── requirements.txt
```

## Hur koden är uppdelad

Jag har delat upp programmet så att olika filer har olika ansvar.

main.py är programmets startpunkt och kopplar ihop de olika delarna.

loading.py läser in orderdatan från CSV-filen.

validation.py kontrollerar att datan går att använda, till exempel att obligatoriska kolumner finns.

processing.py rensar datan och gör beräkningar som ordervärde och rabatt.

reporting.py skapar de olika rapporterna och sparar dem som CSV-filer.

config.py innehåller inställningar för bland annat var input- och outputfiler finns.


## Reflektion

### 1. Vilka var de viktigaste problemen i originalkoden?

Ett problem var att nästan all kod låg i samma fil, så det blev ganska mycket kod på samma ställe och svårt att få en bra överblick. Vissa delar av koden upprepades också, till exempel rapporterna för kategori och region. Programmet använde även print() för att visa vad som hände och hade en except Exception som fångade alla fel på samma sätt. Det fanns inte heller några tester som kunde kontrollera att beräkningarna fortfarande blev rätt när man ändrade i koden.

### 2. Vilka förändringar tycker du förbättrade programmet mest?

Den viktigaste förändringen tycker jag var att dela upp koden i flera filer med olika ansvar. Det gjorde det lättare att förstå vad varje del av programmet gör. Jag tycker också att testerna var en viktig förbättring, eftersom jag då kunde kontrollera att beräkningarna fortfarande fungerade efter att jag ändrat och flyttat runt koden.

### 3. Varför valde du den projektstruktur du använde?

Jag valde den här strukturen för att dela upp programmet efter vad de olika delarna gör. Till exempel ligger inläsningen av data i loading.py, beräkningarna i processing.py och rapporterna i reporting.py. På så sätt blir det lättare att hitta i koden och man behöver inte ändra i en stor fil varje gång något ska uppdateras.

### 4. Var använde du OOP/dataclass och varför passade det där?

Jag använde en dataclass som heter ReportConfig för att samla inställningarna för programmet, till exempel var orderfilen finns och var rapporterna ska sparas. Jag tyckte att det passade bra där eftersom de här värdena hör ihop och används som konfiguration för programmet. Resten av programmet består mest av funktioner med tydliga uppgifter, så jag såg ingen anledning att skapa klasser bara för att använda OOP.

### 5. Vilka viktiga beteenden skyddar dina automatiska tester, och vilken nytta ger testerna om programmet förändras i framtiden?

Testerna kontrollerar bland annat att ordervärde och rabatt räknas rätt, att rapporterna räknar försäljning och returer rätt och att antalet unika ordrar blir rätt. Jag testar också att programmet reagerar om obligatoriska kolumner saknas eller om datan är tom. Om programmet ändras i framtiden kan testerna hjälpa till att upptäcka om någon ändring råkar göra så att något som fungerade tidigare slutar fungera.

### 6. Vad var svårast?

Det svåraste var att dela upp originalkoden utan att råka ändra hur programmet fungerade. Det var viktigt att beräkningarna och rapporterna fortfarande gav samma resultat som innan. Jag tyckte också att det var lite svårt i början att veta vilken kod som skulle ligga i vilken fil och hur de olika filerna skulle kopplas ihop med importer.

### 7. Vad hade du velat förbättra ytterligare om du haft mer tid?

Om jag hade haft mer tid hade jag lagt till fler tester för olika typer av felaktig data och gjort valideringen mer noggrann. Jag hade också kunnat göra inställningarna mer flexibla, till exempel så att användaren själv kan välja vilken CSV-fil som ska läsas in och var rapporterna ska sparas.
