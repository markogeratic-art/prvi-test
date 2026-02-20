// Vaja 15: Interaktivni drsniki
// Dva drsnika obsega. Ohranjaj vsoto 100. Dinamično prilagodi nasprotni drsnik.
// Dva meterja se sinhronizirata z drsniki.
let drsnik1 = document.getElementById("slider1");
let drsnik2 = document.getElementById("slider2");
let meter1 = document.getElementById("meter1");
let meter2 = document.getElementById("meter2");
function updateMeters() {
    meter1.value = parseFloat(drsnik1.value);
    meter2.value = parseFloat(drsnik2.value);
}
function updateSliders() {
    drsnik2.value = (100 - parseFloat(drsnik1.value)).toString();
    meter1.value = parseFloat(drsnik1.value);
    meter2.value = parseFloat(drsnik2.value);
}
function updateSlidersReverse() {
    drsnik1.value = (100 - parseFloat(drsnik2.value)).toString();
    meter1.value = parseFloat(drsnik1.value);
    meter2.value = parseFloat(drsnik2.value);
}
// Osnovni sinhronizacijski eventi
drsnik1.addEventListener("input", updateSliders);
drsnik2.addEventListener("input", updateSlidersReverse);
export {};
