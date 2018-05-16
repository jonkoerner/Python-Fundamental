
function coinchange(cents){
var q, d, n, p;
    var dict= {"Quarters": q, "Dimes": d, "Nickels": n, "Pennies": p};
    var x = cents;

    dict["Quarters"]= Math.floor(x/25);
        x= x% 25;
    dict["Dimes"] = Math.floor(x / 10);
        x = x % 10;e
    dict["Nickels"] = Math.floor(x / 5);
        x = x % 5;
    dict["Pennies"] = x

    console.log(dict);
}

coinchange(94)