const gumb = document.getElementById("fetchBtn") as HTMLButtonElement;
const seznam = document.getElementById("factsList") as HTMLUListElement;

interface DogFactAttributes {
    body: string;
}

interface DogFactData {
    attributes: DogFactAttributes;
}

interface DogFactResponse {
    data: DogFactData[];
}

async function funkcija123(): Promise<void> {
    try {
        const odgovor = await fetch('https://dogapi.dog/api/v2/facts');
        const podatki: DogFactResponse = await odgovor.json();

        // Dostop do dejstva
        const dejstvo = podatki.data[0].attributes.body;

        // Ustvarimo nov element za dejstvo
        const novElement = document.createElement("li");
        //<li></li>
        novElement.textContent = dejstvo;
        //<li>fun fact</li>
        // Dodamo dejstvo na seznam
        seznam.appendChild(novElement);

    } catch (napaka) {
        console.error(napaka);
        // Prikažemo napako kot nov element na seznamu
        const napakaElement = document.createElement("li");
        napakaElement.textContent = "Prišlo je do napake pri pridobivanju podatkov.";
        seznam.appendChild(napakaElement);
    }
}

gumb.addEventListener("click", funkcija123);

export {};