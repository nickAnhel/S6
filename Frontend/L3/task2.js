class Student {
    constructor(name, age, grade) {
        this._name = name;
        this._age = age;
        this._grade = grade;
    }

    set name(value) {
        if (value.length < 2)
            throw new Error("Name must be at least 2 characters long")

        this._name = value;
    }

    get name() {
        return this._name;
    }

    set age(value) {
        if (value <= 0)
            throw new Error("Age must be positive")

        this._age = value;
    }

    get age() {
        return this._age;
    }

    set grade(value) {
        if (value <= 0)
            throw new Error("Grade must be positive")

        this._grade = value;
    }

    get grade() {
        return this._grade;
    }
}


s = new Student("John", 18, 4.5);

console.log("Name:", s.name);
console.log("Age:", s.age);
console.log("Avg grade", s.grade);

s.name = "Ivan";
s.age = 20;
s.grade = 5;

console.log("\nName:", s.name);
console.log("Age:", s.age);
console.log("Avg grade", s.grade);