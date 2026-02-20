// Vaja 24: Moduli in Canvas
// Dodaj element canvas v index.html. V script.ts, pridobi kontekst canvasa, nariši oblike (pravokotnike, kroge), črte in besedilo z uporabo API-ja canvas. Prav tako uvozi/izvozi module.
// ZA TO VAJO JE POTREBNO ZAGNATI JO Z LIVE SERVER

const canvas = document.getElementById("myCanvas") as HTMLCanvasElement;
const ctx = canvas.getContext("2d") as CanvasRenderingContext2D;

// Nariši pravokotnik
ctx.fillStyle = "blue";
ctx.fillRect(50, 50, 100, 100);

// Nariši krog
ctx.beginPath();
ctx.arc(250, 100, 50, 0, 2 * Math.PI);
ctx.fillStyle = "red";
ctx.fill();

// Nariši črto
ctx.beginPath();
ctx.moveTo(50, 200);
ctx.lineTo(350, 200);
ctx.strokeStyle = "green";
ctx.lineWidth = 5;
ctx.stroke();

// Nariši besedilo
ctx.font = "30px Arial";
ctx.fillStyle = "black";
ctx.fillText("Risba na Canvas", 100, 300);

// Izvozi funkcijo (modul)
export function narišiTrikotnik(x: number, y: number): void {
    ctx.beginPath();
    ctx.moveTo(x, y);
    ctx.lineTo(x + 50, y + 50);
    ctx.lineTo(x - 50, y + 50);
    ctx.closePath();
    ctx.fillStyle = "yellow";
    ctx.fill();
}

// Uporabi izvoženo funkcijo
narišiTrikotnik(200, 350);
