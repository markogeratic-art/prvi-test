// Vaja 16: Preverjanje obrazca
// Obrazec z imenom, e-pošto, starostjo. Prepreči oddajo. Preveri prazna polja. Preveri format e-pošte. Preverjanje obsega starosti. Prikaži sporočila o napakah.
let obrazec = document.getElementById("myForm");
let napakeDiv = document.getElementById("errors");
obrazec.addEventListener("submit", (e) => {
    e.preventDefault();
    napakeDiv.innerHTML = "";
    let ime = obrazec.elements.namedItem("name").value.trim();
    let email = obrazec.elements.namedItem("email").value.trim();
    let starost = parseInt(obrazec.elements.namedItem("age").value);
    let napake = [];
    if (!ime) {
        napake.push("Ime je obvezno");
    }
    if (!email) {
        napake.push("E-pošta je obvezna");
    }
    else if (!/\S+@\S+\.\S+/.test(email)) {
        napake.push("Neveljaven format e-pošte");
    }
    if (!obrazec.elements.namedItem("age").value) {
        napake.push("Starost je obvezna");
    }
    else if (starost < 18 || starost > 100) {
        napake.push("Starost mora biti med 18 in 100");
    }
    if (napake.length === 0) {
        alert("Obrazec uspešno oddan!");
    }
    else {
        napake.forEach((napaka) => {
            let p = document.createElement("p");
            p.textContent = napaka;
            p.style.color = "red";
            napakeDiv.appendChild(p);
        });
    }
});
export {};
