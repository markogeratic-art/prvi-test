// Vaja 02: Matematika in operatorji
// Aritmetika: + - * / %
// Povečanje / zmanjšanje
// Primerjalni operatorji (> < >= ===)
// Uporabite Math.round, Math.floor, Math.random
// Praktični primeri (izračun površine, generator naključnih števil)

// Aritmetične operacije
let a: number = 10;
let b: number = 3;
console.log("Seštevanje:", a + b);
console.log("Odštevanje:", a - b);
console.log("Množenje:", a * b);
console.log("Deljenje:", a / b);
console.log("Ostanek:", a % b);
console.log("Potenciranje", a ** b);

// Povečanje in zmanjšanje
let števec: number = 5;
console.log("Prvotno:", števec);
števec++;
console.log("Povečano:", števec);
števec--;
console.log("Zmanjšano:", števec);

// Primerjalni operatorji
console.log("a > b:", a > b);
console.log("a < b:", a < b);
console.log("a >= b:", a >= b);
console.log("a === b:", a === b);

// Matematične funkcije
let število: number = 3.7;
console.log("Math.round:", Math.round(število));
console.log("Math.floor:", Math.floor(število));
console.log("Math.random:", Math.random());

// Praktični primeri
// Izračun površine
let dolžina: number = 5;
let širina: number = 3;
let površina: number = dolžina * širina;
console.log("Površina pravokotnika:", površina);

// Generator naključnih števil
let naključnoŠtevilo: number = Math.floor(Math.random() * 100) + 1;
console.log("Naključno število med 1 in 100:", naključnoŠtevilo);

export {};