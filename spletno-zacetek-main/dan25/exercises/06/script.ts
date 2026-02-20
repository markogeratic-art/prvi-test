// Vaja 06: Polja (osnovno)
// Ustvarite polja. Dostop po indeksu. push, pop, shift, unshift. Zanka čez polja.

// Ustvarite polja
let sadje: string[] = ["jabolko", "banana", "češnja"];
let številke: number[] = [1, 2, 3, 4, 5];

console.log("Prvotno sadje:", sadje);
console.log("Prvotne številke:", številke);

// Dostop po indeksu
console.log("Prvo sadje:", sadje[0]);
console.log("Tretja številka:", številke[2]);

// push, pop
sadje.push("datelj");
console.log("Po push:", sadje);
sadje.pop();
console.log("Po pop:", sadje);

// shift, unshift
številke.unshift(0);
console.log("Po unshift:", številke);
številke.shift();
console.log("Po shift:", številke);

// Zanka čez polja
console.log("Sadje:");
for (let i: number = 0; i < sadje.length; i++) {
    console.log(sadje[i]);
}

console.log("Številke:");
številke.forEach((številka: number) => console.log(številka));


for (let s of številke) { console.log(s); }

export {};