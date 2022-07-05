/* ************************************************** */
function Limpar() {
    document.getElementById('id_x').value='';
    document.getElementById('id_y').value='';
    document.getElementById('id_resultado').value='';
    document.getElementById('id_console').value = '';
}

function Adicionar(x, y) {
    var result = x+y;
    return(result);
}

function Subtrair(x, y) {
    var result = x-y;
    return(result);
}

function Multiplicar(x, y) {
    var result = x*y;
    return(result);
}

function Dividir(x, y) {
    var result = x/y;
    return(result);
}

function Executar(op) {
    // Questo 06: (Extraia da tela os valores de x e y e armazene em variveis para posterior utilizao)
    var x = parseFloat(document.getElementById('id_x').value);
    var y = parseFloat(document.getElementById('id_y').value);
    // var result = ''
    // Questo 07: (De acordo com a opo 'op' chame a funo para realizar o clculo entre os valores x e y)
    if (op == 'Adic'){
        var result = Adicionar(x,y);
    };
    if (op == 'Sub'){
        var result = Subtrair(x,y);
    };
    if (op == 'Mult'){
        var result = Multiplicar(x,y);
    };
    if (op == 'Div'){
        var result = Dividir(x,y);
    };
    // Questo 08: (Apresente o resultado da operao no componente identificado como: id_resultado)
    document.getElementById('id_resultado').value = result.toFixed(2);
    // Questo 09: (Escreva em uma string os valores de x, y e o resultado. Em seguida,
    //              imprima essa string no componente identificado como: id_console)
    var Str = '';
    Str += 'Variável Valor1 = '+ x+'\n';
    Str += 'Variável Valor2 = '+ y+'\n';
    Str += 'Variável Resultado = '+ result.toFixed(2) + '\n';
    
    document.getElementById('id_console').value = Str;
}
    /* ************************************************** */
