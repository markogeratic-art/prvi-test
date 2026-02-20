document.addEventListener("DOMContentLoaded", () => {
    // Vaja 11: Poslušalci dogodkov
    // Dodajte gumbe in vnose. click. mouseover. keydown. Spremenite besedilo/stile ob dogodkih.
    
    let števec = document.getElementById("counter") as HTMLDivElement;
    let gumbPovečaj = document.getElementById("incBtn") as HTMLButtonElement;
    let gumbZmanjšaj = document.getElementById("decBtn") as HTMLButtonElement;
    let gumbPonastavi = document.getElementById("resetBtn") as HTMLButtonElement;
    
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
        document.addEventListener("keydown", (e: KeyboardEvent) => {
            if (e.key === "r") {
                števec.textContent = "0";
            }
        });
});

export {};