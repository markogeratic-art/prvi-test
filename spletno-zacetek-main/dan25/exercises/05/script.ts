// Vaja 05: Zanke
// for zanke
// while zanke
// break in continue
// Zanka čez polja
// Osnovne gnezdene zanke

// for zanka
console.log("For zanka:");

{
    for (let i: number = 0; i < 5; ++i) {
        console.log("Iteracija:", i);
    }
}

function a(): void {
    let i: number = 200;
}

// while zanka
console.log("While zanka:");
let j: number = 0;
while (j < 5) {
    console.log("Iteracija:", j);
    j++;
}


// break in continue
console.log("Break in continue:");
for (let k: number = 0; k < 10; k++) {
    if (k === 3) continue; // Preskoči 3
    if (k === 7) break; // Ustavi pri 7
    console.log("Številka:", k);
}

// Zanka čez polja
let sadje: string[] = ["jabolko", "banana", "češnja"];
console.log("Zanka čez polje:");
for (let i: number = 0; i < sadje.length; i++) {
    console.log(sadje[i]);
}

// Osnovne gnezdene zanke
console.log("Gnezdene zanke:");
for (let vrstica: number = 0; vrstica < 3; vrstica++) {
    for (let stolpec: number = 0; stolpec < 3; stolpec++) {
        console.log(`Vrstica ${vrstica}, Stolpec ${stolpec}`);
    }
}

export {};