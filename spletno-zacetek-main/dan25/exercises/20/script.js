// Vaja 20: Časovniki
// setTimeout. setInterval. Odštevalnik. Gumb za brisanje intervala.
let timerDiv = document.getElementById("timer");
let startBtn = document.getElementById("start");
let stopBtn = document.getElementById("stop");
let intervalId = null;
let timeLeft = 10;
startBtn.addEventListener("click", () => {
    if (intervalId)
        clearInterval(intervalId);
    timeLeft = 10;
    timerDiv.textContent = timeLeft.toString();
    intervalId = window.setInterval(() => {
        timeLeft--;
        timerDiv.textContent = timeLeft.toString();
        if (timeLeft <= 0) {
            clearInterval(intervalId);
            alert("Čas je potekel!");
        }
    }, 1000);
});
stopBtn.addEventListener("click", () => {
    if (intervalId) {
        clearInterval(intervalId);
        intervalId = null;
    }
});
// setTimeout example
setTimeout(() => {
    console.log("To sporočilo se prikaže po 2 sekundah");
}, 2000);
// Fetch button functionality
let fetchBtn = document.getElementById("fetchBtn");
let dataDiv = document.getElementById("data");
fetchBtn.addEventListener("click", () => {
    dataDiv.textContent = "Pridobivam podatke...";
    // Simulate fetch with setTimeout
    setTimeout(() => {
        dataDiv.textContent = "Podatki so bili uspešno pridobljeni!";
    }, 2000);
});
export {};
