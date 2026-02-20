let izbirnik = document.getElementById("colorPicker") as HTMLInputElement;

izbirnik.addEventListener("input", () => {
    document.body.style.backgroundColor = izbirnik.value;
});

export {};