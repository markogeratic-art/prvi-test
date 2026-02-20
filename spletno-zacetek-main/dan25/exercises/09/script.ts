// Vaja 09: Obravnava napak
// Predstavite try...catch
// Povzročite namerne napake
// Beležite sporočila o napakah po meri

// Basic try...catch
try {
    console.log("Poskušam izvesti kodo...");
    let result: number = 10 / 0; // This won't throw an error
    console.log("Rezultat:", result);
} catch (error) {
    console.log("Napaka ujeta:", (error as Error).message);
}

// Cause intentional error
try {
    console.log("Attempting to access undefined variable...");
    // @ts-ignore - Intentional error for demonstration
    console.log(undefinedVariable); // This will throw ReferenceError
} catch (error) {
    console.log("Error caught:", (error as Error).message);
}

// Custom error messages
function divide(a: number, b: number): number | null {
    try {
        if (b === 0) {
            throw new Error("Division by zero is not allowed");
        }
        return a / b;
    } catch (error) {
        console.log("Custom error:", (error as Error).message);
        return null;
    }
}

console.log("Divide 10 by 2:", divide(10, 2));
console.log("Divide 10 by 0:", divide(10, 0));

// Try with finally
try {
    console.log("In try block");
    throw new Error("Something went wrong");
} catch (error) {
    console.log("In catch block:", (error as Error).message);
} finally {
    console.log("This always executes");
}

export {};