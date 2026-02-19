
//for zanka

console.log ("For zanka:");
for (let i = 0; i < 5; i++) {
    console.log("iteracije:", i);
}

//while zanka

console.log("While zanka:");
let j = 0;
while(j <5) {
    console.log("iteracija:", j);
    j++;
}

//break in continue

console.log("break in continue:");
for (let k = 0; k < 10; k ++) {
    if (k === 3) continue; // preskoči 3
    if (k === 7) break; // ustavi pri 7
    console.log("Številka:", k);
}

