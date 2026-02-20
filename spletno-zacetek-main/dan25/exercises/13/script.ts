let vnos = document.getElementById("inputText") as HTMLInputElement;
let gumb = document.getElementById("reverseBtn") as HTMLButtonElement;
let izhod = document.getElementById("output") as HTMLParagraphElement;

gumb.addEventListener("click", () => {
    let besedilo: string = vnos.value;
    let obrnjeno: string = besedilo.split('').reverse().join('');
    izhod.textContent = obrnjeno;
});

export {};