function deafGrandma(str) {
let stringIsUppercase = true;
for (i = 0; i < str.length; i++){
    if (str.match(/[a-z]/g)){
        stringIsUppercase = false;
        break;
    }

}

if (str.length == 0){
    console.log(">")
    console.log("WHAT!?");
}else if(stringIsUppercase == false){
    console.log("> " + str);
    console.log("SPEAK UP, KID!");
}else if (str === "GOODBYE!"){
    console.log("> " + str);
    console.log("LATER, SKATER!");
}else if(stringIsUppercase == true){
    console.log("> " + str);
    console.log("NO, NOT SINCE 1946!");
}



}

deafGrandma("grandma run away");