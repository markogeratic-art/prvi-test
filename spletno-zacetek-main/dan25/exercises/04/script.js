// Preprosti pogoji
let v;
const input = prompt("nek prompt za stevilo v");
v = input ? parseInt(input) : 0;
let resnica = true;
let neresnica = !resnica;
if (v < 4) {
    console.log("V je manj od 4");
}
else if (v < 50 && v > 10) {
    console.log("V je med 10 in 50");
}
else if (v > 100 || v < -100) {
    console.log("V je med +/-100");
}
else {
    console.log("V je nekaj drugega");
}
export {};
