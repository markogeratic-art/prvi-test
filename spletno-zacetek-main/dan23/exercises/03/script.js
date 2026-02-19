function pozdrav(ime) {
    return "Pozdravljen + ime";
}

const sestej1 = function(a,b) {
return a + b;
}

const pozdrav2 = (ime) => "pozdravljen/a" + ime

function fib(f) {

    if (f <= 1) {
        return 1;
    }
    return fib(f-1) + fib(f-2);
  
}

console.log(fib(1));
console.log(fib(2));
console.log(fib(3));
console.log(fib(4));