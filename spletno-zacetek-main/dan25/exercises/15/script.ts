// Vaja 15: Interaktivni drsniki
// Dva drsnika obsega. Ohranjaj vsoto 100. Dinamično prilagodi nasprotni drsnik.
// Dva meterja se sinhronizirata z drsniki.

let drsnik1 = document.getElementById("slider1") as HTMLInputElement;
let drsnik2 = document.getElementById("slider2") as HTMLInputElement;
let meter1 = document.getElementById("meter1") as HTMLMeterElement;
let meter2 = document.getElementById("meter2") as HTMLMeterElement;

function updateMeters(): void {
    meter1.value = parseFloat(drsnik1.value);
    meter2.value = parseFloat(drsnik2.value);
}

function updateSliders(): void {
    drsnik2.value = (100 - parseFloat(drsnik1.value)).toString();
    meter1.value = parseFloat(drsnik1.value);
    meter2.value = parseFloat(drsnik2.value);
}

function updateSlidersReverse(): void {
    drsnik1.value = (100 - parseFloat(drsnik2.value)).toString();
    meter1.value = parseFloat(drsnik1.value);
    meter2.value = parseFloat(drsnik2.value);
}

// Osnovni sinhronizacijski eventi
drsnik1.addEventListener("input", updateSliders);

drsnik2.addEventListener("input", updateSlidersReverse);

// Dodatni eventi za meterje (če želimo da se tudi meterji lahko spreminjajo)
// meter1.addEventListener("click", () => {
//     drsnik1.value = meter1.value.toString();
//     updateSliders();
// });
// 
// meter2.addEventListener("click", () => {
//     drsnik2.value = meter2.value.toString();
//     updateSlidersReverse();
// });

export {};