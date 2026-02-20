// Vaja 23: Razredi
// Konstruktor. Metode. Instanciraj objekte. Dedovanje.
class Oseba {
    constructor(ime, starost) {
        this.ime = ime;
        this.starost = starost;
    }
    pozdrav() {
        return `Pozdravljen, moje ime je ${this.ime} in imam ${this.starost} let.`;
    }
}
class Študent extends Oseba {
    constructor(ime, starost, ocena) {
        super(ime, starost);
        this.ocena = ocena;
    }
    študiraj() {
        return `${this.ime} študira v razredu ${this.ocena}.`;
    }
}
// Instanciraj objekte
let oseba1 = new Oseba("Janez", 30);
let študent1 = new Študent("Ana", 20, "A");
console.log(oseba1.pozdrav());
console.log(študent1.pozdrav());
console.log(študent1.študiraj());
export {};
