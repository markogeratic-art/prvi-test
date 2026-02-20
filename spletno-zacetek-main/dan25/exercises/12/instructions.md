# 🌐 Vaja 12: Pridobi dejstvo o psu (Fetch + JSON + DOM)

## 🎯 Cilj
Uporabi `fetch` in `async/await`, da:
- pridobiš naključno dejstvo o psu iz API-ja,
- iz JSON objekta izbereš samo besedilo dejstva,
- ga prikažeš v HTML (ne v konzoli).

---

## 📘 Navodila

1. Ustvari gumb z napisom **"Pridobi dejstvo"**.
2. Ustvari prazen `<p>` ali `<div>` element za prikaz dejstva.
3. Ob kliku na gumb:
   - Pokliči API:
     ```
     https://dogapi.dog/api/v2/facts
     ```
   - Pretvori odgovor v JSON.
   - Iz JSON objekta pridobi samo vrednost ključa:
     ```
     data[0].attributes.body
     ```
   - To vrednost vstavi v HTML z uporabo `textContent`.

4. Ne uporabljaj `console.log()` za prikaz podatkov.
5. Dodaj `try...catch` za obravnavo napak.

---

## 💡 Namig

API vrne objekt v obliki:

```json
{
  "data": [
    {
      "attributes": {
        "body": "Dog fact here..."
      }
    }
  ]
}
```

## TypeScript
- Ustvarite interface za API odgovor
- Uporabite `Promise<void>` za async funkcijo
- Uporabite type assertions za DOM elemente