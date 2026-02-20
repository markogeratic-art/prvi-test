// Vaja 09: Obravnava napak
// Predstavite try...catch
// Povzročite namerne napake
// Beležite sporočila o napakah po meri
// Basic try...catch
try {
    console.log("Poskušam izvesti kodo...");
    let result = 10 / 0; // This won't throw an error
    console.log("Rezultat:", result);
}
catch (error) {
    console.log("Napaka ujeta:", error.message);
}
// Cause intentional error
try {
    console.log("Attempting to access undefined variable...");
    // @ts-ignore - Intentional error for demonstration
    console.log(undefinedVariable); // This will throw ReferenceError
}
catch (error) {
    console.log("Error caught:", error.message);
}
// Custom error messages
function divide(a, b) {
    try {
        if (b === 0) {
            throw new Error("Division by zero is not allowed");
        }
        return a / b;
    }
    catch (error) {
        console.log("Custom error:", error.message);
        return null;
    }
}
console.log("Divide 10 by 2:", divide(10, 2));
console.log("Divide 10 by 0:", divide(10, 0));
// Try with finally
try {
    console.log("In try block");
    throw new Error("Something went wrong");
}
catch (error) {
    console.log("In catch block:", error.message);
}
finally {
    console.log("This always executes");
}
export {};
