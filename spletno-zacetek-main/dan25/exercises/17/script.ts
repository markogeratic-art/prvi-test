// Vaja 17: Lokalna shramba (osnove)
// Shrani uporabniško ime. Pridobi ob ponovnem nalaganju. Prikaži shranjene podatke.

let vnos = document.getElementById("nameInput") as HTMLInputElement;
let gumbShrani = document.getElementById("saveBtn") as HTMLButtonElement;
let shranjenoIme = document.getElementById("savedName") as HTMLParagraphElement;

// Pridobi ob nalaganju
let shranjenoImeVrednost: string | null = localStorage.getItem("ime");
if (shranjenoImeVrednost) {
    shranjenoIme.textContent = "Shranjeno ime: " + shranjenoImeVrednost;
}

gumbShrani.addEventListener("click", () => {
    let ime: string = vnos.value.trim();
    if (ime) {
        localStorage.setItem("ime", ime);
        shranjenoIme.textContent = "Shranjeno ime: " + ime;
    }
});

export {};