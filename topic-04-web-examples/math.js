function addNumbers(x,y){
    if (isNaN(x) || isNaN(y)){
        throw new Error("Please enter valid numbers.");
    }
    return x+y;
}


function subtractNumbers(x,y){
    if (isNaN(x) || isNaN(y)){
        throw new Error("Please enter valid numbers.");
    }
    return x+y;
}

// If in Node.js, export the functions for testing
if (typeof module !== 'undefined' && typeof module.exports !== 'undefined'){
    
}