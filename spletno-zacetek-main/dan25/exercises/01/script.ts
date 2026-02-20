// Vaja 01: Konzola in spremenljivke
// Uporabite console.log, console.warn, console.error
// Deklarirajte spremenljivke z let in const
// Prijavite nize, številke, logične vrednosti
// Prijavite objekte in polja
// Cilj: Razumeti osnovno sintakso in odpravljanje napak.

// Deklarirajte spremenljivke
let myString: string = "Pozdravljen, svet!";
const myNumber: number = 42;
let myBoolean: boolean = true;

interface MyObject {
    ime: string;
    starost: number;
}

let myObject: MyObject = { ime: "Janez", starost: 30 };
let myArray: (number | string | MyObject)[] = [1, 2, 3, "štiri", myObject];

// Prijavite v konzolo
console.log("Niz:", myString);
console.log("Številka:", myNumber);
console.log("Logična vrednost:", myBoolean);
console.log("Polje:", myArray);
console.log("Objekt:", myObject);

// Uporabite console.warn in console.error
console.warn("To je opozorilo!");
console.error("To je napaka!");
console.error(new Error("To je napaka!"));

export {};