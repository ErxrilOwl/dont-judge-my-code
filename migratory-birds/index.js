function migratoryBirds(arr) {
    // Write your code here
    const birdSet = {};
    
    for (let i = 0; i < arr.length; i++) {
        if (birdSet[arr[i]] >= 0) {
            birdSet[arr[i]] += 1;
        } else {
            birdSet[arr[i]] = 0;
        }
    }

    const birdSetArray = [];
    const uniqueBirdType = Object.keys(birdSet);
    for (let i = 0; i < uniqueBirdType.length; i++) {
        birdSetArray.push({ type: uniqueBirdType[i], count: birdSet[uniqueBirdType[i]] });
    }
    
    birdSetArray.sort((b1, b2) => {
       if (b1.count < b2.count) return 1;
       if (b1.count > b2.count) return -1;
       
       if (b1.type < b2.count) return 1;
       return 0;
    });
    
    return birdSetArray[0].type;
}

const arr = [1, 4, 4, 4, 5, 3]
console.log(migratoryBirds(arr))