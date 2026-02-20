let izbirnik = document.getElementById("colorPicker");
izbirnik.addEventListener("input", () => {
    document.body.style.backgroundColor = izbirnik.value;
});
export {};
