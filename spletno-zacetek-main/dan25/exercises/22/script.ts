// Vaja 22: Async/Await + Fetch
// Uporabi fetch. Obravnavaj odziv. Razčleni JSON. Uporabi try...catch. Prikaži podatke v DOM.

interface Post {
    userId: number;
    id: number;
    title: string;
    body: string;
}

let gumbPridobi = document.getElementById("fetchBtn") as HTMLButtonElement;
let podatkiDiv = document.getElementById("data") as HTMLDivElement;

gumbPridobi.addEventListener("click", async () => {
    try {
        let odziv = await fetch("https://jsonplaceholder.typicode.com/posts/1");
        if (!odziv.ok) {
            throw new Error("Omrežni odziv ni bil v redu");
        }
        let podatki: Post = await odziv.json();
        podatkiDiv.innerHTML = `<h3>${podatki.title}</h3><p>${podatki.body}</p>`;
        console.log(podatki);
    } catch (napaka: unknown) {
        const napakaSporočilo = napaka instanceof Error ? napaka.message : String(napaka);
        podatkiDiv.textContent = "Napaka: " + napakaSporočilo;
        console.error("Napaka pri pridobivanju:", napaka);
    }
});

export {};