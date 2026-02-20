// Vaja 07: Metode polj
// forEach
// map
// filter
// find

let številke: number[] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

// forEach
console.log("forEach:");
številke.forEach(function(štev: number): void {
    console.log(štev * 2);
});

function podvoji(štev: number): number {
    return štev * 2;
}

// map
console.log("map:");
let podvojene: number[] = številke.map(podvoji);
console.log(podvojene);

// filter
console.log("filter:");
let sodeŠtevilke: number[] = številke.filter(function(štev: number): boolean {
    return štev % 2 === 0;
});
console.log(sodeŠtevilke);

// find
console.log("find:");
let prvaSoda: number | undefined = številke.find(function(štev: number): boolean {
    return štev % 2 === 0;
});
console.log("Prva soda številka:", prvaSoda);

export {};