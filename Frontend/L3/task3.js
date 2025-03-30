class Calculator {
    static add = (x, y) => x + y;
    static sub = (x, y) => x - y;
    static mul = (x, y) => x * y;
    static div = (x, y) => x / y;
}


console.log("1 + 2 =", Calculator.add(1, 2));
console.log("3 - 2 =", Calculator.sub(3, 2));
console.log("2 * 2 =", Calculator.mul(2, 2));
console.log("1 / 0 =", Calculator.div(1, 0));