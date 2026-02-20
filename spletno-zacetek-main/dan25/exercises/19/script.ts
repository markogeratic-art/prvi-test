// Vaja 19: Seznam opravil
// Dodaj elemente. Odstrani elemente. Delegacija dogodkov. Ohrani opravila v lokalni shrambi.

let vnos = document.getElementById("todoInput") as HTMLInputElement;
let gumbDodaj = document.getElementById("addBtn") as HTMLButtonElement;
let seznam = document.getElementById("todoList") as HTMLUListElement;

let opravila: string[] = JSON.parse(localStorage.getItem("opravila") || "[]");

function prikažiOpravila(): void {
    seznam.innerHTML = "";
    opravila.forEach((opravilo: string, indeks: number) => {
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

function shraniOpravila(): void {
    localStorage.setItem("opravila", JSON.stringify(opravila));
}

gumbDodaj.addEventListener("click", () => {
    let besedilo: string = vnos.value.trim();
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