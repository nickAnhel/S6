class Shape {
    constructor() {
        if (this.constructor == Shape)
            throw new Error("Abstract classes can't be instantiated.");
    }

    getArea() {
        throw new Error("Method 'getArea()' must be implemented.");
    }

    getPerimeter() {
        throw new Error("Method 'getPerimeter()' must be implemented.");
    }
}


class Rectangle extends Shape {
    constructor(w, h) {
        super();
        this.width = w;
        this.height = h;
    }

    getArea() {
        return this.width * this.height;
    }

    getPerimeter() {
        return (this.width + this.height) * 2;
    }
}


class Circle extends Shape {
    constructor(r) {
        super();
        this.radius = r;
    }

    getArea() {
        return Math.PI * this.radius * this.radius;
    }

    getPerimeter() {
        return 2 * Math.PI * this.radius;
    }
}

r = new Rectangle(1, 2);
console.log("Rect area:", r.getArea());
console.log("Rect perimeter:", r.getPerimeter());

c = new Circle(3);
console.log("Circle area:", c.getArea());
console.log("Circle perimeter:", c.getPerimeter());
