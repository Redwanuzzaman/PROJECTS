function insertSymbol(number){
    var existingNumbers = $('#result').val();
    $('#result').val(existingNumbers + number);
}

function clearScreen(){
    $('#result').val('');
}

function answer(){
    var result = eval($('#result').val());
    $('#result').val(result);
}

function deleteDigit(){
    var presentVal = $('#result').val();
    if(presentVal != ''){
        $('#result').val(presentVal.slice(0, -1));
    }
}