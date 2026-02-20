console.log("izpis v konzoli")


document.addEventListener('DOMContentLoaded', () => {
    const gumb = document.getElementById('klik-gumb');

    gumb.addEventListener('click', () => {
        alert('Gumb je bil uspešno kliknjen!');
        console.log('Uporabnik je kliknil na gumb.');
    });
});