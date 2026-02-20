// Vaja 07: Metode polj
// forEach
// map
// filter
// find
let številke = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
// forEach
console.log("forEach:");
številke.forEach(function (štev) {
    console.log(štev * 2);
});
function podvoji(štev) {
    return štev * 2;
}
// map
console.log("map:");
let podvojene = številke.map(podvoji);
console.log(podvojene);
// filter
console.log("filter:");
let sodeŠtevilke = številke.filter(function (štev) {
    return štev % 2 === 0;
});
console.log(sodeŠtevilke);
// find
console.log("find:");
let prvaSoda = številke.find(function (štev) {
    return štev % 2 === 0;
});
console.log("Prva soda številka:", prvaSoda);
export {};
