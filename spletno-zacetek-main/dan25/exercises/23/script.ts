// Vaja 23: Razredi
// Konstruktor. Metode. Instanciraj objekte. Dedovanje.

class Oseba {
    ime: string;
    starost: number;

    constructor(ime: string, starost: number) {
        this.ime = ime;
        this.starost = starost;
    }

    pozdrav(): string {
        return `Pozdravljen, moje ime je ${this.ime} in imam ${this.starost} let.`;
    }
}

class Študent extends Oseba {
    ocena: string;

    constructor(ime: string, starost: number, ocena: string) {
        super(ime, starost);
        this.ocena = ocena;
    }

    študiraj(): string {
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