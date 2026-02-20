// Vaja 22: Async/Await + Fetch
// Uporabi fetch. Obravnavaj odziv. Razčleni JSON. Uporabi try...catch. Prikaži podatke v DOM.
let gumbPridobi = document.getElementById("fetchBtn");
let podatkiDiv = document.getElementById("data");
gumbPridobi.addEventListener("click", async () => {
    try {
        let odziv = await fetch("https://jsonplaceholder.typicode.com/posts/1");
        if (!odziv.ok) {
            throw new Error("Omrežni odziv ni bil v redu");
        }
        let podatki = await odziv.json();
        podatkiDiv.innerHTML = `<h3>${podatki.title}</h3><p>${podatki.body}</p>`;
        console.log(podatki);
    }
    catch (napaka) {
        const napakaSporočilo = napaka instanceof Error ? napaka.message : String(napaka);
        podatkiDiv.textContent = "Napaka: " + napakaSporočilo;
        console.error("Napaka pri pridobivanju:", napaka);
    }
});
export {};
