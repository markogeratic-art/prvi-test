# Vaja 16: Preverjanje obrazca

## Cilji
- Ustvariti obrazec z validacijo
- Preprečiti oddajo
- Preveriti prazna polja
- Preveriti format e-pošte
- Preveriti obseg starosti

## Navodila
1. Ustvarite obrazec:
   - Ime (text input)
   - E-pošta (email input)
   - Starost (number input)
   - Gumb za oddajo

2. Preprečite oddajo:
   - Poslušalec dogodka submit
   - event.preventDefault()
   - Preverjanje vseh polj

3. Preverite prazna polja:
   - Preverite, da vsa polja niso prazna
   - Prikažite napake
   - Fokusirajte prvo prazno polje

4. Preverite format e-pošte:
   - Uporabite regularni izraz
   - Preverite, da vsebuje @ in .
   - Prikažite napako za neveljavno e-pošto

5. Preverite obseg starosti:
   - Preverite, da je starost med 18 in 99
   - Prikažite napako za neveljavno starost
   - Obdelajte neštevilske vnose

## Pričakovani rezultat v script.js
- Obrazec z vsemi polji
- Poslušalec dogodka submit
- Funkcije za validacijo
- Prikaz napak

## Namigi
- Preverite, da so vsi pogoji preverjeni
- Poskusite kombinirati različne validacije
- Preverite, da je uporabniški feedback jasno
