var numbers = [1, 4, 3, 2, 6, 7, 5];

let swapped;

for (let i = 0; i < numbers.length - 1; i++) {
    swapped = false;

    for (let j = 0; j < numbers.length - i - 1; j++) {
        if (numbers[j] > numbers[j + 1]) {
            [2,3,1]
            let temp = numbers[j];
            numbers[j] = numbers[j + 1]
            numbers[j + 1] = temp;
            swapped = true;
        }
    }

    if (swapped == false) {
        break;
    }
}

console.log(numbers)  