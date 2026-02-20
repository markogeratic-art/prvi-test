// Vaja 18: Manipulacija JSON
// JSON.stringify. JSON.parse. Shrani objekte v lokalno shrambo. Pridobi in pretvori nazaj.
let gumbShrani = document.getElementById("saveJson");
let gumbNaloži = document.getElementById("loadJson");
let podatkiDiv = document.getElementById("jsonData");
let objekt = { ime: "Janez", starost: 30, hobiji: ["branje", "kodiranje"] };
gumbShrani.addEventListener("click", () => {
    let jsonNiz = JSON.stringify(objekt);
    localStorage.setItem("uporabniškiPodatki", jsonNiz);
    console.log("Shranjeno:", jsonNiz);
});
gumbNaloži.addEventListener("click", () => {
    let jsonNiz = localStorage.getItem("uporabniškiPodatki");
    if (jsonNiz) {
        let razčlenjenObjekt = JSON.parse(jsonNiz);
        podatkiDiv.innerHTML = "<pre>" + JSON.stringify(razčlenjenObjekt, null, 2) + "</pre>";
        console.log("Naloženo:", razčlenjenObjekt);
    }
    else {
        podatkiDiv.textContent = "Ni podatkov";
    }
});
export {};
