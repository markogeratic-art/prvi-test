# Dan 25: TypeScript Vaje

Ta mapa vsebuje TypeScript različico vaj iz dan23. Vse datoteke so bile pretvorjene iz JavaScript v TypeScript z ustreznimi tipi, vmesniki in type assertions.

## Zaganjenje preko spleta
[Typescript online](https://www.typescriptlang.org/play/)

## Namestitev

### 1. Namestite TypeScript (če še ni nameščen)

```bash
npm install -g typescript
```

Ali lokalno v projektu:

```bash
npm init -y
npm install typescript --save-dev
```

### 2. Namestite Visual Studio Code razširitve

Za delo s TypeScriptom in hitri razvoj priporočamo naslednje razširitve:

- **[JavaScript and TypeScript Nightly](https://marketplace.visualstudio.com/items?itemName=ms-vscode.vscode-typescript-next)** - Omogoča typescript@next za VS Code's vgrajeno JavaScript in TypeScript podporo (od Microsoft)
- **[Live Server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer)** - Lokalni razvojni strežnik s samodejnim osveževanjem

## Kako delati z TypeScriptom

### Možnost 1: Ročno prevajanje

1. Odprite terminal v mapi `dan25`
2. Zaženite TypeScript prevajalnik:
   ```bash
   npx tsc
   ```
3. To bo ustvarilo `.js` datoteke iz vseh `.ts` datotek
4. Zaženite Live Server (desni klik na `index.html` → "Open with Live Server")

### Možnost 2: Samodejno prevajanje (watch mode)

1. Zaženite TypeScript v "watch" načinu:
   ```bash
   npx tsc --watch
   ```
2. TypeScript bo samodejno prevajal `.ts` datoteke ob vsaki spremembi
3. Zaženite Live Server

### Možnost 3: Build task v VS Code

1. Pritisnite `Ctrl+Shift+B` (ali `Cmd+Shift+B` na Mac)
2. Izberite "tsc: watch - tsconfig.json"
3. TypeScript bo deloval v ozadju in samodejno prevajal

## Struktura mape

```
dan25/
├── tsconfig.json          # Konfiguracija TypeScript prevajalnika
├── README.md              # Ta datoteka
├── template/              # Predloga za nove vaje
│   ├── index.html
│   ├── script.ts          # TypeScript izvorna koda
│   ├── script.js          # Prevedena JavaScript koda
│   └── style.css
└── exercises/             # Vaje 01-24
    ├── 01/
    │   ├── index.html
    │   ├── instructions.md
    │   ├── script.ts
    │   ├── script.js
    │   └── style.css
    ├── 02/
    │   └── ...
    └── 24/
        └── ...
```

## TypeScript konfiguracija (tsconfig.json)

```json
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "ES2020",
    "lib": ["ES2020", "DOM"],
    "moduleResolution": "node",
    "strict": true,
    "esModuleInterop": true,
    "outDir": "./",
    "rootDir": "./"
  },
  "include": ["**/*.ts"]
}
```

### Pomembne nastavitve:
- **target**: ES2020 - ciljna JavaScript različica
- **module**: ES2020 - uporaba ES modulov
- **lib**: DOM in ES2020 knjižnice
- **strict**: Omogoči striktni način (priporočeno)
- **outDir**: Izhodna mapa za .js datoteke (ista mapa kot .ts)

## Pogoste težave

### Napaka: "Cannot redeclare block-scoped variable"
Vse `.ts` datoteke vsebujejo `export {};` na koncu, da se izognejo tej napaki. To naredi vsako datoteko modul.

### Napaka: "Property 'value' does not exist on type 'HTMLElement'"
Uporabite type assertion:
```typescript
let input = document.getElementById("myInput") as HTMLInputElement;
let value: string = input.value;
```

### Napaka: "'napaka' is of type 'unknown'"
V catch bloku določite tip napake:
```typescript
catch (napaka: unknown) {
    const sporočilo = napaka instanceof Error ? napaka.message : String(napaka);
}
```

## Uporabni TypeScript tipi za DOM

```typescript
// Elementi
let button: HTMLButtonElement = document.getElementById("btn") as HTMLButtonElement;
let input: HTMLInputElement = document.getElementById("input") as HTMLInputElement;
let div: HTMLDivElement = document.getElementById("container") as HTMLDivElement;
let canvas: HTMLCanvasElement = document.getElementById("canvas") as HTMLCanvasElement;

// Kontekst
let ctx: CanvasRenderingContext2D = canvas.getContext("2d") as CanvasRenderingContext2D;

// Dogodki
element.addEventListener("click", (e: MouseEvent) => { });
document.addEventListener("keydown", (e: KeyboardEvent) => { });
```

## Viri

- [TypeScript Dokumentacija](https://www.typescriptlang.org/docs/)
- [TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/)
- [MDN Web Docs - TypeScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference)
