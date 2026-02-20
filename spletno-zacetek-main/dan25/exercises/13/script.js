let vnos = document.getElementById("inputText");
let gumb = document.getElementById("reverseBtn");
let izhod = document.getElementById("output");
gumb.addEventListener("click", () => {
    let besedilo = vnos.value;
    let obrnjeno = besedilo.split('').reverse().join('');
    izhod.textContent = obrnjeno;
});
export {};
