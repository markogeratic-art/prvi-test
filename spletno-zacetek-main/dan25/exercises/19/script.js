// Vaja 19: Seznam opravil
// Dodaj elemente. Odstrani elemente. Delegacija dogodkov. Ohrani opravila v lokalni shrambi.
let vnos = document.getElementById("todoInput");
let gumbDodaj = document.getElementById("addBtn");
let seznam = document.getElementById("todoList");
let opravila = JSON.parse(localStorage.getItem("opravila") || "[]");
function prikažiOpravila() {
    seznam.innerHTML = "";
    opravila.forEach((opravilo, indeks) => {
        let li = document.createElement("li");
        li.textContent = opravilo;
        let gumbOdstrani = document.createElement("button");
        gumbOdstrani.textContent = "Odstrani";
        gumbOdstrani.addEventListener("click", () => {
            opravila.splice(indeks, 1);
            shraniOpravila();
            prikažiOpravila();
        });
        li.appendChild(gumbOdstrani);
        seznam.appendChild(li);
    });
}
function shraniOpravila() {
    localStorage.setItem("opravila", JSON.stringify(opravila));
}
gumbDodaj.addEventListener("click", () => {
    let besedilo = vnos.value.trim();
    if (besedilo) {
        opravila.push(besedilo);
        shraniOpravila();
        prikažiOpravila();
        vnos.value = "";
    }
});
// Začetna prikaza
prikažiOpravila();
export {};
