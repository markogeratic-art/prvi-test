// Vaja 21: Obljube
// Ustvari lastne obljube. .then() / .catch(). Simuliraj asinhrono s setTimeout.

function zakasnitev(ms: number): Promise<string> {
    return new Promise(resolve => {
        setTimeout(() => {
            resolve("Zakasnjeno za " + ms + "ms");
        }, ms);
    });
}

function naključnaObljuba(): Promise<string> {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            if (Math.random() > 0.5) {
                resolve("Uspeh!");
            } else {
                reject("Neuspeh!");
            }
        }, 1000);
    });
}

// Uporaba obljub
zakasnitev(2000).then(sporočilo => {
    console.log(sporočilo);
    return naključnaObljuba();
}).then(rezultat => {
    console.log(rezultat);
}).catch(napaka => {
    console.log("Napaka:", napaka);
});

// Drug primer
naključnaObljuba()
    .then(rezultat => console.log("Razrešeno:", rezultat))
    .catch(napaka => console.log("Zavrnjeno:", napaka));

export {};