function filterArray(arr, callback) {
    let newArr = [];

    for (let item of arr)
        if (callback(item))
            newArr.push(item);

    return newArr;
}


console.log(filterArray([1, 2, 3, 4, 5], it => it % 2 != 0));
console.log(filterArray(["Nick", "Jordan", "Alexander", "Eliza", "Bo"], it => it.length > 4));