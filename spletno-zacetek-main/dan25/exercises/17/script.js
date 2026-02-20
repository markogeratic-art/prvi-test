// Vaja 17: Lokalna shramba (osnove)
// Shrani uporabniško ime. Pridobi ob ponovnem nalaganju. Prikaži shranjene podatke.
let vnos = document.getElementById("nameInput");
let gumbShrani = document.getElementById("saveBtn");
let shranjenoIme = document.getElementById("savedName");
// Pridobi ob nalaganju
let shranjenoImeVrednost = localStorage.getItem("ime");
if (shranjenoImeVrednost) {
    shranjenoIme.textContent = "Shranjeno ime: " + shranjenoImeVrednost;
}
gumbShrani.addEventListener("click", () => {
    let ime = vnos.value.trim();
    if (ime) {
        localStorage.setItem("ime", ime);
        shranjenoIme.textContent = "Shranjeno ime: " + ime;
    }
});
export {};
