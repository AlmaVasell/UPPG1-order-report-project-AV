# Code Review – Originalkoden

## 1. Hela programmet ligger i en fil

**Observation:** Nästan all logik ligger direkt i `order_report.py`. Filen läser CSV, validerar data, bearbetar information och sparar rapporter.

**Konsekvens:** Koden blir svår att förstå, återanvända och testa eftersom alla delar är ihopkopplade.

**Förslag:** Dela upp programmet i moduler med tydliga ansvarsområden, exempelvis `loading.py`, `validation.py`, `processing.py` och `reporting.py`.

---

## 2. Programmet använder `print()` för körinformation

**Observation:** Statusmeddelanden som "Startar orderrapport" och "Sparade overview.csv" skrivs ut med `print()`.

**Konsekvens:** Det blir svårt att skilja mellan vanlig information, varningar och fel.

**Förslag:** Ersätt `print()` med Python-modulen `logging` och konfigurera loggningen centralt.

---

## 3. För bred felhantering

**Observation:** Programmet använder `except Exception`.

**Konsekvens:** Alla typer av fel fångas på samma sätt, vilket gör det svårare att förstå vad som faktiskt gick fel.

**Förslag:** Fånga specifika fel, exempelvis `FileNotFoundError`, `ValueError` eller `KeyError`, där det passar.

---

## 4. Duplicerad kod i rapporterna

**Observation:** Koden som skapar rapporter per produktkategori och per region är nästan identisk och använder liknande `groupby`-logik.

**Konsekvens:** Om beräkningen behöver ändras måste samma ändring göras på flera ställen.

**Förslag:** Skapa återanvändbara funktioner som kan användas för flera typer av rapporter.

---

## 5. Ingen tydlig startpunkt

**Observation:** Koden körs direkt när filen startas.

**Konsekvens:** Om filen importeras i ett test eller i en annan modul körs hela programmet direkt.

**Förslag:** Flytta programmets körning till en `main()`-funktion och använd `if __name__ == "__main__":`.

---

## 6. Begränsad validering av data

**Observation:** Programmet kontrollerar om obligatoriska kolumner finns, men valideringen ligger tillsammans med resten av programmet och felmeddelandet är bara "Fel data".

**Konsekvens:** Det blir svårt att förstå vad som är fel med datan och valideringen blir svårare att testa separat.

**Förslag:** Flytta valideringen till en egen modul och ge tydligare felmeddelanden. Kontrollera till exempel om datan är tom och vilka obligatoriska kolumner som saknas.

