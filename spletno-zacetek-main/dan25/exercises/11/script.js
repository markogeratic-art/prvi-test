document.addEventListener("DOMContentLoaded", () => {
    // Vaja 11: Poslušalci dogodkov
    // Dodajte gumbe in vnose. click. mouseover. keydown. Spremenite besedilo/stile ob dogodkih.
    let števec = document.getElementById("counter");
    let gumbPovečaj = document.getElementById("incBtn");
    let gumbZmanjšaj = document.getElementById("decBtn");
    let gumbPonastavi = document.getElementById("resetBtn");
    gumbPovečaj.addEventListener("click", () => {
        števec.textContent = (parseInt(števec.textContent || "0") + 1).toString();
    });
    gumbZmanjšaj.addEventListener("click", () => {
        števec.textContent = (parseInt(števec.textContent || "0") - 1).toString();
    });
    gumbPonastavi.addEventListener("click", () => {
        števec.textContent = "0";
    });
    // mouseover
    gumbPovečaj.addEventListener("mouseover", () => {
        gumbPovečaj.style.backgroundColor = "lightgreen";
    });
    gumbPovečaj.addEventListener("mouseout", () => {
        gumbPovečaj.style.backgroundColor = "";
    });
    // keydown
    document.addEventListener("keydown", (e) => {
        if (e.key === "r") {
            števec.textContent = "0";
        }
    });
});
export {};
