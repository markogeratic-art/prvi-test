// Vaja 08: Objekti
// Ustvarite objekte. Dostop z piko in oglatimi oklepaji. Dodajte/odstranite lastnosti. Metode objektov. Zanka z for...in in Object.keys().
let oseba = {
    ime: "Janez",
    starost: 30,
    kraj: "New York"
};
console.log("Prvotni objekt:", oseba);
// Dostop z piko
console.log("Ime:", oseba.ime);
// Dostop z oglatimi oklepaji
console.log("Starost:", oseba["starost"]);
// Dodajte lastnost
oseba.poklic = "Razvijalec";
console.log("Po dodajanju poklica:", oseba);
// Odstranite lastnost
delete oseba.kraj;
console.log("Po odstranitvi kraja:", oseba);
// Metoda objekta
oseba.pozdrav = function () {
    console.log("Pozdravljen, moje ime je " + this.ime);
};
oseba.rojstnidan = function () {
    this.starost++;
};
oseba.rojstnidan();
oseba.pozdrav();
// Zanka z for...in
console.log("Lastnosti z for...in:");
for (let ključ in oseba) {
    console.log(ključ + ": " + oseba[ključ]);
}
// Object.keys()
console.log("Ključi:", Object.keys(oseba));
export {};
