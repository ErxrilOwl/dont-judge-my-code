let word1 = "cinema";
let word2 = "iceman";

if (word1.split("").sort().join("") == word2.split("").sort().join("")) {
    console.log("ANAGRAM!")
} else {
    console.log("NOT ANAGRAM!")
}