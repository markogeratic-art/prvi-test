// Vaja 18: Manipulacija JSON
// JSON.stringify. JSON.parse. Shrani objekte v lokalno shrambo. Pridobi in pretvori nazaj.

interface Uporabnik {
    ime: string;
    starost: number;
    hobiji: string[];
}

let gumbShrani = document.getElementById("saveJson") as HTMLButtonElement;
let gumbNaloži = document.getElementById("loadJson") as HTMLButtonElement;
let podatkiDiv = document.getElementById("jsonData") as HTMLDivElement;

let objekt: Uporabnik = { ime: "Janez", starost: 30, hobiji: ["branje", "kodiranje"] };

gumbShrani.addEventListener("click", () => {
    let jsonNiz: string = JSON.stringify(objekt);
    localStorage.setItem("uporabniškiPodatki", jsonNiz);
    console.log("Shranjeno:", jsonNiz);
});

gumbNaloži.addEventListener("click", () => {
    let jsonNiz: string | null = localStorage.getItem("uporabniškiPodatki");
    if (jsonNiz) {
        let razčlenjenObjekt: Uporabnik = JSON.parse(jsonNiz);
        podatkiDiv.innerHTML = "<pre>" + JSON.stringify(razčlenjenObjekt, null, 2) + "</pre>";
        console.log("Naloženo:", razčlenjenObjekt);
    } else {
        podatkiDiv.textContent = "Ni podatkov";
    }
});

export {};