//vi lager en funksjon som fjerner alle duplikat bokstaver.
const unrepeated = (str) => [... new Set(str)].join("");

//vi bruker funksjonen og fjerner unødvendige mellom rom og punktum.
var string1 = unrepeated("dare").replace(" ", "").replace(".", "");
//vi sorterer for å få en rekkefølge i arrayet.
var array = Array.from(string1).sort()

var string2 = unrepeated("read").replace(" ", "").replace(".", "");
var array2 = Array.from(string2).sort();

//vi sender verdiene våre til en function som sjekker om stringene er anagram.
if(array.length == array2.length) {
    sjekkOmAnagram(array, array2);
}
else {
    console.log("Dette er ikke et anagram.")
}

function sjekkOmAnagram(x, y) {
    for(i = 0; i > x.length; i++) {
        if(x[i] != y[i]) {
            return false;
        }
    }
    console.log("Dette er et anagram.")
}


