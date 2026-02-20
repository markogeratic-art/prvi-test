// Vaja 03: Preproste funkcije
// Deklaracije funkcij. Parametri in vrnjene vrednosti. Puščice funkcije. Izrazi funkcij. Klicanje funkcij večkrat.

// Deklaracija funkcije
function pozdrav(ime: string): string {
    return "Pozdravljen, " + ime;
}

function sestej(a: number, b: number): number {
    return a + b;
}

// Izraz funkcije
const sestej1 = function(a: number, b: number): number {
    return a + b;
};

const pozdrav2 = (ime: string): string => "pozdravljen/a" + ime;


const sestej2 = (a: number, b: number): number => a + b;

// Puščica funkcija
const zmnoži = (a: number, b: number): number => a * b;

// Klicanje funkcij večkrat
console.log(pozdrav("Svet"));
console.log(pozdrav("TypeScript"));
console.log(sestej(2, 3));
console.log(sestej2(5, 7));
console.log(zmnoži(4, 5));
console.log(zmnoži(3, 8));

export {};