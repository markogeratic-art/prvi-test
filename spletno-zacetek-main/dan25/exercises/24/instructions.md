# Vaja 24: Moduli in Canvas

## Cilji
- Razumeti uporabo Canvas API-ja za risanje grafike
- Spoznati modulno strukturo v TypeScriptu
- Narediti osnovne risarske operacije na Canvasu
- Implementirati uvoz in izvoz modulov

## Navodila
1. Dodaj element canvas v index.html
2. V script.ts, pridobi kontekst canvasa
3. Nariši osnovne oblike:
   - Pravokotnike
   - Kroge
   - Črte
   - Besedilo
4. Uporabi Canvas API za risanje
5. Implementiraj modulno strukturo:
   - Uvozi potrebne module
   - Izvozi funkcije za risanje

## Pričakovani rezultat v script.ts
- Element canvas ustvarjen v HTML
- Kontekst canvasa pridobljen z `getContext('2d')`
- Funkcije za risanje različnih oblik
- Uporaba Canvas API-ja za risanje
- Implementacija import/export modulov
- Pravilno strukturirana koda z modulno arhitekturo
- TypeScript tipi za canvas element in kontekst

## Namigi
- Uporabi `getContext('2d')` za pridobivanje risarskega konteksta
- Preveri, da je canvas element ustrezne velikosti
- Testiraj različne Canvas metode kot `fillRect()`, `arc()`, `stroke()`, `fillText()`
- Poskrbi za pravilno strukturiranje modulov
- Preveri, da so vsi potrebni moduli pravilno uvoženi
- Uporabi TypeScript type assertions za canvas element (`as HTMLCanvasElement`)
- Uporabi `CanvasRenderingContext2D` tip za kontekst