// Vaja 10: Osnovni izbor DOM
// Dodajte odstavek z id. Uporabite getElementById. Spremenite textContent. Spremenite stile. Dodajte/odstranite razrede.

let odstavek = document.getElementById("myPara") as HTMLParagraphElement;
let slider1 = document.getElementById("slider1") as HTMLInputElement;
let meter1 = document.getElementById("meter1") as HTMLMeterElement;
let slider2 = document.getElementById("slider2") as HTMLInputElement;
let meter2 = document.getElementById("meter2") as HTMLMeterElement;

console.log("Prvotno besedilo:", odstavek.textContent);

// Spremenite textContent
odstavek.textContent = "Spremenjeno besedilo";

// Spremenite stile
odstavek.style.color = "red";
odstavek.style.fontSize = "24px";

// Dodajte razred
odstavek.classList.add("highlight");
console.log("Po dodajanju razreda:", odstavek.className);

// Odstranite razred
setTimeout(() => {
    odstavek.classList.remove("highlight");
    console.log("Po odstranitvi razreda:", odstavek.className);
}, 5000);

// Povezava sliderja z metrom
slider1.addEventListener("input", function(this: HTMLInputElement): void {
    meter1.value = parseFloat(this.value);
});
slider2.addEventListener("input", function(this: HTMLInputElement): void {
    meter2.value = parseFloat(this.value);
});

export {};